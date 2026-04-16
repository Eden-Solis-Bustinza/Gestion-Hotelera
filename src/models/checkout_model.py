from src.config.database import db
from datetime import datetime


class CheckoutModel:
    def __init__(self):
        self.db = db

    def buscar_reserva_activa(self, valor_busqueda, is_id_habitacion=False):
        """Busca reserva activa (habitación Ocupada=2) por DNI del huésped o Id de Habitación.
        BUG-02 FIX: ahora incluye tarifa_base de TIPO_HABITACION."""
        conn = self.db.get_connection()
        if not conn:
            return None
        try:
            cursor = conn.cursor()
            
            filtro = "h.id_habitacion = ?" if is_id_habitacion else "hu.nro_documento = ?"
            
            cursor.execute(f"""
                SELECT r.id_reserva,
                       r.id_habitacion,
                       h.numero,
                       r.fecha_checkin,
                       r.fecha_checkout,
                       hu.nombre,
                       hu.apellido,
                       hu.telefono,
                       r.monto_adelantado,
                       th.tarifa_base
                FROM RESERVAS r
                JOIN HUESPEDES     hu ON r.id_huesped    = hu.id_huesped
                JOIN HABITACIONES   h ON r.id_habitacion = h.id_habitacion
                JOIN TIPO_HABITACION th ON h.id_tipo     = th.id_tipo
                WHERE {filtro}
                  AND h.id_estado = 2
                ORDER BY r.fecha_checkin DESC
            """, (valor_busqueda,))
            row = cursor.fetchone()
            conn.close()
            if row:
                reserva_dict = {
                    "id_reserva":       row[0],
                    "id_habitacion":    row[1],
                    "num_habitacion":   row[2],
                    "fecha_in":         row[3],
                    "fecha_out":        row[4],
                    "huesped_nombres":  f"{row[5]} {row[6]}",
                    "huesped_contacto": row[7],
                    "monto_adelanto":   float(row[8]) if row[8] else 0.0,
                    "tarifa_base":      float(row[9]) if row[9] else 0.0,              
                }
                
                cursor.execute("""
                    SELECT c.id_producto, p.nombre, c.cantidad, c.precio_unitario, c.subtotal
                    FROM CONSUMO_RESERVA c
                    JOIN PRODUCTO p ON c.id_producto = p.id
                    WHERE c.id_reserva = ?
                """, (row[0],))
                
                reserva_dict["consumos"] = [
                    {"id_producto": c[0], "nombre": c[1], "cantidad": c[2], "precio": c[3], "subtotal": c[4]}
                    for c in cursor.fetchall()
                ]
                
                return reserva_dict
        except Exception as e:
            print(f"Error al buscar reserva activa: {e}")
            if conn:
                conn.close()
        return None

    def get_metodos_pago(self):
        """BUG-03 FIX: carga métodos de pago desde CAT_METODO_PAGO en BD."""
        conn = self.db.get_connection()
        metodos = []
        if not conn:
            return metodos
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id_metodo, nombre FROM CAT_METODO_PAGO ORDER BY id_metodo")
            metodos = cursor.fetchall()
            conn.close()
        except Exception as e:
            print(f"Error al obtener métodos de pago: {e}")
            if conn:
                conn.close()
        return metodos

    def get_habitaciones_ocupadas(self):
        """Obtiene todas las habitaciones que actualmente están ocupadas."""
        conn = self.db.get_connection()
        habitaciones = []
        if not conn:
            return habitaciones
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id_habitacion, numero FROM HABITACIONES WHERE id_estado = 2 ORDER BY numero")
            habitaciones = cursor.fetchall()
            conn.close()
        except Exception as e:
            print(f"Error al obtener habitaciones ocupadas: {e}")
            if conn:
                conn.close()
        return habitaciones
        
    def get_productos(self):
        """Obtiene todos los productos del inventario y su precio."""
        conn = self.db.get_connection()
        productos = []
        if not conn:
            return productos
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, ISNULL(precio, 10.00) FROM PRODUCTO ORDER BY nombre")
            productos = cursor.fetchall()
            conn.close()
        except Exception as e:
            print(f"Error al obtener productos: {e}")
            if conn:
                conn.close()
        return productos

    def get_detalle_comprobante(self, id_comprobante):
        """Obtiene los datos del comprobante generado para mostrarlo."""
        conn = self.db.get_connection()
        if not conn:
            return None
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT
                    c.numero_comprobante,
                    c.dias_estancia,
                    c.subtotal,
                    c.total_general,
                    mp.nombre         AS metodo_pago,
                    c.fecha_pago,
                    h.numero          AS habitacion,
                    th.nombre         AS tipo_hab,
                    hu.nombre + ' ' + hu.apellido AS huesped,
                    hu.nro_documento,
                    c.id_reserva
                FROM COMPROBANTE c
                JOIN RESERVAS r      ON c.id_reserva    = r.id_reserva
                JOIN HABITACIONES h  ON c.id_habitacion = h.id_habitacion
                JOIN TIPO_HABITACION th ON h.id_tipo    = th.id_tipo
                JOIN HUESPEDES hu    ON r.id_huesped    = hu.id_huesped
                JOIN CAT_METODO_PAGO mp ON c.id_metodo_pago = mp.id_metodo
                WHERE c.id_comprobante = ?
            """, (id_comprobante,))
            row = cursor.fetchone()
            conn.close()
            if row:
                comprobante_dict = {
                    "numero_comprobante": row[0],
                    "dias_estancia":      row[1],
                    "subtotal":           float(row[2]),
                    "total_general":      float(row[3]),
                    "metodo_pago":        row[4],
                    "fecha_pago":         row[5],
                    "habitacion":         row[6],
                    "tipo_hab":           row[7],
                    "huesped":            row[8],
                    "nro_documento":      row[9],
                    "id_reserva":         row[10],
                }

                cursor.execute("""
                    SELECT p.nombre, c.cantidad, c.subtotal
                    FROM CONSUMO_RESERVA c
                    JOIN PRODUCTO p ON c.id_producto = p.id
                    WHERE c.id_reserva = ?
                """, (row[10],))
                
                comprobante_dict["productos_detalle"] = [
                    {"nombre": c[0], "cantidad": c[1], "subtotal": float(c[2])}
                    for c in cursor.fetchall()
                ]
                
                return comprobante_dict
        except Exception as e:
            print(f"Error al obtener comprobante: {e}")
            if conn:
                conn.close()
        return None

    def procesar_checkout(self, id_reserva, id_habitacion, dias_estancia,
                          subtotal, total_general, id_metodo_pago, id_usuario,
                          lista_extras=None):
        """
        Transacción atómica:
          1. INSERT en COMPROBANTE
          2. UPDATE RESERVAS → Completada
          3. UPDATE HABITACIONES → En Limpieza
          4. Registrar en MOVIMIENTO_INVENTARIO los extras consumidos
        Retorna (True, id_comprobante) o (False, None)
        """
        if lista_extras is None:
            lista_extras = []
            
        conn = self.db.get_connection()
        if not conn:
            return False, None

        try:
            conn.autocommit = False
            cursor = conn.cursor()

                                                       
            cursor.execute("""
                INSERT INTO COMPROBANTE
                    (id_reserva, id_habitacion, dias_estancia,
                     subtotal, total_general, id_metodo_pago, id_usuario)
                OUTPUT INSERTED.id_comprobante
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (id_reserva, id_habitacion, dias_estancia,
                  subtotal, total_general, id_metodo_pago, id_usuario))
            row_comp = cursor.fetchone()
            id_comprobante = row_comp[0] if row_comp else None

                                                            
            cursor.execute("""
                SELECT TOP 1 id_estado FROM CAT_ESTADO_RESERVA
                WHERE UPPER(nombre) COLLATE Latin1_General_CI_AI = UPPER('Completada')
                   OR id_estado = 4
                ORDER BY
                    CASE WHEN UPPER(nombre) COLLATE Latin1_General_CI_AI = UPPER('Completada')
                         THEN 0 ELSE 1 END
            """)
            res = cursor.fetchone()
            if not res:
                raise Exception("Falta estado 'Completada' en CAT_ESTADO_RESERVA")
            cursor.execute("UPDATE RESERVAS SET id_estado = ? WHERE id_reserva = ?",
                           (res[0], id_reserva))

                                                                
            cursor.execute("""
                SELECT TOP 1 id_estado FROM CAT_ESTADO_HABITACION
                WHERE UPPER(nombre) COLLATE Latin1_General_CI_AI = UPPER('En Limpieza')
                   OR id_estado = 3
                ORDER BY
                    CASE WHEN UPPER(nombre) COLLATE Latin1_General_CI_AI = UPPER('En Limpieza')
                         THEN 0 ELSE 1 END
            """)
            hab = cursor.fetchone()
            if not hab:
                raise Exception("Falta estado 'En Limpieza' en CAT_ESTADO_HABITACION")
            cursor.execute("UPDATE HABITACIONES SET id_estado = ? WHERE id_habitacion = ?",
                           (hab[0], id_habitacion))

                                                        
            if lista_extras and id_comprobante:
                for extr in lista_extras:
                    id_prod = extr['id_producto']
                    cant = extr['cantidad']
                    subtotal_ext = extr['subtotal']
                    precio_uni = subtotal_ext / cant if cant > 0 else 0
                    
                    cursor.execute("""
                        INSERT INTO MOVIMIENTO_INVENTARIO 
                        (producto_id, cantidad, tipo, id_comprobante, id_usuario)
                        VALUES (?, ?, 'salida', ?, ?)
                    """, (id_prod, cant, id_comprobante, id_usuario))
                    
                    # Insert in CONSUMO_RESERVA if not already from reservation
                    cursor.execute("SELECT 1 FROM CONSUMO_RESERVA WHERE id_reserva = ? AND id_producto = ? AND subtotal = ?", (id_reserva, id_prod, subtotal_ext))
                    if not cursor.fetchone():
                        cursor.execute("""
                            INSERT INTO CONSUMO_RESERVA (id_reserva, id_producto, cantidad, precio_unitario, subtotal)
                            VALUES (?, ?, ?, ?, ?)
                        """, (id_reserva, id_prod, cant, precio_uni, subtotal_ext))

            conn.commit()
            return True, id_comprobante

        except Exception as e:
            print(f"Error procesando checkout: {e}")
            conn.rollback()
            return False, None
        finally:
            conn.autocommit = True
            conn.close()
