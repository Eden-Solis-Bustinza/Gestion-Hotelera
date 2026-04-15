from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from src.views.FrmNotificaciones import Ui_Dialog
from src.models.notificacion_model import NotificacionModel


                                        
COLOR_MAP = {
    "ReservaProxima":    "#AED6F1",                           
    "HabitacionLimpia":  "#16A085",                             
    "CheckoutPendiente": "#F1948A",                            
    "Otro":              "#F8C471",                    
}

                                            
SLOTS = [
    ("LE_tipo1", "LE_mensaje1", "LE_fyh1", "L_disponible"),
    ("LE_tipo2", "LE_mensaje2", "LE_fyh2", "L_reservado"),
    ("LE_tipo3", "LE_mensaje3", "LE_fyh3", "L_ocupado"),
    ("LE_tipo4", "LE_mensaje4", "LE_fyh4", "L_limyman"),
]


class NotificacionesController:
    def __init__(self, user_data):
        self.window = QtWidgets.QDialog()
        self.view = Ui_Dialog()
        self.view.setupUi(self.window)

        self.user_data = user_data
        self.model = NotificacionModel()

        self.window.setWindowTitle("🔔 Notificaciones del Sistema")
        self.window.setMinimumSize(840, 478)
        self.window.setMaximumSize(16777215, 16777215)                        
        self.window.setWindowState(QtCore.Qt.WindowMaximized)

                                                                
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.cargar_notificaciones)
        self.timer.start(60_000)

        self.cargar_notificaciones()

    def show(self):
        self.window.exec_()
        self.timer.stop()

    def cargar_notificaciones(self):
        """Genera nuevas notificaciones y las muestra en los 4 slots de la UI."""
                                              
        self.model.generar_notificaciones()

                                   
        notificaciones = self.model.get_notificaciones(limit=4)

                          
        for (le_tipo, le_msg, le_fyh, lbl_color) in SLOTS:
            getattr(self.view, le_tipo).clear()
            getattr(self.view, le_msg).clear()
            getattr(self.view, le_fyh).clear()
            getattr(self.view, lbl_color).setStyleSheet("QLabel { background-color: #D5DBDB; }")

                                      
        for i, notif in enumerate(notificaciones[:4]):
            le_tipo, le_msg, le_fyh, lbl_color = SLOTS[i]
            color = COLOR_MAP.get(notif["tipo"], "#F8C471")

            getattr(self.view, le_tipo).setText(notif["tipo"])
            getattr(self.view, le_msg).setText(notif["mensaje"])
            getattr(self.view, le_fyh).setText(notif["fecha"])
            getattr(self.view, lbl_color).setStyleSheet(
                f"QLabel {{ background-color: {color}; border-radius: 3px; }}"
            )

                                                        
        total = self.model.contar_notificaciones_hoy()
        self.window.setWindowTitle(f"🔔 Notificaciones del Sistema  ({total} hoy)")
