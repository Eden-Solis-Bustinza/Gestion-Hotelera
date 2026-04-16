from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (
    QMessageBox, QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTableWidget, QTableWidgetItem,
    QHeaderView, QDateTimeEdit, QSpinBox, QDoubleSpinBox,
    QFrame, QGroupBox
)
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import QFont
from src.views.FrmCrear_reserva import Ui_Dialog
from src.models.reserva_model import ReservaModel
from datetime import datetime
import random
import string


class CrearReservaController:
    def __init__(self, user_data):
        self.window = QtWidgets.QDialog()
        self.view = Ui_Dialog()
        self.view.setupUi(self.window)

        self.user_data = user_data
        self.model = ReservaModel()

        self.id_huesped_actual = None
        self.lista_extras = []

        self.window.setWindowState(QtCore.Qt.WindowMaximized)

        self.setup_ui_defaults()
        self.setup_connections()

    def show(self):
        self.window.exec_()

    def setup_ui_defaults(self):
        self.view.PB_crear.setEnabled(False)
        self.view.CB_numero_h.setEnabled(False)

        ahora = QtCore.QDateTime.currentDateTime()
        self.view.DT_fyh_ingreso.setMinimumDateTime(ahora)
        self.view.DT_fyh_salida.setMinimumDateTime(ahora.addDays(1))
        self.view.DT_fyh_ingreso.setDateTime(ahora)
        self.view.DT_fyh_salida.setDateTime(ahora.addDays(1))

        self.cargar_metodos_pago()

    def cargar_metodos_pago(self):
        metodos = self.model.get_metodos_pago()
        self.view.CB_medio_p.clear()
        for id_m, nombre in metodos:
            self.view.CB_medio_p.addItem(nombre, id_m)

        productos = self.model.get_productos()
        self.view.CB_producto.clear()
        for id_p, nombre, precio in productos:
            self.view.CB_producto.addItem(f"{nombre} (S/.{float(precio):.2f})", {'id': id_p, 'precio': float(precio), 'nombre': nombre})

    def setup_connections(self):
        self.view.PB_buscar.clicked.connect(self.buscar_huesped)
        self.view.PB_validar.clicked.connect(self.validar_disponibilidad)
        self.view.PB_crear.clicked.connect(self.crear_reserva)
        if hasattr(self.view, 'PB_cargar_2'):
            self.view.PB_cargar_2.clicked.connect(self.agregar_extra)
        self.view.PB_salir.clicked.connect(self.window.close)
                                                             
        if hasattr(self.view, 'PB_gestionar'):
            self.view.PB_gestionar.clicked.connect(self.abrir_gestion_reservas)

    def buscar_huesped(self):
        dni = self.view.LE_numero_d.text().strip()
        if not dni:
            QMessageBox.warning(self.window, "Error", "Ingrese documento.")
            return

        h = self.model.buscar_huesped_por_dni(dni)
        if h:
            self.id_huesped_actual = h['id']
            self.view.LE_nombres_apellidos.setText(h['nombres'])
            self.view.LE_contacto.setText(h['contacto'] or "")
            self.view.LE_correo.setText(h['email'] or "")
            
            # Generar código único R + DNI + 3 letras aleatorias
            letras = ''.join(random.choices(string.ascii_uppercase, k=3))
            codigo_reserva = f"R{dni}{letras}"
            self.view.LE_id_r.setText(codigo_reserva)
            self.view.LE_id_r.setReadOnly(True)
            
            QMessageBox.information(self.window, "✅ Éxito", "Huésped encontrado.")
        else:
            self.id_huesped_actual = None
            self.view.LE_nombres_apellidos.clear()
            self.view.LE_id_r.clear()
            QMessageBox.warning(self.window, "No encontrado",
                                "Huésped no existe. Regístrelo primero.")

    def validar_disponibilidad(self):
        f_in  = self.view.DT_fyh_ingreso.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        f_out = self.view.DT_fyh_salida.dateTime().toString("yyyy-MM-dd HH:mm:ss")

        if self.view.DT_fyh_ingreso.dateTime() >= self.view.DT_fyh_salida.dateTime():
            QMessageBox.warning(self.window, "Fechas",
                                "La salida debe ser posterior al ingreso.")
            return

        habs = self.model.get_habitaciones_disponibles(f_in, f_out)
        self.view.CB_numero_h.clear()

        if not habs:
            QMessageBox.warning(self.window, "Sin disponibilidad",
                                "No hay habitaciones para esas fechas.")
            self.view.CB_numero_h.setEnabled(False)
            self.view.PB_crear.setEnabled(False)
            return

        for hab in habs:
            self.view.CB_numero_h.addItem(f"{hab[1]} - {hab[2]}  (S/. {hab[3]}/noche)", hab[0])

        self.view.CB_numero_h.setEnabled(True)
        if self.id_huesped_actual:
            self.view.PB_crear.setEnabled(True)

        QMessageBox.information(self.window, "Disponible",
                                f"Se encontraron {len(habs)} habitación(es) disponible(s).")

    def agregar_extra(self):
        data_prod = self.view.CB_producto.currentData()
        if not data_prod:
            QMessageBox.warning(self.window, "Atención", "Seleccione un producto.")
            return
            
        cantidad = self.view.SB_cantidad.value()
        if cantidad <= 0:
            QMessageBox.warning(self.window, "Atención", "Seleccione una cantidad mayor a 0.")
            return
            
        subtotal = data_prod['precio'] * cantidad
        
        self.lista_extras.append({
            'id_producto': data_prod['id'],
            'cantidad': cantidad,
            'precio': data_prod['precio'],
            'subtotal': subtotal
        })
        
        row = self.view.TW_productos_c.rowCount()
        self.view.TW_productos_c.insertRow(row)
        
        item_desc = QTableWidgetItem(data_prod['nombre'])
        item_desc.setTextAlignment(Qt.AlignCenter)
        self.view.TW_productos_c.setItem(row, 0, item_desc)
        
        item_cant = QTableWidgetItem(str(cantidad))
        item_cant.setTextAlignment(Qt.AlignCenter)
        self.view.TW_productos_c.setItem(row, 1, item_cant)
        
        item_sub = QTableWidgetItem(f"{subtotal:.2f}")
        item_sub.setTextAlignment(Qt.AlignCenter)
        self.view.TW_productos_c.setItem(row, 2, item_sub)
        
        total = sum(item['subtotal'] for item in self.lista_extras)
        self.view.LE_monto.setText(f"{total:.2f}")
        
        self.view.SB_cantidad.setValue(0)

    def crear_reserva(self):
        if not self.id_huesped_actual:
            QMessageBox.warning(self.window, "Error", "Busque un huésped primero.")
            return

        id_hab = self.view.CB_numero_h.currentData()
        if not id_hab:
            QMessageBox.warning(self.window, "Error", "Seleccione una habitación.")
            return

        num_huespedes = self.view.SB_numero_h.value()
        if num_huespedes <= 0:
            QMessageBox.warning(self.window, "Error", "Ingrese un n° de huéspedes.")
            return

        monto = self.view.LE_monto_a.text().strip()
        monto_float = float(monto) if monto.replace('.', '', 1).isdigit() else 0.0
        id_metodo = self.view.CB_medio_p.currentData()

        f_in  = self.view.DT_fyh_ingreso.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        f_out = self.view.DT_fyh_salida.dateTime().toString("yyyy-MM-dd HH:mm:ss")

        exito = self.model.crear_reserva(
            self.id_huesped_actual, id_hab, num_huespedes,
            f_in, f_out, monto_float,
            self.user_data.get('id', 1),
            lista_extras=self.lista_extras
        )

        codigo_generado = self.view.LE_id_r.text()

        if exito:
            QMessageBox.information(self.window, "✅ Reserva creada",
                                    f"Reserva registrada exitosamente.\n\nCódigo de Reserva: {codigo_generado}")
            self.window.close()
        else:
            QMessageBox.critical(self.window, "❌ Error",
                                 "No se pudo crear la reserva. Verifique disponibilidad.")

    def abrir_gestion_reservas(self):
        """Abre un diálogo con la lista de reservas activas para gestionar."""
        reservas = self.model.get_reservas_activas()

        dlg = QDialog(self.window)
        dlg.setWindowTitle("Gestión de Reservas — Modificar / Cancelar")
        dlg.setMinimumSize(900, 500)
        dlg.setWindowState(Qt.WindowMaximized)
        dlg.setStyleSheet("""
            QDialog { background-color: #EBEDEF; }
            QLabel { font-family: 'Berlin Sans FB'; }
            QPushButton {
                background-color: #2C3E50; color: white; border-radius: 5px;
                font-weight: bold; padding: 7px 14px; font-family: 'Berlin Sans FB';
            }
            QPushButton:hover { background-color: #16A085; }
            QTableWidget { background: white; font-family: 'Berlin Sans FB'; }
            QHeaderView::section {
                background-color: #2C3E50; color: white; padding: 6px; font-weight: bold;
            }
        """)

        lay = QVBoxLayout(dlg)
        lay.setContentsMargins(16, 16, 16, 16)
        lay.setSpacing(10)

        titulo = QLabel("Reservas Activas (Pendiente / Confirmada)")
        titulo.setFont(QFont("Berlin Sans FB", 13, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color: #2C3E50;")
        lay.addWidget(titulo)

        tabla = QTableWidget()
        tabla.setColumnCount(8)
        tabla.setHorizontalHeaderLabels([
            "ID", "Huésped", "DNI", "Habitación",
            "Check-in", "Check-out", "Estado", "Monto Adelanto"
        ])
        tabla.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        tabla.setEditTriggers(QTableWidget.NoEditTriggers)
        tabla.setSelectionBehavior(QTableWidget.SelectRows)
        tabla.setAlternatingRowColors(True)
        tabla.setStyleSheet("alternate-background-color: #F8F9F9;")

        for res in reservas:
            row = tabla.rowCount()
            tabla.insertRow(row)
            fi = res['fecha_checkin']
            fo = res['fecha_checkout']
            fi_str = fi.strftime("%d/%m/%Y %H:%M") if hasattr(fi, 'strftime') else str(fi)[:16]
            fo_str = fo.strftime("%d/%m/%Y %H:%M") if hasattr(fo, 'strftime') else str(fo)[:16]
            vals = [
                str(res['id_reserva']),
                res['huesped'],
                res['nro_documento'],
                res['habitacion'],
                fi_str, fo_str,
                res['estado'],
                f"S/. {float(res['monto_adelantado']):.2f}"
            ]
            for col, v in enumerate(vals):
                item = QTableWidgetItem(v)
                item.setTextAlignment(Qt.AlignCenter)
                tabla.setItem(row, col, item)
                                
            color = "#D5F5E3" if res['estado'] == "Confirmada" else "#FEF9E7"
            for col in range(tabla.columnCount()):
                if tabla.item(row, col):
                    tabla.item(row, col).setBackground(QtWidgets.QColor(color))

        lay.addWidget(tabla)

        btn_row = QHBoxLayout()

        btn_cancelar_res = QPushButton("🚫  Cancelar Reserva")
        btn_cancelar_res.setStyleSheet(
            "background-color: #E74C3C;")
        btn_cancelar_res.clicked.connect(
            lambda: self._cancelar_seleccionada(tabla, dlg, reservas)
        )

        btn_modificar_res = QPushButton("✏️  Modificar Reserva")
        btn_modificar_res.clicked.connect(
            lambda: self._modificar_seleccionada(tabla, dlg, reservas)
        )

        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.setStyleSheet("background-color: #7F8C8D;")
        btn_cerrar.clicked.connect(dlg.close)

        btn_row.addWidget(btn_cancelar_res)
        btn_row.addWidget(btn_modificar_res)
        btn_row.addStretch()
        btn_row.addWidget(btn_cerrar)
        lay.addLayout(btn_row)

        dlg.exec_()

    def _cancelar_seleccionada(self, tabla, dlg, reservas):
        fila = tabla.currentRow()
        if fila < 0:
            QMessageBox.warning(dlg, "Error", "Seleccione una reserva.")
            return
        id_reserva = int(tabla.item(fila, 0).text())
        huesped = tabla.item(fila, 1).text()

        confirm = QMessageBox.question(
            dlg, "Confirmar cancelación",
            f"¿Cancelar la reserva #{id_reserva} de {huesped}?\n"
            "Esta acción no se puede deshacer.",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            ok = self.model.cancelar_reserva(id_reserva)
            if ok:
                QMessageBox.information(dlg, "✅", f"Reserva #{id_reserva} cancelada.")
                dlg.close()
            else:
                QMessageBox.critical(dlg, "❌ Error",
                                     "No se pudo cancelar. La reserva puede haber cambiado de estado.")

    def _modificar_seleccionada(self, tabla, dlg, reservas):
        fila = tabla.currentRow()
        if fila < 0:
            QMessageBox.warning(dlg, "Error", "Seleccione una reserva.")
            return

        id_reserva = int(tabla.item(fila, 0).text())
        res = next((r for r in reservas if r['id_reserva'] == id_reserva), None)
        if not res:
            return

        mod_dlg = QDialog(dlg)
        mod_dlg.setWindowTitle(f"Modificar Reserva #{id_reserva}")
        mod_dlg.setMinimumSize(420, 320)
        mod_dlg.setStyleSheet(dlg.styleSheet())

        lay = QVBoxLayout(mod_dlg)
        lay.setContentsMargins(20, 20, 20, 20)
        lay.setSpacing(10)

        lbl = QLabel(f"<b>Huésped:</b> {res['huesped']} | <b>Hab:</b> {res['habitacion']}")
        lbl.setFont(QFont("Berlin Sans FB", 10))
        lay.addWidget(lbl)

        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        lay.addWidget(sep)

        from PyQt5.QtWidgets import QFormLayout
        form = QFormLayout()

        fi_actual = res['fecha_checkin']
        fo_actual = res['fecha_checkout']
        fi_qdt = QDateTime.fromString(
            fi_actual.strftime("%Y-%m-%d %H:%M:%S") if hasattr(fi_actual, 'strftime') else str(fi_actual)[:19],
            "yyyy-MM-dd HH:mm:ss"
        )
        fo_qdt = QDateTime.fromString(
            fo_actual.strftime("%Y-%m-%d %H:%M:%S") if hasattr(fo_actual, 'strftime') else str(fo_actual)[:19],
            "yyyy-MM-dd HH:mm:ss"
        )

        dt_in = QDateTimeEdit(fi_qdt)
        dt_in.setCalendarPopup(True)
        dt_in.setDisplayFormat("dd/MM/yyyy HH:mm")
        form.addRow("Nueva fecha Check-in:", dt_in)

        dt_out = QDateTimeEdit(fo_qdt)
        dt_out.setCalendarPopup(True)
        dt_out.setDisplayFormat("dd/MM/yyyy HH:mm")
        form.addRow("Nueva fecha Check-out:", dt_out)

        sb_hues = QSpinBox()
        sb_hues.setMinimum(1)
        sb_hues.setMaximum(10)
        sb_hues.setValue(int(res['nro_huespedes']) if res['nro_huespedes'] else 1)
        form.addRow("N° huéspedes:", sb_hues)

        sb_monto = QDoubleSpinBox()
        sb_monto.setMinimum(0.0)
        sb_monto.setMaximum(99999.0)
        sb_monto.setDecimals(2)
        sb_monto.setValue(float(res['monto_adelantado']) if res['monto_adelantado'] else 0.0)
        form.addRow("Monto adelantado:", sb_monto)

        lay.addLayout(form)

        btn_h = QHBoxLayout()
        btn_cancel = QPushButton("Cancelar")
        btn_cancel.setStyleSheet("background-color: #7F8C8D;")
        btn_cancel.clicked.connect(mod_dlg.reject)
        btn_save = QPushButton("Guardar cambios")
        btn_save.clicked.connect(lambda: self._guardar_modificacion(
            id_reserva,
            dt_in.dateTime().toString("yyyy-MM-dd HH:mm:ss"),
            dt_out.dateTime().toString("yyyy-MM-dd HH:mm:ss"),
            sb_hues.value(), sb_monto.value(), mod_dlg, dlg
        ))
        btn_h.addWidget(btn_cancel)
        btn_h.addWidget(btn_save)
        lay.addLayout(btn_h)

        mod_dlg.exec_()

    def _guardar_modificacion(self, id_res, f_in, f_out, n_hues, monto, mod_dlg, parent_dlg):
        if f_in >= f_out:
            QMessageBox.warning(mod_dlg, "Error", "La fecha de salida debe ser posterior.")
            return
        ok = self.model.modificar_reserva(id_res, f_in, f_out, n_hues, monto)
        if ok:
            QMessageBox.information(mod_dlg, "✅", f"Reserva #{id_res} modificada.")
            mod_dlg.accept()
            parent_dlg.close()
        else:
            QMessageBox.critical(mod_dlg, "❌ Error", "No se pudo modificar la reserva.")
