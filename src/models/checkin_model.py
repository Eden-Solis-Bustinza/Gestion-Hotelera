from src.config.database import db

class CheckinModel:
    def __init__(self):
        self.db = db

    def buscar_huesped_por_dni(self, dni):
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id_huesped, nombre, apellido, telefono 
                    FROM HUESPEDES 
                    WHERE nro_documento = ?
                """, (dni,))
                row = cursor.fetchone()
                conn.close()
                if row:
                    return {"id": row[0], "nombres": f"{row[1]} {row[2]}", "contacto": row[3]}
            except Exception as e:
                print(f"Error al buscar huésped: {e}")
                if conn: conn.close()
        return None

    def get_habitaciones_disponibles(self):
        """REQ-02/06: Solo trae habitaciones con estado 1 (Disponible)"""
        conn = self.db.get_connection()
        habitaciones = []
        if conn:
            try:
                cursor = conn.cursor()
                # CORRECCIÓN CRÍTICA: La tabla correcta es TIPO_HABITACION
                cursor.execute("""
                    SELECT h.id_habitacion, h.numero, th.nombre 
                    FROM HABITACIONES h
                    JOIN TIPO_HABITACION th ON h.id_tipo = th.id_tipo
                    WHERE h.id_estado = 1 
                """)
                habitaciones = cursor.fetchall()
                conn.close()
            except Exception as e:
                print(f"Error al obtener habitaciones: {e}")
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

    def registrar_checkin_directo(self, id_huesped, id_habitacion, num_huespedes, fecha_in, fecha_out, monto, id_metodo, id_usuario):
        conn = self.db.get_connection()
        if not conn: return False
        
        try:
            conn.autocommit = False 
            cursor = conn.cursor()

            # 1. Obtener id_estado 'Confirmada' de forma robusta:
            #    Primero por id (posición fija en el catálogo del schema v3:
            #    1=Pendiente, 2=Confirmada, 3=Cancelada, 4=Completada)
            #    Si alguien re-sembró la BD con otro orden, el COLLATE lo resuelve.
            cursor.execute("""
                SELECT TOP 1 id_estado
                FROM CAT_ESTADO_RESERVA
                WHERE UPPER(nombre) COLLATE Latin1_General_CI_AI = UPPER('Confirmada')
                   OR id_estado = 2
                ORDER BY
                    CASE WHEN UPPER(nombre) COLLATE Latin1_General_CI_AI = UPPER('Confirmada')
                         THEN 0 ELSE 1 END
            """)
            row_estado = cursor.fetchone()
            if not row_estado:
                # Último recurso: usar id=2 que es 'Confirmada' según hotel_schema_v3.sql
                id_estado_confirmada = 2
                print("[WARN] Usando id_estado=2 (Confirmada) por fallback.")
            else:
                id_estado_confirmada = row_estado[0]

            # 2. Insertar la reserva con el ID dinámico
            cursor.execute("""
                INSERT INTO RESERVAS (id_huesped, id_habitacion, fecha_checkin, fecha_checkout, id_estado, nro_huespedes, monto_adelantado, id_usuario_crea)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (id_huesped, id_habitacion, fecha_in, fecha_out, id_estado_confirmada, num_huespedes, monto, id_usuario))

            # 3. Actualizar la habitación a Ocupada (Estado 2 habitualmente)
            # Buscamos el ID real de "Ocupada" para estar 100% seguros
            # 3. Actualizar habitación a Ocupada
            cursor.execute("""
                SELECT TOP 1 id_estado FROM CAT_ESTADO_HABITACION
                WHERE UPPER(nombre) COLLATE Latin1_General_CI_AI = UPPER('Ocupada')
                   OR id_estado = 2
                ORDER BY
                    CASE WHEN UPPER(nombre) COLLATE Latin1_General_CI_AI = UPPER('Ocupada')
                         THEN 0 ELSE 1 END
            """)
            row_ocupada = cursor.fetchone()
            id_estado_ocupada = row_ocupada[0] if row_ocupada else 2  # 2=Ocupada en schema v3

            cursor.execute("""
                UPDATE HABITACIONES 
                SET id_estado = ? 
                WHERE id_habitacion = ? AND id_estado = 1
            """, (id_estado_ocupada, id_habitacion))

            if cursor.rowcount == 0:
                raise Exception("La habitación ya no está disponible.")

            conn.commit()
            return True

        except Exception as e:
            print(f"ROLLBACK EJECUTADO. Error en transacción: {e}")
            conn.rollback()
            return False
        finally:
            conn.autocommit = True
            conn.close()