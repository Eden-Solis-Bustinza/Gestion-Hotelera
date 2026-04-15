from src.config.database import db


class ReporteModel:
    def __init__(self):
        self.db = db

                                                                          
                                                                           
                                                                          
    def get_reporte_ingresos(self, fecha_desde, fecha_hasta):
        """
        Usa la vista VW_REPORTE_BASE para obtener el detalle de facturas
        en un rango de fechas.
        """
        conn = self.db.get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT
                    numero_comprobante,
                    huesped,
                    habitacion,
                    tipo,
                    dias_estancia,
                    subtotal,
                    total_general,
                    metodo_pago,
                    fecha_pago
                FROM dbo.VW_REPORTE_BASE
                WHERE fecha_pago BETWEEN ? AND ?
                ORDER BY fecha_pago DESC
            """, (fecha_desde, fecha_hasta))
            columns = [d[0] for d in cursor.description]
            rows = cursor.fetchall()
            conn.close()
            return [dict(zip(columns, r)) for r in rows]
        except Exception as e:
            print(f"Error en reporte de ingresos: {e}")
            if conn:
                conn.close()
            return []

    def get_resumen_ingresos(self, fecha_desde, fecha_hasta):
        """
        Resumen agregado: total de ventas, monto total y habitaciones únicas
        en el período.
        """
        conn = self.db.get_connection()
        if not conn:
            return {}
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT
                    COUNT(*)                         AS cantidad_comprobantes,
                    ISNULL(SUM(total_general), 0)    AS total_ingresos,
                    ISNULL(AVG(total_general), 0)    AS promedio_por_estancia,
                    ISNULL(SUM(dias_estancia), 0)    AS total_noches
                FROM dbo.VW_REPORTE_BASE
                WHERE fecha_pago BETWEEN ? AND ?
            """, (fecha_desde, fecha_hasta))
            row = cursor.fetchone()
            conn.close()
            if row:
                return {
                    "cantidad": row[0],
                    "total_ingresos": float(row[1]),
                    "promedio": float(row[2]),
                    "total_noches": row[3]
                }
            return {}
        except Exception as e:
            print(f"Error en resumen de ingresos: {e}")
            if conn:
                conn.close()
            return {}

    def get_ocupacion_por_tipo(self, fecha_desde, fecha_hasta):
        """Cuenta rooms por tipo facturadas en el período."""
        conn = self.db.get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT
                    tipo,
                    COUNT(*)               AS cantidad,
                    SUM(total_general)     AS ingresos
                FROM dbo.VW_REPORTE_BASE
                WHERE fecha_pago BETWEEN ? AND ?
                GROUP BY tipo
                ORDER BY ingresos DESC
            """, (fecha_desde, fecha_hasta))
            rows = cursor.fetchall()
            conn.close()
            return [{"tipo": r[0], "cantidad": r[1], "ingresos": float(r[2])} for r in rows]
        except Exception as e:
            print(f"Error en ocupación por tipo: {e}")
            if conn:
                conn.close()
            return []

    def get_metodos_pago_stats(self, fecha_desde, fecha_hasta):
        """Distribución de métodos de pago en el período."""
        conn = self.db.get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT
                    metodo_pago,
                    COUNT(*)            AS cantidad,
                    SUM(total_general)  AS monto
                FROM dbo.VW_REPORTE_BASE
                WHERE fecha_pago BETWEEN ? AND ?
                GROUP BY metodo_pago
                ORDER BY monto DESC
            """, (fecha_desde, fecha_hasta))
            rows = cursor.fetchall()
            conn.close()
            return [{"metodo": r[0], "cantidad": r[1], "monto": float(r[2])} for r in rows]
        except Exception as e:
            if conn:
                conn.close()
            return []
