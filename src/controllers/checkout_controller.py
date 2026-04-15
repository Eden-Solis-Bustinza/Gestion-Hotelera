from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QHeaderView, QDialog, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from src.views.FrmCheckout import Ui_Dialog
from src.models.checkout_model import CheckoutModel
from datetime import datetime
import math


class CheckoutController:
    def __init__(self, user_data):
        self.window = QtWidgets.QDialog()
        self.view = Ui_Dialog()
        self.view.setupUi(self.window)

        self.user_data = user_data
        self.model = CheckoutModel()

        self.reserva_actual = None
        self.total_calculado = 0.0
        self.monto_adelantado = 0.0
        self.tarifa_diaria = 0.0
        self.tarifa_diaria = 0.0
        self._ultimo_comprobante_id = None
        self._extras_cargados = []                                                              

        self.window.setWindowState(QtCore.Qt.WindowMaximized)

        self.setup_ui()
        self.setup_connections()

    def show(self):
        self.window.exec_()

    def setup_ui(self):
        self.view.PB_checkout.setEnabled(False)
        self.view.PB_comprobante.setEnabled(False)
        self.view.CB_numero_h.setEnabled(True)
        self.view.LE_numero_d.setReadOnly(False)

                         
        self.view.TW_productos.setColumnCount(3)
        self.view.TW_productos.setHorizontalHeaderLabels(["Descripción", "Cant.", "SubT."])
        self.view.TW_productos.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.view.TW_productos.setRowCount(0)

        metodos = self.model.get_metodos_pago()
        self.view.CB_medio_p.clear()
        if metodos:
            for id_m, nombre in metodos:
                self.view.CB_medio_p.addItem(nombre, id_m)
        else:
            for nombre in ["Efectivo", "Tarjeta", "Transferencia", "Otro"]:
                self.view.CB_medio_p.addItem(nombre)

        habs_ocupadas = self.model.get_habitaciones_ocupadas()
        self.view.CB_numero_h.clear()
        if habs_ocupadas:
            for id_v, numero in habs_ocupadas:
                self.view.CB_numero_h.addItem(str(numero), id_v)
        else:
            self.view.CB_numero_h.addItem("Sin habitaciones ocupadas")
            self.view.CB_numero_h.setEnabled(False)

        productos = self.model.get_productos()
        self.view.CB_producto.clear()
        for id_p, nombre, precio in productos:
            self.view.CB_producto.addItem(f"{nombre} (S/.{precio:.2f})", {'id': id_p, 'precio': precio, 'nombre': nombre})

    def setup_connections(self):
        self.view.PB_buscar.clicked.connect(self.buscar_por_habitacion)
        if hasattr(self.view, 'PB_cargar'):
            self.view.PB_cargar.clicked.connect(self.buscar_reserva)
        self.view.PB_cargar_e.clicked.connect(self.agregar_extra)
        
        self.view.PB_checkout.clicked.connect(self.procesar_checkout)
        self.view.PB_comprobante.clicked.connect(self.mostrar_comprobante)
        self.view.PB_salir.clicked.connect(self.window.close)

    def buscar_por_habitacion(self):
        id_hab = self.view.CB_numero_h.currentData()
        if not id_hab:
            QMessageBox.warning(self.window, "Atención", "No hay habitación seleccionada válida.")
            return

        reserva = self.model.buscar_reserva_activa(id_hab, is_id_habitacion=True)
        if not reserva:
            QMessageBox.warning(self.window, "No encontrado", "No se encontró reserva para esta habitación.")
            self.limpiar_ui()
            return
            
        self.cargar_datos_en_ui(reserva)

    def buscar_reserva(self):
        dni = self.view.LE_numero_d.text().strip()
        if not dni:
            QMessageBox.warning(self.window, "Error", "Ingrese número de documento.")
            return

        reserva = self.model.buscar_reserva_activa(dni, False)
        if not reserva:
            QMessageBox.warning(self.window, "No encontrado",
                                "No hay reservas con habitación OCUPADA para este documento.")
            self.limpiar_ui()
            return
            
        self.cargar_datos_en_ui(reserva)

    def cargar_datos_en_ui(self, reserva):
        self.reserva_actual = reserva

        self.view.LE_numero_d.setText(str(reserva.get('nro_documento', '')))                                 
        self.view.LE_nombres_apellidos.setText(reserva['huesped_nombres'])
        self.view.LE_contacto.setText(str(reserva['huesped_contacto']) if reserva['huesped_contacto'] else "")
        
        idx = self.view.CB_numero_h.findData(reserva['id_habitacion'])
        if idx >= 0:
            self.view.CB_numero_h.setCurrentIndex(idx)

        f_in = reserva['fecha_in']
        if isinstance(f_in, str):
            f_in = datetime.strptime(f_in, "%Y-%m-%d %H:%M:%S")

        f_out = datetime.now()
        self.view.DT_fyh_salida_r.setDateTime(QtCore.QDateTime(f_out.year, f_out.month,
                                                                f_out.day, f_out.hour,
                                                                f_out.minute, f_out.second))
        dias = math.ceil((f_out - f_in).total_seconds() / 86400.0)
        dias = max(1, dias)
        self.view.LE_dias_e.setText(str(dias))

        self.tarifa_diaria = reserva.get('tarifa_base', 0.0)
        self.monto_adelantado = reserva['monto_adelanto']
        self.view.LE_monto_a.setText(f"{self.monto_adelantado:.2f}")

        self.calcular_totales()
        self.view.PB_checkout.setEnabled(True)

    def agregar_extra(self):
        """Agrega un producto extra consumido a la tabla temporal y recalcula total."""
        if not self.reserva_actual:
            QMessageBox.warning(self.window, "Atención", "Busque una reserva activa primero.")
            return

        data_prod = self.view.CB_producto.currentData()
        if not data_prod:
            return
            
        cantidad = self.view.SB_cantidad.value()
        if cantidad <= 0:
            QMessageBox.warning(self.window, "Atención", "Seleccione una cantidad mayor a 0.")
            return
            
        subtotal = float(data_prod['precio']) * cantidad
        
        self._extras_cargados.append({
            'id_producto': data_prod['id'],
            'cantidad': cantidad,
            'subtotal': subtotal
        })
        
        row = self.view.TW_productos.rowCount()
        self.view.TW_productos.insertRow(row)
        
        item_desc = QtWidgets.QTableWidgetItem(data_prod['nombre'])
        item_desc.setData(QtCore.Qt.UserRole, data_prod['id'])                              
        self.view.TW_productos.setItem(row, 0, item_desc)
        
        item_cant = QtWidgets.QTableWidgetItem(str(cantidad))
        item_cant.setTextAlignment(QtCore.Qt.AlignCenter)
        self.view.TW_productos.setItem(row, 1, item_cant)
        
        item_sub = QtWidgets.QTableWidgetItem(f"{subtotal:.2f}")
        item_sub.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.view.TW_productos.setItem(row, 2, item_sub)
        
        self.calcular_totales()
        
        self.view.SB_cantidad.setValue(0)

    def calcular_totales(self):
        if not self.reserva_actual:
            return

        try:
            dias = int(self.view.LE_dias_e.text())
        except ValueError:
            dias = 1

        subtotal_hab = round(self.tarifa_diaria * dias, 2)
        self.view.LE_subtotal.setText(f"{subtotal_hab:.2f}")

        extras = 0.0
        for row in range(self.view.TW_productos.rowCount()):
            item = self.view.TW_productos.item(row, 2)
            if item:
                try:
                    extras += float(item.text())
                except ValueError:
                    pass

        total = subtotal_hab + extras
        total_a_pagar = max(0.0, total - self.monto_adelantado)
        self.total_calculado = total_a_pagar
        self.view.LE_total.setText(f"{total_a_pagar:.2f}")

    def procesar_checkout(self):
        if not self.reserva_actual:
            return

        try:
            dias = int(self.view.LE_dias_e.text())
            subT = float(self.view.LE_subtotal.text())
            total = float(self.view.LE_total.text())
        except ValueError:
            QMessageBox.warning(self.window, "Error", "Valores numéricos inválidos.")
            return

        id_metodo = self.view.CB_medio_p.currentData()
        if id_metodo is None:
            id_metodo = self.view.CB_medio_p.currentIndex() + 1

        id_usuario = self.user_data.get('id', 1)

        exito, id_comp = self.model.procesar_checkout(
            self.reserva_actual['id_reserva'],
            self.reserva_actual['id_habitacion'],
            dias, subT, total, id_metodo, id_usuario,
            self._extras_cargados  
        )

        if exito:
            self._ultimo_comprobante_id = id_comp
            QMessageBox.information(
                self.window, "✅ Check-out exitoso",
                f"Estancia cerrada. Habitación pasa a 'En Limpieza'.\n"
                f"Comprobante generado."
            )
            self.view.PB_comprobante.setEnabled(True)
            self.view.PB_checkout.setEnabled(False)
        else:
            QMessageBox.critical(self.window, "❌ Error",
                                 "No se pudo realizar el check-out. Operación revertida.")

    def mostrar_comprobante(self):
        """REQ-09: Genera el comprobante final en un documento PDF interactivo."""
        from PyQt5.QtWidgets import QFileDialog
        
        if not self._ultimo_comprobante_id:
            return

        datos = self.model.get_detalle_comprobante(self._ultimo_comprobante_id)
        if not datos:
            QMessageBox.warning(self.window, "Error", "No se pudo obtener el comprobante.")
            return

        default_name = f"Comprobante_{datos['numero_comprobante']}.pdf"
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self.window, "Guardar Comprobante PDF", default_name, "Archivos PDF (*.pdf)", options=options)
        
        if file_path:
            try:
                self.generar_pdf(file_path, datos)
                import webbrowser
                webbrowser.open_new(file_path)
            except Exception as e:
                QMessageBox.critical(self.window, "Error", f"No se pudo guardar el PDF:\n{e}")

    def generar_pdf(self, path, datos):
        from reportlab.lib.pagesizes import A5
        from reportlab.pdfgen import canvas
        
        c = canvas.Canvas(path, pagesize=A5)
        ancho, alto = A5

        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(ancho / 2, alto - 40, "HOTEL SUMAK WASI")
        c.setFont("Helvetica", 10)
        c.drawCentredString(ancho / 2, alto - 55, "Av. Principal 123, Ciudad")
        c.drawCentredString(ancho / 2, alto - 70, "RUC: 10123456789 - Tel: (01) 234-5678")

        c.setFont("Helvetica-Bold", 13)
        c.drawCentredString(ancho / 2, alto - 100, f"COMPROBANTE DE PAGO N° {datos['numero_comprobante']}")
        
        c.line(30, alto - 110, ancho - 30, alto - 110)

        c.setFont("Helvetica", 10)
        y = alto - 130
        
        fecha_pago = datos["fecha_pago"]
        if hasattr(fecha_pago, "strftime"):
            fecha_pago = fecha_pago.strftime("%d/%m/%Y %H:%M:%S")

        c.drawString(30, y, f"Fecha Emisión: {fecha_pago}")
        c.drawString(30, y - 20, f"Huésped: {datos['huesped']}")
        c.drawString(30, y - 40, f"Documento: {datos['nro_documento']}")
        
        c.drawString(ancho / 2 + 10, y - 20, f"Habitación: {datos['habitacion']} ({datos['tipo_hab']})")
        c.drawString(ancho / 2 + 10, y - 40, f"Días Estancia: {datos['dias_estancia']}")

        c.drawString(30, y - 60, f"Método de Pago: {datos['metodo_pago']}")

        y -= 85
        c.line(30, y, ancho - 30, y)
        
        c.setFont("Helvetica-Bold", 10)
        c.drawString(30, y - 15, "DESCRIPCIÓN")
        c.drawString(ancho - 100, y - 15, "IMPORTE")
        c.line(30, y - 20, ancho - 30, y - 20)

        c.setFont("Helvetica", 10)
        c.drawString(30, y - 40, "Alojamiento / Extras Totales")
        c.drawString(ancho - 100, y - 40, f"S/. {datos['subtotal']:.2f}")
        
        c.line(30, y - 55, ancho - 30, y - 55)

        c.setFont("Helvetica-Bold", 11)
        c.drawString(ancho - 180, y - 75, "TOTAL PAGADO:")
        c.drawString(ancho - 100, y - 75, f"S/. {datos['total_general']:.2f}")

        c.setFont("Helvetica-Oblique", 9)
        c.drawCentredString(ancho / 2, y - 120, "¡Gracias por su visita y feliz viaje!")

        c.save()

    def limpiar_ui(self):
        self.reserva_actual = None
        self._ultimo_comprobante_id = None
        self._extras_cargados = []
        self.view.LE_nombres_apellidos.clear()
        self.view.LE_contacto.clear()
                                                             
        self.view.LE_subtotal.clear()
        self.view.LE_total.clear()
        self.view.LE_monto_a.clear()
        self.view.PB_checkout.setEnabled(False)
        self.view.PB_comprobante.setEnabled(False)
