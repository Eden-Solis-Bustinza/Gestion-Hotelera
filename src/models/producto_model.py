from src.config.database import db


class ProductoModel:
    def __init__(self):
        self.db = db

    # ------------------------------------------------------------------ #
    #  Catálogos                                                          #
    # ------------------------------------------------------------------ #
    def get_categorias(self):
        conn = self.db.get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre FROM CATEGORIA ORDER BY nombre")
            res = cursor.fetchall()
            conn.close()
            return res
        except Exception as e:
            print(f"Error al obtener categorías: {e}")
            if conn:
                conn.close()
            return []

    def get_productos_by_categoria(self, categoria_id):
        conn = self.db.get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, nombre FROM PRODUCTO WHERE categoria_id = ? ORDER BY nombre",
                (categoria_id,)
            )
            res = cursor.fetchall()
            conn.close()
            return res
        except Exception as e:
            print(f"Error al obtener productos: {e}")
            if conn:
                conn.close()
            return []

    # ------------------------------------------------------------------ #
    #  Stock disponible (saldo de entradas - salidas)                     #
    # ------------------------------------------------------------------ #
    def get_stock_producto(self, id_producto):
        """Calcula stock actual = SUM(entradas) - SUM(salidas)."""
        conn = self.db.get_connection()
        if not conn:
            return 0
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT
                    ISNULL(SUM(CASE WHEN tipo = 'entrada' THEN cantidad ELSE 0 END), 0)
                  - ISNULL(SUM(CASE WHEN tipo = 'salida'  THEN cantidad ELSE 0 END), 0)
                    AS stock
                FROM MOVIMIENTO_INVENTARIO
                WHERE producto_id = ?
            """, (id_producto,))
            row = cursor.fetchone()
            conn.close()
            return int(row[0]) if row else 0
        except Exception as e:
            print(f"Error al calcular stock: {e}")
            if conn:
                conn.close()
            return 0

    # ------------------------------------------------------------------ #
    #  Habitaciones ocupadas (para el combo "Nro. Habitación")            #
    # ------------------------------------------------------------------ #
    def get_habitaciones_ocupadas(self):
        """Devuelve habitaciones con estado 'Ocupada' para cargar consumos."""
        conn = self.db.get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT h.id_habitacion, h.numero,
                       r.id_reserva
                FROM HABITACIONES h
                JOIN CAT_ESTADO_HABITACION e ON h.id_estado = e.id_estado
                LEFT JOIN RESERVAS r ON r.id_habitacion = h.id_habitacion
                    AND r.id_estado IN (
                        SELECT id_estado FROM CAT_ESTADO_RESERVA WHERE nombre IN ('Confirmada', 'Pendiente')
                    )
                WHERE e.nombre = 'Ocupada'
            """)
            rows = cursor.fetchall()
            conn.close()
            return rows  # (id_habitacion, numero, id_reserva)
        except Exception as e:
            print(f"Error al obtener habitaciones ocupadas: {e}")
            if conn:
                conn.close()
            return []

    # ------------------------------------------------------------------ #
    #  Movimientos                                                        #
    # ------------------------------------------------------------------ #
    def agregar_stock_entrada(self, id_producto, cantidad, id_usuario):
        """REQ-08: Reabastecimiento → movimiento 'entrada'."""
        return self._crear_movimiento(id_producto, cantidad, "entrada", id_usuario, None)

    def registrar_venta(self, id_producto, cantidad, id_usuario, id_comprobante=None):
        """REQ-08: Venta/consumo → movimiento 'salida'."""
        # Verificar stock disponible
        stock = self.get_stock_producto(id_producto)
        if stock < cantidad:
            return False, f"Stock insuficiente. Disponible: {stock}"
        ok = self._crear_movimiento(id_producto, cantidad, "salida", id_usuario, id_comprobante)
        return (True, "OK") if ok else (False, "Error al registrar salida")

    def _crear_movimiento(self, id_producto, cantidad, tipo, id_usuario, id_comprobante):
        conn = self.db.get_connection()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO MOVIMIENTO_INVENTARIO
                    (producto_id, cantidad, tipo, id_usuario, id_comprobante)
                VALUES (?, ?, ?, ?, ?)
            """, (id_producto, cantidad, tipo, id_usuario, id_comprobante))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error al registrar movimiento: {e}")
            if conn:
                conn.rollback()
                conn.close()
            return False

    def crear_producto(self, nombre, id_categoria, id_usuario):
        """Registra un nuevo producto en catálogo."""
        conn = self.db.get_connection()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO PRODUCTO (nombre, categoria_id) VALUES (?, ?)",
                (nombre.strip(), id_categoria)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error al crear producto: {e}")
            if conn:
                conn.rollback()
                conn.close()
            return False
