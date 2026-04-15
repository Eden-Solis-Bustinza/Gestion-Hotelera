from src.config.database import db  
import bcrypt

class UserModel:
    def __init__(self):
        self.db = db

    def get_user_by_email(self, email):
        try:
            conn = self.db.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id_usuario, nombre, email, password_hash, id_rol FROM USUARIOS WHERE email = ? AND activo = 1", (email,))
                row = cursor.fetchone()
                conn.close()
                if row:
                    return {
                        "id": row[0],
                        "nombre": row[1],
                        "email": row[2],
                        "password_hash": row[3],
                        "id_rol": row[4]
                    }
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
        return None

    def verify_password(self, password, password_hash):
        try:
            # Si el password_hash esta guardado como string en la BD
            if isinstance(password_hash, str):
                password_hash = password_hash.encode('utf-8')
            return bcrypt.checkpw(password.encode('utf-8'), password_hash)
        except Exception as e:
            print(f"Error al verificar password: {e}")
            return False

    def create_user(self, nombre, email, password, id_rol, id_pregunta, respuesta_seguridad):
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO USUARIOS (nombre, email, password_hash, id_rol, id_pregunta, respuesta_seguridad, activo)
                    VALUES (?, ?, ?, ?, ?, ?, 1)
                """, (nombre, email.strip().lower(), password_hash, id_rol, id_pregunta, respuesta_seguridad.strip().lower()))
                conn.commit()
                conn.close()
                return True
            except Exception as e:
                print(f"Error al crear usuario: {e}")
                conn.rollback()
                conn.close()
        return False

    def get_roles(self):
        conn = self.db.get_connection()
        roles = []
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_rol, nombre FROM CAT_ROL")
            roles = cursor.fetchall()
            conn.close()
        return roles

    def update_password(self, email, id_pregunta, respuesta, new_password):
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                # Verificar respuesta de seguridad
                cursor.execute("""
                    SELECT id_usuario FROM USUARIOS 
                    WHERE email = ? AND id_pregunta = ? AND respuesta_seguridad = ?
                """, (email.strip().lower(), id_pregunta, respuesta.strip().lower()))
                row = cursor.fetchone()
                
                if row:
                    password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    cursor.execute("UPDATE USUARIOS SET password_hash = ? WHERE id_usuario = ?", (password_hash, row[0]))
                    conn.commit()
                    conn.close()
                    return True
                conn.close()
            except Exception as e:
                print(f"Error al recuperar contraseña: {e}")
                conn.rollback()
                conn.close()
        return False

    def get_preguntas_seguridad(self):
        conn = self.db.get_connection()
        preguntas = []
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_pregunta, pregunta FROM SEGURIDAD_PREGUNTAS")
            preguntas = cursor.fetchall()
            conn.close()
        return preguntas

    def update_last_login(self, id_usuario):
        """BUG-05 FIX: Actualiza ultimo_acceso en USUARIOS al hacer login."""
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE USUARIOS SET ultimo_acceso = GETDATE() WHERE id_usuario = ?",
                    (id_usuario,)
                )
                conn.commit()
                conn.close()
            except Exception as e:
                print(f"Error al actualizar ultimo_acceso: {e}")
                if conn: conn.close()
