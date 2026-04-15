from src.config.database import db
from src.models.user_model import UserModel
import bcrypt                                                      

def seed_database():
    print("--- Verificando base de datos y datos iniciales ---")
    conn = db.get_connection()
    if not conn:
        print("Error: No se pudo conectar a la base de datos.")
        return False
    
    try:
        cursor = conn.cursor()
        
                                       
        cursor.execute("SELECT COUNT(*) FROM CAT_ROL")
        if cursor.fetchone()[0] == 0:
            print("Insertando roles predeterminados...")
            cursor.execute("INSERT INTO CAT_ROL (nombre) VALUES ('Administracion'), ('Recepcion'), ('Contabilidad')")
            conn.commit()

                                           
        cursor.execute("SELECT COUNT(*) FROM SEGURIDAD_PREGUNTAS")
        if cursor.fetchone()[0] == 0:
            print("Insertando preguntas de seguridad...")
            cursor.execute("INSERT INTO SEGURIDAD_PREGUNTAS (pregunta) VALUES ('Nombre de tu primera mascota'), ('Ciudad donde naciste')")
            conn.commit()

                                            
        cursor.execute("SELECT COUNT(*) FROM TIPO_DOCUMENTO")
        if cursor.fetchone()[0] == 0:
            print("Insertando tipos de documento...")
            cursor.execute("INSERT INTO TIPO_DOCUMENTO (nombre) VALUES ('DNI'), ('Pasaporte'), ('Carnet Extranjeria')")
            conn.commit()

                                            
        cursor.execute("SELECT COUNT(*) FROM USUARIOS")
        if cursor.fetchone()[0] == 0:
            print("No se encontraron usuarios. Creando usuario administrador...")
            
                                                                                 
            cursor.execute("SELECT id_rol FROM CAT_ROL WHERE nombre = 'Administracion'")
            rol_row = cursor.fetchone()
            if not rol_row:
                print("Error crítico: No se encontró el rol 'Administracion'.")
                return False
            id_rol_admin = rol_row[0]

                                                        
            cursor.execute("SELECT id_pregunta FROM SEGURIDAD_PREGUNTAS WHERE pregunta = 'Nombre de tu primera mascota'")
            pregunta_row = cursor.fetchone()
            if not pregunta_row:
                print("Error crítico: No se encontró la pregunta de seguridad inicial.")
                return False
            id_pregunta_inicial = pregunta_row[0]

                                                         
            user_model = UserModel()
            user_model.create_user(
                nombre="Administrador",
                email="admin@hotel.com",
                password="admin",                              
                id_rol=id_rol_admin,
                id_pregunta=id_pregunta_inicial,
                respuesta_seguridad="admin"                              
            )
            print("Usuario 'admin@hotel.com' creado correctamente.")
        else:
            print("Ya existen usuarios en la base de datos.")
            
        print("--- Inicialización completada con éxito ---")
        return True
        
    except Exception as e:
        print(f"Error crítico durante el seeding: {e}")
                                                                                                     
                          
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()