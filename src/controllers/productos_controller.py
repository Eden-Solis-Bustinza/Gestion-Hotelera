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

                                                                          
                                                                           
                                                                          
    def setup_ui(self):
                                   
        self.view.TW_productos.setColumnCount(3)
        self.view.TW_productos.setRowCount(0)
        self.view.TW_productos.setHorizontalHeaderLabels(["Producto", "Cantidad", "Subtotal"])
        self.view.TW_productos.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.view.TW_productos.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

                                  
        self.view.SB_cantidad.setMinimum(1)
        self.view.SB_cantidad.setValue(1)

                                                 
        self.view.RB_inmediato.setChecked(True)

                         
        self.view.LE_subtotal.setReadOnly(True)
        self.view.LE_igv.setReadOnly(True)
        self.view.LE_total.setReadOnly(True)
        self.view.LE_subtotal.setText("0.00")
        self.view.LE_igv.setText("0.00")
        self.view.LE_total.setText("0.00")

                                                                     
        self.view.LE_cantidad.setReadOnly(True)
        self.view.LE_cantidad.setPlaceholderText("Stock disponible")

    def load_datos_iniciales(self):
                                                      
        categorias = self.model.get_categorias()
        self.view.CB_categoria.clear()
        self.view.CB_categoria_2.clear()
        for c in categorias:
            self.view.CB_categoria.addItem(c[1], c[0])
            self.view.CB_categoria_2.addItem(c[1], c[0])

                                                            
        self.view.CB_numero_h.clear()
        hab_ocupadas = self.model.get_habitaciones_ocupadas()
        if hab_ocupadas:
            for id_hab, numero, id_res in hab_ocupadas:
                self.view.CB_numero_h.addItem(f"Hab. {numero}", (id_hab, id_res))
        else:
            self.view.CB_numero_h.addItem("Sin ocupadas")

                                                  
        if self.view.CB_categoria.count() > 0:
            self._cargar_productos(self.view.CB_categoria, self.view.CB_producto)
            self._cargar_productos(self.view.CB_categoria_2, self.view.CB_producto_v)

    def setup_connections(self):
                                                                          
        self.view.CB_categoria.currentIndexChanged.connect(
            lambda: self._on_categoria_inv_changed()
        )
                                               
        self.view.CB_categoria_2.currentIndexChanged.connect(
            lambda: self._cargar_productos(self.view.CB_categoria_2, self.view.CB_producto_v)
        )

                 
        self.view.PB_cargar.clicked.connect(self.agregar_stock)                     
        self.view.PB_pagar.clicked.connect(self.realizar_venta)                  

                                                                          
                                                                           
                                                                          
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

                                                                          
                                                                          
                                                                          
    def agregar_stock(self):
                                    
        nombre_nuevo = self.view.LE_producto.text().strip()
        id_categoria = self.view.CB_categoria_2.currentData()
        cantidad_txt = self.view.LE_cantidad_2.text().strip()

        if not cantidad_txt.isdigit() or int(cantidad_txt) <= 0:
            QMessageBox.warning(self.window, "Error", "Ingrese una cantidad válida (número > 0).")
            return

        cantidad = int(cantidad_txt)

                                                             
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
                                                            
            self._cargar_productos(self.view.CB_categoria_2, self.view.CB_producto_v)
            QMessageBox.information(self.window, "Creado",
                                    f"Producto '{nombre_nuevo}' creado.")
            self.view.LE_producto.clear()
                                                   
            prods = self.model.get_productos_by_categoria(id_categoria)
            id_prod_nuevo = next((p[0] for p in prods if p[1].lower() == nombre_nuevo.lower()), None)
            if id_prod_nuevo:
                self.model.agregar_stock_entrada(id_prod_nuevo, cantidad, id_usuario)
        else:
                                                             
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

                                                  
        hab_data = self.view.CB_numero_h.currentData()
        id_comprobante = None                                                   

        exito, msg = self.model.registrar_venta(id_prod, cantidad, id_usuario, id_comprobante)

        if exito:
            nombre_prod = self.view.CB_producto_v.currentText()

                                            
            row = self.view.TW_productos.rowCount()
            self.view.TW_productos.insertRow(row)
            self.view.TW_productos.setItem(row, 0, QTableWidgetItem(nombre_prod))
            self.view.TW_productos.setItem(row, 1, QTableWidgetItem(str(cantidad)))
            self.view.TW_productos.setItem(row, 2, QTableWidgetItem("—"))                               

            self._actualizar_totales_venta()
            self._actualizar_stock()
            QMessageBox.information(self.window, "✅ Venta registrada",
                                    f"{cantidad} x {nombre_prod} registrado correctamente.")
        else:
            QMessageBox.critical(self.window, "❌ Error", msg)

    def _actualizar_totales_venta(self):
        """Calcula subtotal, IGV y total del carrito."""
                                                                        
        filas = self.view.TW_productos.rowCount()
        self.view.LE_subtotal.setText(f"{filas} ítem(s)")
        self.view.LE_igv.setText("18% incluido")
        self.view.LE_total.setText("Ver checkout")
