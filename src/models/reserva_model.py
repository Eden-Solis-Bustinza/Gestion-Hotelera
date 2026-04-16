from src.config.database import db

class ReservaModel:
    def __init__(self):
        self.db = db

    def buscar_huesped_por_dni(self, dni):
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id_huesped, nombre, apellido, telefono, email 
                    FROM HUESPEDES 
                    WHERE nro_documento = ?
                """, (dni,))
                row = cursor.fetchone()
                conn.close()
                if row:
                    return {
                        "id": row[0], 
                        "nombres": f"{row[1]} {row[2]}", 
                        "contacto": row[3],
                        "email": row[4]
                    }
            except Exception as e:
                print(f"Error al buscar huésped: {e}")
                if conn: conn.close()
        return None

    def get_habitaciones_disponibles(self, fecha_in, fecha_out):
        conn = self.db.get_connection()
        habitaciones = []
        if conn:
            try:
                cursor = conn.cursor()
                                                                         
                cursor.execute("""
                    SELECT h.id_habitacion, h.numero, t.nombre as tipo, t.tarifa_base
                    FROM dbo.FN_HabitacionesDisponibles(?, ?) f
                    JOIN HABITACIONES h ON h.id_habitacion = f.id_habitacion
                    JOIN TIPO_HABITACION t ON t.id_tipo = h.id_tipo
                """, (fecha_in, fecha_out))
                habitaciones = cursor.fetchall()
                conn.close()
            except Exception as e:
                print(f"Error al obtener diponibilidad: {e}")
                if conn: conn.close()
        return habitaciones

    def get_metodos_pago(self):
        conn = self.db.get_connection()
        metodos = []
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT id_metodo, nombre FROM CAT_METODO_PAGO")
                metodos = cursor.fetchall()
                conn.close()
            except Exception as e:
                if conn: conn.close()
        return metodos

    def get_productos(self):
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

    def crear_reserva(self, id_huesped, id_habitacion, num_huespedes, fecha_in, fecha_out, monto, id_usuario, lista_extras=None):
        if lista_extras is None:
            lista_extras = []
        conn = self.db.get_connection()
        if not conn: return False
        
        try:
            conn.autocommit = False 
            cursor = conn.cursor()

            cursor.execute("SELECT id_estado FROM CAT_ESTADO_RESERVA WHERE nombre = ?", ('Pendiente',))
            res_estado = cursor.fetchone()
            id_estado_reserva = res_estado[0] if res_estado else 1

            cursor.execute("""
                INSERT INTO RESERVAS (id_huesped, id_habitacion, fecha_checkin, fecha_checkout, id_estado, nro_huespedes, monto_adelantado, id_usuario_crea)
                OUTPUT INSERTED.id_reserva
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (id_huesped, id_habitacion, fecha_in, fecha_out, id_estado_reserva, num_huespedes, monto, id_usuario))
            
            row = cursor.fetchone()
            id_reserva = row[0] if row else None

            if id_reserva and lista_extras:
                for ext in lista_extras:
                    cursor.execute("""
                        INSERT INTO CONSUMO_RESERVA (id_reserva, id_producto, cantidad, precio_unitario, subtotal)
                        VALUES (?, ?, ?, ?, ?)
                    """, (id_reserva, ext['id_producto'], ext['cantidad'], ext['precio'], ext['subtotal']))                                                                                                                              
            
            conn.commit()
            return True

        except Exception as e:
            print(f"Error en transacción reserva: {e}")
            conn.rollback()
            return False
        finally:
            conn.autocommit = True
            conn.close()

    def get_reservas_activas(self):
        """REQ-05: Lista reservas Pendiente/Confirmada para modificar o cancelar."""
        conn = self.db.get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT r.id_reserva,
                       hu.nombre + ' ' + hu.apellido AS huesped,
                       hu.nro_documento,
                       h.numero AS habitacion,
                       r.fecha_checkin,
                       r.fecha_checkout,
                       er.nombre AS estado,
                       r.nro_huespedes,
                       r.monto_adelantado
                FROM RESERVAS r
                JOIN HUESPEDES hu ON r.id_huesped = hu.id_huesped
                JOIN HABITACIONES h ON r.id_habitacion = h.id_habitacion
                JOIN CAT_ESTADO_RESERVA er ON r.id_estado = er.id_estado
                WHERE r.id_estado IN (1, 2)  -- Pendiente o Confirmada
                ORDER BY r.fecha_checkin ASC
            """)
            cols = [d[0] for d in cursor.description]
            rows = [dict(zip(cols, row)) for row in cursor.fetchall()]
            conn.close()
            return rows
        except Exception as e:
            print(f"Error al listar reservas: {e}")
            if conn: conn.close()
            return []

    def cancelar_reserva(self, id_reserva):
        """REQ-05: Cancela una reserva (id_estado → 'Cancelada')."""
        conn = self.db.get_connection()
        if not conn:
            return False
        try:
            conn.autocommit = False
            cursor = conn.cursor()
            cursor.execute("""
                SELECT TOP 1 id_estado FROM CAT_ESTADO_RESERVA
                WHERE UPPER(nombre) COLLATE Latin1_General_CI_AI = UPPER('Cancelada')
                   OR id_estado = 3
                ORDER BY
                    CASE WHEN UPPER(nombre) COLLATE Latin1_General_CI_AI = UPPER('Cancelada')
                         THEN 0 ELSE 1 END
            """)
            row = cursor.fetchone()
            if not row:
                raise Exception("Estado 'Cancelada' no existe en BD")
            cursor.execute(
                "UPDATE RESERVAS SET id_estado = ? WHERE id_reserva = ? AND id_estado IN (1,2)",
                (row[0], id_reserva)
            )
            if cursor.rowcount == 0:
                raise Exception("La reserva ya fue procesada y no se puede cancelar.")
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al cancelar reserva: {e}")
            conn.rollback()
            return False
        finally:
            conn.autocommit = True
            conn.close()

    def modificar_reserva(self, id_reserva, nueva_fecha_in, nueva_fecha_out,
                          nro_huespedes, monto_adelantado):
        """REQ-05: Modifica fechas y datos de una reserva Pendiente/Confirmada."""
        conn = self.db.get_connection()
        if not conn:
            return False
        try:
            conn.autocommit = False
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE RESERVAS
                SET fecha_checkin     = ?,
                    fecha_checkout    = ?,
                    nro_huespedes     = ?,
                    monto_adelantado  = ?
                WHERE id_reserva = ? AND id_estado IN (1, 2)
            """, (nueva_fecha_in, nueva_fecha_out,
                  nro_huespedes, monto_adelantado, id_reserva))
            if cursor.rowcount == 0:
                raise Exception("Reserva no encontrada o ya fue cerrada.")
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al modificar reserva: {e}")
            conn.rollback()
            return False
        finally:
            conn.autocommit = True
            conn.close()
