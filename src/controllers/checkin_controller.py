from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from src.views.FrmCheckin import Ui_Dialog
from src.models.checkin_model import CheckinModel
from datetime import datetime

class CheckinController:
    def __init__(self, user_data): 
        self.window = QtWidgets.QDialog()
        self.view = Ui_Dialog()
        self.view.setupUi(self.window)
        
        self.user_data = user_data
        self.model = CheckinModel()
        
        self.id_huesped_actual = None 
        
        self.setup_ui_defaults()
        self.setup_connections()

    def show(self):
        self.window.exec_()

    def setup_ui_defaults(self):
        """Configuración de seguridad inicial y control de fechas"""
        self.view.PB_marcar_checkin.setEnabled(False)
        self.view.CB_numero_h.setEnabled(False)
        
        self.view.CB_tipo_h.hide()
        self.view.label_19.hide()

        self.view.SB_numero_h.setReadOnly(False)
        self.view.LE_monto_a.setReadOnly(False)
        self.view.DT_fyh_salida.setReadOnly(False)

        self.view.DT_fyh_ingreso.setReadOnly(True)

        ahora = QtCore.QDateTime.currentDateTime()
        self.view.DT_fyh_ingreso.setDateTime(ahora)
        
        self.view.DT_fyh_salida.setMinimumDateTime(ahora)

        manana = ahora.addDays(1)
        manana.setTime(QtCore.QTime(12, 0))
        self.view.DT_fyh_salida.setDateTime(manana)

                       
        self.cargar_habitaciones()
        self.cargar_metodos_pago()

    def cargar_habitaciones(self):
        habitaciones = self.model.get_habitaciones_disponibles()
        self.view.CB_numero_h.clear()
        if not habitaciones:
            self.view.CB_numero_h.addItem("Sin habitaciones disponibles")
            return
            
        for id_hab, numero, tipo in habitaciones:
            self.view.CB_numero_h.addItem(f"{numero} - {tipo}", id_hab)

    def cargar_metodos_pago(self):
        metodos = self.model.get_metodos_pago()
        self.view.CB_medio_p.clear()
        for id_metodo, nombre in metodos:
            self.view.CB_medio_p.addItem(nombre, id_metodo)

    def setup_connections(self):
        self.view.PB_buscar.clicked.connect(self.buscar_huesped)
        self.view.PB_marcar_checkin.clicked.connect(self.procesar_checkin)
        self.view.PB_salir.clicked.connect(self.window.close)

    def buscar_huesped(self):
        dni = self.view.LE_numero_d.text().strip()
        if not dni:
            QMessageBox.warning(self.window, "Error", "Ingrese un número de documento.")
            return

        huesped = self.model.buscar_huesped_por_dni(dni)
        
        if huesped:
            self.id_huesped_actual = huesped['id']
            self.view.LE_nombres_apellidos.setText(huesped['nombres'])
            self.view.LE_contacto.setText(huesped['contacto'])
            
            self.view.CB_numero_h.setEnabled(True)
            self.view.PB_marcar_checkin.setEnabled(True)
            self.view.LE_id_r.setText("INGRESO DIRECTO")
            QMessageBox.information(self.window, "Encontrado", "Huésped validado. Proceda con el Check-in.")
        else:
            self.id_huesped_actual = None
            self.view.PB_marcar_checkin.setEnabled(False)
            self.view.CB_numero_h.setEnabled(False)
            self.view.LE_nombres_apellidos.clear()
            self.view.LE_contacto.clear()
            QMessageBox.warning(self.window, "No encontrado", "El DNI no está registrado. Por favor, registre al huésped primero.")

    def procesar_checkin(self):
                                      
        if not self.id_huesped_actual:
            return

        id_habitacion = self.view.CB_numero_h.currentData()
        if not id_habitacion:
            QMessageBox.warning(self.window, "Error", "No hay habitaciones disponibles seleccionadas.")
            return

        num_huespedes = self.view.SB_numero_h.value()
        if num_huespedes <= 0:
            QMessageBox.warning(self.window, "Error", "El número de huéspedes debe ser mayor a cero.")
            return

        monto_adelantado = self.view.LE_monto_a.text().strip()
        if not monto_adelantado.replace('.', '', 1).isdigit():
            monto_adelantado = 0.0
        else:
            monto_adelantado = float(monto_adelantado)

        id_metodo = self.view.CB_medio_p.currentData()
        fecha_in = self.view.DT_fyh_ingreso.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        fecha_out = self.view.DT_fyh_salida.dateTime().toString("yyyy-MM-dd HH:mm:ss")

                              
                                                                      
        exito = self.model.registrar_checkin_directo(
            self.id_huesped_actual, id_habitacion, num_huespedes,
            fecha_in, fecha_out, monto_adelantado, id_metodo,
            self.user_data.get('id', 1)
        )

        if exito:
            QMessageBox.information(self.window, "Éxito", "Check-in registrado. La habitación ahora está OCUPADA.")
            self.window.close()
        else:
            QMessageBox.critical(self.window, "Error Transaccional", "Ocurrió un error al procesar el Check-in. Operación revertida por seguridad.")