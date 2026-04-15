import os
import subprocess
from datetime import datetime
from src.config.database import db


class BackupModel:
    def __init__(self):
        self.db = db

    # ------------------------------------------------------------------ #
    #  REQ-14: Backup de la base de datos SQL Server                      #
    # ------------------------------------------------------------------ #
    def ejecutar_backup(self, ruta_destino, id_usuario):
        """
        Ejecuta BACKUP DATABASE HotelDB TO DISK vía pyodbc y registra
        el resultado en la tabla BACKUPS.
        ruta_destino: carpeta donde se guardará el .bak
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"HotelDB_backup_{timestamp}.bak"
        ruta_completa = os.path.join(ruta_destino, nombre_archivo)

        conn = self.db.get_connection()
        if not conn:
            return False, "Sin conexión a la base de datos."

        # Estado inicial: En Proceso (3)
        id_estado = 3
        id_backup = None

        try:
            conn.autocommit = True          # BACKUP no acepta transacciones explícitas
            cursor = conn.cursor()

            # Registrar inicio
            cursor.execute("""
                INSERT INTO BACKUPS (ruta_archivo, id_estado, observaciones, id_usuario)
                OUTPUT INSERTED.id_backup
                VALUES (?, ?, 'En proceso...', ?)
            """, (ruta_completa, id_estado, id_usuario))
            row = cursor.fetchone()
            id_backup = row[0] if row else None

            # Realizar el backup
            cursor.execute(f"""
                BACKUP DATABASE HotelDB
                TO DISK = N'{ruta_completa}'
                WITH FORMAT, MEDIANAME = 'HotelDB_Backup',
                     NAME = 'Backup completo HotelDB'
            """)

            # Actualizar a Exitoso (1)
            if id_backup:
                cursor.execute("""
                    UPDATE BACKUPS SET id_estado = 1,
                        observaciones = 'Backup completado exitosamente.'
                    WHERE id_backup = ?
                """, (id_backup,))

            conn.close()
            return True, ruta_completa

        except Exception as e:
            # Actualizar a Fallido (2)
            try:
                if id_backup:
                    cursor.execute("""
                        UPDATE BACKUPS SET id_estado = 2,
                            observaciones = ?
                        WHERE id_backup = ?
                    """, (str(e)[:290], id_backup))
            except Exception:
                pass
            if conn:
                conn.close()
            return False, str(e)

    def get_historial_backups(self):
        """Devuelve el historial de backups registrados."""
        conn = self.db.get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT TOP 20
                    b.id_backup,
                    b.fecha_hora,
                    b.ruta_archivo,
                    e.nombre AS estado,
                    b.observaciones,
                    u.nombre AS usuario
                FROM BACKUPS b
                JOIN CAT_ESTADO_BACKUP e ON b.id_estado = e.id_estado
                JOIN USUARIOS u ON b.id_usuario = u.id_usuario
                ORDER BY b.fecha_hora DESC
            """)
            rows = cursor.fetchall()
            conn.close()
            return [
                {
                    "id": r[0],
                    "fecha": r[1].strftime("%d/%m/%Y %H:%M:%S") if r[1] else "",
                    "ruta": r[2],
                    "estado": r[3],
                    "observaciones": r[4],
                    "usuario": r[5]
                }
                for r in rows
            ]
        except Exception as e:
            print(f"Error al obtener historial de backups: {e}")
            if conn:
                conn.close()
            return []
