from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from src.views.FrmLogin import Ui_Dialog
from src.models.user_model import UserModel
from src.controllers.dashboard_controller import DashboardController 
from src.controllers.recupera_controller import RecuperaController

class LoginController:
    def __init__(self):
                                                     
        self.window = QtWidgets.QDialog()
        self.view = Ui_Dialog()
        self.view.setupUi(self.window)
        
        self.user_model = UserModel()
        self.setup_connections()

    def show(self):
        self.window.show()

    def setup_connections(self):
        self.view.PB_ingresar.clicked.connect(self.login)
        self.view.PB_recuperar_c.clicked.connect(self.open_recupera)

    def login(self):
        email = self.view.LE_correo.text().strip().lower()
        password = self.view.LE_contrasena.text()

        if not email or not password:
            QMessageBox.warning(self.window, "Error", "Campos vacíos.")
            return

        user = self.user_model.get_user_by_email(email)
        
        if user and self.user_model.verify_password(password, user['password_hash']):
                                                  
            self.user_model.update_last_login(user['id'])
            self.window.close()
            self.dashboard = DashboardController(user)
            self.dashboard.show()
        else:
            QMessageBox.critical(self.window, "Error", "Credenciales incorrectas.")
            self.view.LE_contrasena.clear()

    def open_recupera(self):
        self.recupera = RecuperaController()
        self.recupera.show()