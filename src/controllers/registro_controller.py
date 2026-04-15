from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from src.views.FrmRegistro import Ui_Dialog
from src.models.user_model import UserModel

class RegistroController:
    def __init__(self):
        self.window = QtWidgets.QDialog()
        self.view = Ui_Dialog()
        self.view.setupUi(self.window)
        
        self.user_model = UserModel()
        
        self.configurar_responsive()
        self.load_combos()
        self.setup_connections()

    def configurar_responsive(self):
        layout = QtWidgets.QVBoxLayout(self.window)
        if hasattr(self.view, 'label'):
            layout.addWidget(self.view.label)
            self.view.label.setScaledContents(True)
        self.window.setWindowState(QtCore.Qt.WindowMaximized)

    def show(self):
        self.window.exec_()

    def load_combos(self):
                      
        roles = self.user_model.get_roles()
        self.view.CB_roles.clear()
        for id_rol, nombre in roles:
            self.view.CB_roles.addItem(nombre, id_rol)

                                       
        preguntas = self.user_model.get_preguntas_seguridad()
        self.view.CB_pregunta_s.clear()
        for id_pregunta, pregunta in preguntas:
            self.view.CB_pregunta_s.addItem(pregunta, id_pregunta)

    def setup_connections(self):
        self.view.PB_registrar.clicked.connect(self.registrar)
        self.view.PB_iniciar_s.clicked.connect(self.window.close)

    def registrar(self):
        nombre = self.view.LE_nombres.text().strip()
        email = self.view.LE_correo.text().strip()
        id_rol = self.view.CB_roles.currentData()
        id_pregunta = self.view.CB_pregunta_s.currentData()
        respuesta = self.view.LE_respuesta.text().strip()
        password = self.view.LE_contrasena.text()
        confirm_password = self.view.LE_cocontrasena.text()

        if not all([nombre, email, respuesta, password, confirm_password]):
            QMessageBox.warning(self.window, "Error", "Por favor, complete todos los campos.")
            return

        if password != confirm_password:
            QMessageBox.warning(self.window, "Error", "Las contraseñas no coinciden.")
            return

        if self.user_model.create_user(nombre, email, password, id_rol, id_pregunta, respuesta):
            QMessageBox.information(self.window, "Éxito", "Usuario registrado correctamente.")
            self.window.close()
        else:
            QMessageBox.critical(self.window, "Error", "No se pudo registrar el usuario. El correo podría estar en uso.")
