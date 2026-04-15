from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QHeaderView, QTableWidgetItem
from src.views.FrmProductos import Ui_Dialog
from src.models.producto_model import ProductoModel


class ProductosController:
    def __init__(self, user_data):
        self.window = QtWidgets.QDialog()
        self.view = Ui_Dialog()
        self.view.setupUi(self.window)

        self.user_data = user_data
        self.model = ProductoModel()

        self.window.setWindowState(QtCore.Qt.WindowMaximized)

        self.setup_ui()
        self.load_datos_iniciales()
        self.setup_connections()

    def show(self):
        self.window.exec_()

    # ------------------------------------------------------------------ #
    #  Setup                                                              #
    # ------------------------------------------------------------------ #
    def setup_ui(self):
        # Tabla de carrito de venta
        self.view.TW_productos.setColumnCount(3)
        self.view.TW_productos.setRowCount(0)
        self.view.TW_productos.setHorizontalHeaderLabels(["Producto", "Cantidad", "Subtotal"])
        self.view.TW_productos.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.view.TW_productos.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # Spinbox por defecto en 1
        self.view.SB_cantidad.setMinimum(1)
        self.view.SB_cantidad.setValue(1)

        # Radio buttons — por defecto "Inmediato"
        self.view.RB_inmediato.setChecked(True)

        # Limpiar totales
        self.view.LE_subtotal.setReadOnly(True)
        self.view.LE_igv.setReadOnly(True)
        self.view.LE_total.setReadOnly(True)
        self.view.LE_subtotal.setText("0.00")
        self.view.LE_igv.setText("0.00")
        self.view.LE_total.setText("0.00")

        # Inventario: LE_cantidad muestra stock actual (solo lectura)
        self.view.LE_cantidad.setReadOnly(True)
        self.view.LE_cantidad.setPlaceholderText("Stock disponible")

    def load_datos_iniciales(self):
        # ── Categorías para INVENTARIO (CB_categoria)
        categorias = self.model.get_categorias()
        self.view.CB_categoria.clear()
        self.view.CB_categoria_2.clear()
        for c in categorias:
            self.view.CB_categoria.addItem(c[1], c[0])
            self.view.CB_categoria_2.addItem(c[1], c[0])

        # ── Habitaciones ocupadas para el combo CB_numero_h
        self.view.CB_numero_h.clear()
        hab_ocupadas = self.model.get_habitaciones_ocupadas()
        if hab_ocupadas:
            for id_hab, numero, id_res in hab_ocupadas:
                self.view.CB_numero_h.addItem(f"Hab. {numero}", (id_hab, id_res))
        else:
            self.view.CB_numero_h.addItem("Sin ocupadas")

        # Cargar productos de la primera categoría
        if self.view.CB_categoria.count() > 0:
            self._cargar_productos(self.view.CB_categoria, self.view.CB_producto)
            self._cargar_productos(self.view.CB_categoria_2, self.view.CB_producto_v)

    def setup_connections(self):
        # Inventario: al cambiar categoría → cargar productos e inventario
        self.view.CB_categoria.currentIndexChanged.connect(
            lambda: self._on_categoria_inv_changed()
        )
        # Venta: al cambiar categorías de venta
        self.view.CB_categoria_2.currentIndexChanged.connect(
            lambda: self._cargar_productos(self.view.CB_categoria_2, self.view.CB_producto_v)
        )

        # Botones
        self.view.PB_cargar.clicked.connect(self.agregar_stock)   # Reabastecimiento
        self.view.PB_pagar.clicked.connect(self.realizar_venta)   # Venta/consumo

    # ------------------------------------------------------------------ #
    #  Carga de combos                                                    #
    # ------------------------------------------------------------------ #
    def _cargar_productos(self, cb_cat, cb_prod):
        id_cat = cb_cat.currentData()
        cb_prod.clear()
        if id_cat:
            prods = self.model.get_productos_by_categoria(id_cat)
            for p in prods:
                cb_prod.addItem(p[1], p[0])

    def _on_categoria_inv_changed(self):
        self._cargar_productos(self.view.CB_categoria, self.view.CB_producto)
        self._actualizar_stock()

    def _actualizar_stock(self):
        id_prod = self.view.CB_producto.currentData()
        if id_prod:
            stock = self.model.get_stock_producto(id_prod)
            self.view.LE_cantidad.setText(str(stock))
        else:
            self.view.LE_cantidad.clear()

    # ------------------------------------------------------------------ #
    #  Reabastecimiento (GB_agregar_p → PB_cargar)  REQ-08               #
    # ------------------------------------------------------------------ #
    def agregar_stock(self):
        # Producto del panel Agregar
        nombre_nuevo = self.view.LE_producto.text().strip()
        id_categoria = self.view.CB_categoria_2.currentData()
        cantidad_txt = self.view.LE_cantidad_2.text().strip()

        if not cantidad_txt.isdigit() or int(cantidad_txt) <= 0:
            QMessageBox.warning(self.window, "Error", "Ingrese una cantidad válida (número > 0).")
            return

        cantidad = int(cantidad_txt)

        # Caso A: Nombre nuevo → crear producto y dar entrada
        if nombre_nuevo:
            if not id_categoria:
                QMessageBox.warning(self.window, "Error", "Seleccione una categoría.")
                return
            id_usuario = self.user_data.get('id', 1)
            ok = self.model.crear_producto(nombre_nuevo, id_categoria, id_usuario)
            if not ok:
                QMessageBox.critical(self.window, "Error",
                                     "No se pudo crear el producto (¿nombre duplicado?).")
                return
            # Recargar combo y obtener id del nuevo producto
            self._cargar_productos(self.view.CB_categoria_2, self.view.CB_producto_v)
            QMessageBox.information(self.window, "Creado",
                                    f"Producto '{nombre_nuevo}' creado.")
            self.view.LE_producto.clear()
            # Dar entrada de stock al recién creado
            prods = self.model.get_productos_by_categoria(id_categoria)
            id_prod_nuevo = next((p[0] for p in prods if p[1].lower() == nombre_nuevo.lower()), None)
            if id_prod_nuevo:
                self.model.agregar_stock_entrada(id_prod_nuevo, cantidad, id_usuario)
        else:
            # Caso B: Producto existente del panel inventario
            id_prod = self.view.CB_producto.currentData()
            if not id_prod:
                QMessageBox.warning(self.window, "Error", "Seleccione un producto del inventario.")
                return
            id_usuario = self.user_data.get('id', 1)
            ok = self.model.agregar_stock_entrada(id_prod, cantidad, id_usuario)
            if ok:
                self._actualizar_stock()
                QMessageBox.information(self.window, "✅ Stock actualizado",
                                        f"Se agregaron {cantidad} unidades al inventario.")
            else:
                QMessageBox.critical(self.window, "Error", "No se pudo registrar la entrada.")

        self.view.LE_cantidad_2.clear()

    # ------------------------------------------------------------------ #
    #  Venta / Consumo (GB_venta_p → PB_pagar)  REQ-08                  #
    # ------------------------------------------------------------------ #
    def realizar_venta(self):
        id_prod = self.view.CB_producto_v.currentData()
        if not id_prod:
            QMessageBox.warning(self.window, "Error", "Seleccione un producto para vender.")
            return

        cantidad = self.view.SB_cantidad.value()
        if cantidad <= 0:
            QMessageBox.warning(self.window, "Error", "La cantidad debe ser > 0.")
            return

        id_usuario = self.user_data.get('id', 1)

        # Verificar si hay habitación seleccionada
        hab_data = self.view.CB_numero_h.currentData()
        id_comprobante = None  # las ventas directas no vinculan comprobante aún

        exito, msg = self.model.registrar_venta(id_prod, cantidad, id_usuario, id_comprobante)

        if exito:
            nombre_prod = self.view.CB_producto_v.currentText()

            # Agregar fila al carrito visual
            row = self.view.TW_productos.rowCount()
            self.view.TW_productos.insertRow(row)
            self.view.TW_productos.setItem(row, 0, QTableWidgetItem(nombre_prod))
            self.view.TW_productos.setItem(row, 1, QTableWidgetItem(str(cantidad)))
            self.view.TW_productos.setItem(row, 2, QTableWidgetItem("—"))  # precio sin tarifa en modelo

            self._actualizar_totales_venta()
            self._actualizar_stock()
            QMessageBox.information(self.window, "✅ Venta registrada",
                                    f"{cantidad} x {nombre_prod} registrado correctamente.")
        else:
            QMessageBox.critical(self.window, "❌ Error", msg)

    def _actualizar_totales_venta(self):
        """Calcula subtotal, IGV y total del carrito."""
        # Sin precio unitario en el modelo actual, mostramos solo conteo
        filas = self.view.TW_productos.rowCount()
        self.view.LE_subtotal.setText(f"{filas} ítem(s)")
        self.view.LE_igv.setText("18% incluido")
        self.view.LE_total.setText("Ver checkout")
