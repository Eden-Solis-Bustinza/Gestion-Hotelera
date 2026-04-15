from src.models.user_model import UserModel
from PyQt5.QtWidgets import QMessageBox

class RecuperaController:
    def __init__(self, view):
        self.view = view
        self.user_model = UserModel()
        self.load_combos()
        self.setup_connections()

    def load_combos(self):
        preguntas = self.user_model.get_preguntas_seguridad()
        for id_pregunta, pregunta in preguntas:
            self.view.CB_pregunta_s.addItem(pregunta, id_pregunta)

    def setup_connections(self):
        self.view.PB_confirmar.clicked.connect(self.confirmar)

    def confirmar(self):
        email = self.view.LE_correo.text().strip()
        id_pregunta = self.view.CB_pregunta_s.currentData()
        respuesta = self.view.LE_respuesta.text().strip()
        password = self.view.LE_contrasena.text()
        confirm_password = self.view.LE_cocontrasena.text()

        if not all([email, respuesta, password, confirm_password]):
            QMessageBox.warning(self.view, "Error", "Por favor, complete todos los campos.")
            return

        if password != confirm_password:
            QMessageBox.warning(self.view, "Error", "Las contraseñas no coinciden.")
            return

        if self.user_model.update_password(email, id_pregunta, respuesta, password):
            QMessageBox.information(self.view, "Éxito", "Contraseña actualizada correctamente.")
            self.view.close()
        else:
            QMessageBox.critical(self.view, "Error", "Los datos de seguridad no coinciden con nuestros registros.")
