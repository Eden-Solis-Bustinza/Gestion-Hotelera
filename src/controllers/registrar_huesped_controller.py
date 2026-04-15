from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from src.views.FrmRegistrar_huesped import Ui_Dialog
from src.models.huesped_model import HuespedModel
import re
from datetime import date # Importación obligatoria para cálculos matemáticos de fechas

class RegistrarHuespedController:
    def __init__(self):
        self.window = QtWidgets.QDialog()
        self.view = Ui_Dialog()
        self.view.setupUi(self.window)
        
        self.huesped_model = HuespedModel()
        self.setup_ui_defaults()
        self.load_combos()
        self.setup_connections()

    def show(self):
        self.window.exec_()

    def setup_ui_defaults(self):
        """Configura valores iniciales del calendario"""
        # Forzar el formato visual a dd/mm/aa (ej. 15/04/26)
        self.view.DT_nacimiento.setDisplayFormat("dd/MM/yy")
        
        # Llama a la fecha del equipo por defecto
        fecha_actual = QtCore.QDate.currentDate()
        self.view.DT_nacimiento.setDate(fecha_actual)
        
        # Bloquear campo para que no se pueda modificar
        self.view.DT_nacimiento.setReadOnly(True)
        # Quitar los botones para subir/bajar fecha
        self.view.DT_nacimiento.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

    def load_combos(self):
        tipos = self.huesped_model.get_tipos_documento()
        self.view.CB_tipo_d.clear()
        for id_tipo, nombre in tipos:
            self.view.CB_tipo_d.addItem(nombre, id_tipo)

    def setup_connections(self):
        self.view.PB_registrar.clicked.connect(self.registrar)
        self.view.PB_salir.clicked.connect(self.window.close)

    def registrar(self):
        id_tipo_doc = self.view.CB_tipo_d.currentData()
        tipo_doc_texto = self.view.CB_tipo_d.currentText()
        numero_doc = self.view.LE_numero_d.text().strip()
        nombres = self.view.LE_nombres.text().strip().upper()
        apellidos = self.view.LE_apellidos.text().strip().upper()
        contacto = self.view.LE_contacto.text().strip()
        email = self.view.LE_correo.text().strip().lower()
        fecha_nacimiento = self.view.DT_nacimiento.date().toPyDate()

        # Validación Capa 1: Campos vacíos
        if not all([numero_doc, nombres, apellidos, contacto, email]):
            QMessageBox.warning(self.window, "Error de Validación", "Por favor, complete todos los campos obligatorios.")
            return

        # Validación Capa 2: Formato de DNI (REQ-03)
        if tipo_doc_texto == 'DNI':
            if not numero_doc.isdigit() or len(numero_doc) != 8:
                QMessageBox.warning(self.window, "Error de Formato", "El DNI debe contener exactamente 8 dígitos numéricos.")
                return

        # Validación Capa 3: Formato de Correo Electrónico
        patron_correo = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(patron_correo, email):
            QMessageBox.warning(self.window, "Error de Formato", "Ingrese un correo electrónico válido (ejemplo: usuario@correo.com).")
            return
        
        # (Se eliminó la validación de edad >= 18 ya que la fecha está bloqueada a la del día del equipo)

        # Inserción en Base de Datos
        if self.huesped_model.create_huesped(id_tipo_doc, numero_doc, nombres, apellidos, contacto, email, fecha_nacimiento):
            QMessageBox.information(self.window, "Éxito", f"Huésped {nombres} {apellidos} registrado correctamente.")
            self.window.close()
        else:
            QMessageBox.critical(self.window, "Error SQL", "No se pudo registrar el huésped. Verifique si el documento ya existe en el sistema.")