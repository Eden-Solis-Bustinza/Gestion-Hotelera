from src.config.database import db
from datetime import datetime, timedelta


class NotificacionModel:
    def __init__(self):
        self.db = db

    # ------------------------------------------------------------------ #
    #  Generación automática de notificaciones en BD                      #
    # ------------------------------------------------------------------ #
    def generar_notificaciones(self):
        """
        REQ-07: Genera (INSERT) notificaciones en la tabla NOTIFICACIONES
        basándose en el estado actual de reservas y habitaciones.
        Se llama al abrir el panel para que siempre esté fresca.
        """
        conn = self.db.get_connection()
        if not conn:
            return

        try:
            conn.autocommit = False
            cursor = conn.cursor()

            # 1. Reservas que vencen en las próximas 24 horas (CheckoutProximo)
            cursor.execute("""
                SELECT r.id_reserva,
                       hu.nombre + ' ' + hu.apellido AS huesped,
                       h.numero,
                       r.fecha_checkout
                FROM RESERVAS r
                JOIN HUESPEDES     hu ON r.id_huesped    = hu.id_huesped
                JOIN HABITACIONES   h ON r.id_habitacion = h.id_habitacion
                WHERE r.id_estado IN (1, 2)
                  AND r.fecha_checkout BETWEEN GETDATE() AND DATEADD(HOUR, 24, GETDATE())
            """)
            for row in cursor.fetchall():
                id_res, huesped, num_hab, f_out = row
                msg = (f"Check-out próximo: Hab {num_hab} | "
                       f"{huesped} | Salida: {f_out.strftime('%d/%m %H:%M')}")
                cursor.execute("""
                    INSERT INTO NOTIFICACIONES (id_tipo, mensaje)
                    SELECT t.id_tipo, ?
                    FROM CAT_TIPO_NOTIFICACION t
                    WHERE t.nombre = 'CheckoutPendiente'
                      AND NOT EXISTS (
                          SELECT 1 FROM NOTIFICACIONES n2
                          JOIN CAT_TIPO_NOTIFICACION t2 ON n2.id_tipo = t2.id_tipo
                          WHERE t2.nombre = 'CheckoutPendiente'
                            AND n2.mensaje = ?
                            AND n2.created_at >= CAST(GETDATE() AS DATE)
                      )
                """, (msg, msg))

            # 2. Reservas que inician en las próximas 2 horas (ReservaProxima)
            cursor.execute("""
                SELECT r.id_reserva,
                       hu.nombre + ' ' + hu.apellido AS huesped,
                       h.numero,
                       r.fecha_checkin
                FROM RESERVAS r
                JOIN HUESPEDES hu ON r.id_huesped = hu.id_huesped
                JOIN HABITACIONES h ON r.id_habitacion = h.id_habitacion
                WHERE r.id_estado IN (1, 2)
                  AND r.fecha_checkin BETWEEN GETDATE() AND DATEADD(HOUR, 2, GETDATE())
            """)
            for row in cursor.fetchall():
                id_res, huesped, num_hab, f_in = row
                msg = (f"Reserva inminente: Hab {num_hab} | "
                       f"{huesped} | Llegada: {f_in.strftime('%d/%m %H:%M')}")
                cursor.execute("""
                    INSERT INTO NOTIFICACIONES (id_tipo, mensaje)
                    SELECT t.id_tipo, ?
                    FROM CAT_TIPO_NOTIFICACION t
                    WHERE t.nombre = 'ReservaProxima'
                      AND NOT EXISTS (
                          SELECT 1 FROM NOTIFICACIONES n2
                          JOIN CAT_TIPO_NOTIFICACION t2 ON n2.id_tipo = t2.id_tipo
                          WHERE t2.nombre = 'ReservaProxima'
                            AND n2.mensaje = ?
                            AND n2.created_at >= CAST(GETDATE() AS DATE)
                      )
                """, (msg, msg))

            # 3. Habitaciones en limpieza (HabitacionLimpia)
            cursor.execute("""
                SELECT h.id_habitacion, h.numero
                FROM HABITACIONES h
                JOIN CAT_ESTADO_HABITACION e ON h.id_estado = e.id_estado
                WHERE e.nombre = 'En Limpieza'
            """)
            for row in cursor.fetchall():
                id_hab, num_hab = row
                msg = f"Habitación {num_hab} terminó limpieza — lista para disponibilidad."
                cursor.execute("""
                    INSERT INTO NOTIFICACIONES (id_tipo, mensaje)
                    SELECT t.id_tipo, ?
                    FROM CAT_TIPO_NOTIFICACION t
                    WHERE t.nombre = 'HabitacionLimpia'
                      AND NOT EXISTS (
                          SELECT 1 FROM NOTIFICACIONES n2
                          JOIN CAT_TIPO_NOTIFICACION t2 ON n2.id_tipo = t2.id_tipo
                          WHERE t2.nombre = 'HabitacionLimpia'
                            AND n2.mensaje = ?
                            AND n2.created_at >= CAST(GETDATE() AS DATE)
                      )
                """, (msg, msg))

            conn.commit()
        except Exception as e:
            print(f"Error al generar notificaciones: {e}")
            conn.rollback()
        finally:
            conn.autocommit = True
            conn.close()

    # ------------------------------------------------------------------ #
    #  Lectura de las últimas notificaciones                              #
    # ------------------------------------------------------------------ #
    def get_notificaciones(self, limit=50):
        """Devuelve las últimas N notificaciones ordenadas por fecha desc."""
        conn = self.db.get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT TOP (?)
                    n.id_notificacion,
                    t.nombre   AS tipo,
                    n.mensaje,
                    n.created_at
                FROM NOTIFICACIONES n
                JOIN CAT_TIPO_NOTIFICACION t ON n.id_tipo = t.id_tipo
                ORDER BY n.created_at DESC
            """, (limit,))
            rows = cursor.fetchall()
            conn.close()
            return [
                {
                    "id": r[0],
                    "tipo": r[1],
                    "mensaje": r[2],
                    "fecha": r[3].strftime("%d/%m/%Y %H:%M") if r[3] else ""
                }
                for r in rows
            ]
        except Exception as e:
            print(f"Error al obtener notificaciones: {e}")
            if conn:
                conn.close()
            return []

    def contar_notificaciones_hoy(self):
        """Cuenta notificaciones generadas hoy (para badge en Dashboard)."""
        conn = self.db.get_connection()
        if not conn:
            return 0
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT COUNT(*) FROM NOTIFICACIONES
                WHERE created_at >= CAST(GETDATE() AS DATE)
            """)
            row = cursor.fetchone()
            conn.close()
            return row[0] if row else 0
        except Exception as e:
            if conn:
                conn.close()
            return 0
