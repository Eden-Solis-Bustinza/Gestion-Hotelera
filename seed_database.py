from src.config.database import db
import bcrypt

def seed_database():
    """
    Inicializa la base de datos con los catálogos críticos y asegura que 
    la estructura mínima para funcionar exista (Roles, Tipos, Usuario Admin).
    También inyecta datos de prueba (Productos y Habitaciones) si no existen.
    
    Retorna True si todo fue exitoso o False si hubo un error irrecuperable.
    """
    conn = db.get_connection()
    if not conn:
        print("[Error] No se pudo establecer conexión con la base de datos para el Seeding.")
        return False
        
    try:
        conn.autocommit = False
        cursor = conn.cursor()
        
                                     
        cursor.execute("SELECT COUNT(*) FROM CAT_ROL")
        if cursor.fetchone()[0] == 0:
            print("🌱 Poblando tabla de Roles (CAT_ROL)...")
            roles = ['Administracion', 'Recepcion', 'Contabilidad']
            for rol in roles:
                cursor.execute("INSERT INTO CAT_ROL (nombre) VALUES (?)", (rol,))

                                                     
        cursor.execute("SELECT COUNT(*) FROM CAT_ESTADO_HABITACION")
        if cursor.fetchone()[0] == 0:
            print("🌱 Poblando Estados de Habitación...")
            estados = ['Disponible', 'Ocupada', 'En Limpieza', 'Mantenimiento']
            for est in estados:
                cursor.execute("INSERT INTO CAT_ESTADO_HABITACION (nombre) VALUES (?)", (est,))

                                                  
        cursor.execute("SELECT COUNT(*) FROM CAT_ESTADO_RESERVA")
        if cursor.fetchone()[0] == 0:
            print("🌱 Poblando Estados de Reserva...")
            estados_res = ['Pendiente', 'Confirmada', 'Cancelada', 'Completada']
            for est in estados_res:
                cursor.execute("INSERT INTO CAT_ESTADO_RESERVA (nombre) VALUES (?)", (est,))

                                              
        cursor.execute("SELECT COUNT(*) FROM TIPO_DOCUMENTO")
        if cursor.fetchone()[0] == 0:
            print("🌱 Poblando Tipos de Documento...")
            docs = ['DNI', 'Pasaporte', 'Carnet Extranjeria']
            for doc in docs:
                cursor.execute("INSERT INTO TIPO_DOCUMENTO (nombre) VALUES (?)", (doc,))

                                                        
        cursor.execute("SELECT COUNT(*) FROM SEGURIDAD_PREGUNTAS")
        if cursor.fetchone()[0] == 0:
            print("🌱 Poblando Preguntas Secretas...")
            preguntas = [
                'Nombre de tu primera mascota', 'Ciudad donde naciste', 
                'Nombre de tu madre', 'Nombre de tu colegio primario', 'Apodo de infancia'
            ]
            for preg in preguntas:
                cursor.execute("INSERT INTO SEGURIDAD_PREGUNTAS (pregunta) VALUES (?)", (preg,))

                                                                          
        cursor.execute("SELECT COUNT(*) FROM USUARIOS")
        if cursor.fetchone()[0] == 0:
            print("🌱 Creando usuario Administrador inicial...")
                                                
            hash_pass = bcrypt.hashpw('admin123'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                                                                         
            cursor.execute("""
                INSERT INTO USUARIOS (nombre, email, password_hash, id_rol, id_pregunta, respuesta_seguridad)
                VALUES ('Administrador Global', 'admin@hotel.com', ?, 1, 1, 'admin')
            """, (hash_pass,))

                                                                     
        cursor.execute("SELECT COUNT(*) FROM CATEGORIA")
        if cursor.fetchone()[0] == 0:
            print("🌱 Insertando categorías de inventario...")
            for cat in ['Aseo Personal', 'Bebidas', 'Snacks', 'Otros Extras']:
                cursor.execute("INSERT INTO CATEGORIA (nombre) VALUES (?)", (cat,))
                
        cursor.execute("SELECT COUNT(*) FROM PRODUCTO")
        if cursor.fetchone()[0] == 0:
            print("🌱 Inyectando catálogo base de Productos Valorado...")
                                                       
            cursor.execute("SELECT id, nombre FROM CATEGORIA")
            categorias_map = {row[1]: row[0] for row in cursor.fetchall()}
            
            productos_mock = [
                (categorias_map.get('Aseo Personal', 1), 'Jabón Tocador 100g', 2.50),
                (categorias_map.get('Aseo Personal', 1), 'Shampoo Botella 500ml', 15.00),
                (categorias_map.get('Snacks', 1),         'Papas Fritas Lays 80g', 3.50),
                (categorias_map.get('Bebidas', 1),        'Agua Mineral 600ml', 2.00),
                (categorias_map.get('Bebidas', 1),        'Cerveza Artesanal 330ml', 8.50)
            ]
            for cat_id, prod_name, prod_precio in productos_mock:
                try:
                    cursor.execute("INSERT INTO PRODUCTO (categoria_id, nombre, precio) VALUES (?, ?, ?)", 
                                   (cat_id, prod_name, prod_precio))
                except Exception as e:
                                                                                                             
                    pass
                    
                                            
        cursor.execute("SELECT COUNT(*) FROM TIPO_HABITACION")
        if cursor.fetchone()[0] == 0:
            print("🌱 Generando tipos de habitación standard...")
            for tipo, desc, tarifa in [('Simple', 'Cama Simple', 80.00), ('Doble', 'Matrimonial', 120.00)]:
                 cursor.execute("INSERT INTO TIPO_HABITACION (nombre, descripcion, tarifa_base) VALUES (?, ?, ?)", (tipo, desc, tarifa))
                 
        cursor.execute("SELECT COUNT(*) FROM HABITACIONES")
        if cursor.fetchone()[0] == 0:
            print("🌱 Generando lista estándar de Habitaciones (Piso 1 y 2)...")
            cursor.execute("SELECT id_tipo, nombre FROM TIPO_HABITACION")
            tipos = {n: _id for _id, n in cursor.fetchall()}
            
            habitaciones_mock = [
                ('101', tipos.get('Simple', 1)), ('102', tipos.get('Simple', 1)), 
                ('201', tipos.get('Doble', 2)), ('202', tipos.get('Doble', 2))
            ]
            for num, tipo_id in habitaciones_mock:
                                                   
                 cursor.execute("INSERT INTO HABITACIONES (numero, id_tipo, id_estado) VALUES (?, ?, 1)", (num, tipo_id))

        conn.commit()
        print("✅ Base de datos inicializada correctamente (Seeding completado).")
        return True
        
    except Exception as e:
        print(f"❌ Ocurrió un error inicializando las configuraciones iniciales de BD: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()
