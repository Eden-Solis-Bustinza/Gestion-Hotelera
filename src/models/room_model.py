from src.config.database import db


class RoomModel:
    def __init__(self):
        self.db = db

    def get_all_rooms(self):
        conn = self.db.get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT h.id_habitacion, h.numero, th.nombre AS tipo,
                       eh.nombre AS estado, eh.id_estado,
                       th.tarifa_base, h.observaciones
                FROM HABITACIONES h
                JOIN TIPO_HABITACION       th ON h.id_tipo   = th.id_tipo
                JOIN CAT_ESTADO_HABITACION eh ON h.id_estado = eh.id_estado
                ORDER BY h.numero
            """)
            columns = [c[0] for c in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            conn.close()
            return results
        except Exception as e:
            print(f"Error al obtener habitaciones: {e}")
            if conn:
                conn.close()
            return []

    def get_tipos_habitacion(self):
        conn = self.db.get_connection()
        tipos = []
        if not conn:
            return tipos
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id_tipo, nombre, tarifa_base FROM TIPO_HABITACION WHERE activo = 1")
            tipos = cursor.fetchall()
            conn.close()
        except Exception as e:
            print(f"Error al obtener tipos: {e}")
            if conn:
                conn.close()
        return tipos

    def get_estados_habitacion(self):
        conn = self.db.get_connection()
        estados = []
        if not conn:
            return estados
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id_estado, nombre FROM CAT_ESTADO_HABITACION")
            estados = cursor.fetchall()
            conn.close()
        except Exception as e:
            if conn:
                conn.close()
        return estados

    def update_room_status(self, room_id, status_id):
        """Actualiza el estado de una habitación."""
        conn = self.db.get_connection()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE HABITACIONES SET id_estado = ? WHERE id_habitacion = ?",
                (status_id, room_id)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error al actualizar estado: {e}")
            if conn:
                conn.rollback()
                conn.close()
            return False

    def crear_habitacion(self, numero, id_tipo, observaciones=""):
        """REQ-02: Registra una nueva habitación con estado Disponible (1)."""
        conn = self.db.get_connection()
        if not conn:
            return False, "Sin conexión a la base de datos."
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO HABITACIONES (numero, id_tipo, id_estado, observaciones)
                VALUES (?, ?, 1, ?)
            """, (numero.strip(), id_tipo, observaciones.strip()))
            conn.commit()
            conn.close()
            return True, "Habitación creada exitosamente."
        except Exception as e:
            msg = str(e)
            if "UNIQUE" in msg or "duplicate" in msg.lower():
                msg = f"Ya existe una habitación con el número '{numero}'."
            if conn:
                conn.rollback()
                conn.close()
            return False, msg