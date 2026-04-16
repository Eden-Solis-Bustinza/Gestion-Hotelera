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

    def get_all_users(self):
        conn = self.db.get_connection()
        users = []
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT u.id_usuario, u.nombre, u.email, r.nombre AS rol_nombre, u.id_rol, u.activo
                    FROM USUARIOS u
                    JOIN CAT_ROL r ON u.id_rol = r.id_rol
                    ORDER BY u.id_usuario
                """)
                for row in cursor.fetchall():
                    users.append({
                        "id": row[0],
                        "nombre": row[1],
                        "email": row[2],
                        "rol": row[3],
                        "id_rol": row[4],
                        "activo": bool(row[5])
                    })
                conn.close()
            except Exception as e:
                print(f"Error al obtener todos los usuarios: {e}")
                if conn: conn.close()
        return users

    def toggle_user_status(self, id_usuario, new_status):
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                val = 1 if new_status else 0
                cursor.execute("UPDATE USUARIOS SET activo = ? WHERE id_usuario = ?", (val, id_usuario))
                conn.commit()
                conn.close()
                return True
            except Exception as e:
                print(f"Error al actualizar estado del usuario: {e}")
                conn.rollback()
                if conn: conn.close()
        return False

    def update_user_details_admin(self, id_usuario, nombre, email, id_rol, new_password=None):
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                if new_password:
                    password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    cursor.execute("""
                        UPDATE USUARIOS 
                        SET nombre = ?, email = ?, id_rol = ?, password_hash = ?
                        WHERE id_usuario = ?
                    """, (nombre, email.strip().lower(), id_rol, password_hash, id_usuario))
                else:
                    cursor.execute("""
                        UPDATE USUARIOS 
                        SET nombre = ?, email = ?, id_rol = ?
                        WHERE id_usuario = ?
                    """, (nombre, email.strip().lower(), id_rol, id_usuario))
                conn.commit()
                conn.close()
                return True
            except Exception as e:
                print(f"Error al actualizar usuario (admin): {e}")
                conn.rollback()
                if conn: conn.close()
        return False
