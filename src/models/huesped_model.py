from src.config.database import db

class HuespedModel:
    def __init__(self):
        self.db = db

    def get_tipos_documento(self):
        conn = self.db.get_connection()
        tipos = []
        if conn:
            cursor = conn.cursor()
            # Falla corregida: La columna real es id_tipo_documento
            cursor.execute("SELECT id_tipo_documento, nombre FROM TIPO_DOCUMENTO")
            tipos = cursor.fetchall()
            conn.close()
        return tipos

    def create_huesped(self, id_tipo_doc, numero_doc, nombres, apellidos, contacto, email, fecha_nacimiento):
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                # Fallas corregidas: Se reemplazó id_tipo_doc, numero_documento, nombres, apellidos, contacto
                # por las columnas reales de tu tabla HUESPEDES
                cursor.execute("""
                    INSERT INTO HUESPEDES (id_tipo_documento, nro_documento, nombre, apellido, telefono, email, fecha_nacimiento)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (id_tipo_doc, numero_doc, nombres, apellidos, contacto, email, fecha_nacimiento))
                conn.commit()
                conn.close()
                return True
            except Exception as e:
                print(f"Error crítico en BD al registrar huésped: {e}")
                if conn:
                    conn.rollback()
                    conn.close()
        return False