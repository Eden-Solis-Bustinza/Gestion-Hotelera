from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from src.views.FrmDashboard import Ui_MainWindow
from src.controllers.habitaciones_controller import HabitacionesController
from src.controllers.checkin_controller import CheckinController
from src.controllers.registrar_huesped_controller import RegistrarHuespedController
from src.controllers.crear_reserva_controller import CrearReservaController
from src.controllers.checkout_controller import CheckoutController
from src.controllers.productos_controller import ProductosController
from src.controllers.registro_controller import RegistroController
from src.controllers.notificaciones_controller import NotificacionesController
from src.controllers.reporte_controller import ReporteController
from src.controllers.backup_controller import BackupController
from src.models.notificacion_model import NotificacionModel


class DashboardController:
    def __init__(self, user_data):
        self.window = QtWidgets.QMainWindow()
        self.view = Ui_MainWindow()
        self.view.setupUi(self.window)

        self.user_data = user_data
        self._notif_model = NotificacionModel()

        self.window.setWindowState(QtCore.Qt.WindowMaximized)
        self.window.setWindowTitle("🏨 Sistema de Gestión Hotelera")

        self.aplicar_seguridad_roles()
        self.setup_connections()

        # Timer: revisar notificaciones cada 60 s y actualizar badge
        self._timer_notif = QtCore.QTimer()
        self._timer_notif.timeout.connect(self._actualizar_badge_notificaciones)
        self._timer_notif.start(60_000)
        self._actualizar_badge_notificaciones()   # primera vez al abrir

    def show(self):
        self.window.show()

    # ------------------------------------------------------------------ #
    #  REQ-01: Control de acceso por rol                                  #
    # ------------------------------------------------------------------ #
    def aplicar_seguridad_roles(self):
        """
        Roles:
          1 = Administración  → acceso total
          2 = Recepción       → ocultar Registrar Usuario y Reportes
          3 = Contabilidad    → solo Reportes y Backup (no operaciones)
        """
        rol_id = self.user_data.get('id_rol', 1)
        nombre = self.user_data.get('nombre', 'Usuario')

        self.window.setWindowTitle(f"🏨 Hotel — {nombre}  [Rol: {self._nombre_rol(rol_id)}]")

        if rol_id == 2:         # Recepción
            self.view.PB_registrar_u.hide()
            self.view.PB_reporte.hide()
        elif rol_id == 3:       # Contabilidad
            self.view.PB_habitacion.hide()
            self.view.PB_checkin.hide()
            self.view.PB_checkout.hide()
            self.view.PB_registrar_u.hide()
            self.view.PB_registro_h.hide()
            self.view.PB_reserva.hide()
            self.view.PB_producto.hide()

    @staticmethod
    def _nombre_rol(id_rol):
        return {1: "Administración", 2: "Recepción", 3: "Contabilidad"}.get(id_rol, "Desconocido")

    # ------------------------------------------------------------------ #
    #  Conexiones de botones                                              #
    # ------------------------------------------------------------------ #
    def setup_connections(self):
        self.view.PB_habitacion.clicked.connect(self.show_habitaciones)
        self.view.PB_registro_h.clicked.connect(self.show_huespedes)
        self.view.PB_reserva.clicked.connect(self.show_reservas)
        self.view.PB_producto.clicked.connect(self.show_productos)
        self.view.PB_checkin.clicked.connect(self.show_checkin)
        self.view.PB_checkout.clicked.connect(self.show_checkout)
        self.view.PB_reporte.clicked.connect(self.show_reportes)
        self.view.PB_registrar_u.clicked.connect(self.show_registrar_usuario)
        self.view.PB_notificaciones.clicked.connect(self.show_notificaciones)
        
        # Conectar el ícono de la persona (label_14)
        self.view.label_14.mousePressEvent = self.mostrar_perfil
        self.view.label_14.setCursor(QtCore.Qt.PointingHandCursor)

    def mostrar_perfil(self, event):
        from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
        from PyQt5.QtGui import QFont
        from src.controllers.login_controller import LoginController
        
        dlg = QDialog(self.window)
        dlg.setWindowTitle("👤 Perfil de Usuario")
        dlg.setFixedSize(320, 240)
        dlg.setStyleSheet("""
            QDialog { background-color: #F8F9F9; }
            QLabel { color: #2C3E50; }
        """)
        
        layout = QVBoxLayout(dlg)
        layout.setSpacing(15)
        
        lbl_titulo = QLabel("TU CUENTA")
        lbl_titulo.setFont(QFont("Berlin Sans FB", 14, QFont.Bold))
        lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lbl_titulo)
        
        nombre = self.user_data.get('nombre', 'Administrador')
        email = self.user_data.get('email', 'admin@hotel.com')
        rol = self._nombre_rol(self.user_data.get('id_rol', 1))
        
        def _add_fila(texto):
            lbl = QLabel(texto)
            lbl.setFont(QFont("Segoe UI", 11))
            layout.addWidget(lbl)
            
        _add_fila(f"<b>Nombre:</b> {nombre}")
        _add_fila(f"<b>Usuario:</b> {email}")
        _add_fila(f"<b>Rol Nivel:</b> {rol}")
        
        layout.addStretch()
        
        btn_logout = QPushButton("CERRAR SESIÓN")
        btn_logout.setCursor(QtCore.Qt.PointingHandCursor)
        btn_logout.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C; color: white; font-weight: bold; 
                padding: 10px; border-radius: 5px; font-family: 'Berlin Sans FB';
            }
            QPushButton:hover { background-color: #C0392B; }
        """)
        
        def logout():
            dlg.accept()
            self.window.close()
            # Resetear e ir al Login
            self.login_window = LoginController()
            self.login_window.show()
            
        btn_logout.clicked.connect(logout)
        layout.addWidget(btn_logout)
        
        dlg.exec_()

    # ------------------------------------------------------------------ #
    #  Badge de notificaciones                                            #
    # ------------------------------------------------------------------ #
    def _actualizar_badge_notificaciones(self):
        """REQ-07: Genera notificaciones automáticas y actualiza el tooltip del botón."""
        try:
            self._notif_model.generar_notificaciones()
            total = self._notif_model.contar_notificaciones_hoy()
            if total > 0:
                self.view.PB_notificaciones.setToolTip(
                    f"🔔 {total} notificación(es) hoy — haz clic para ver"
                )
                # Efecto visual: resaltar el botón si hay notificaciones
                self.view.PB_notificaciones.setStyleSheet(
                    "QPushButton { background-color: #E74C3C; border-radius: 5px; }"
                    "QPushButton:hover { background-color: #C0392B; }"
                )
            else:
                self.view.PB_notificaciones.setToolTip("Sin notificaciones nuevas")
                self.view.PB_notificaciones.setStyleSheet("")
        except Exception as e:
            print(f"Error al actualizar badge: {e}")

    # ------------------------------------------------------------------ #
    #  Enrutamiento de módulos                                            #
    # ------------------------------------------------------------------ #
    def show_habitaciones(self):
        from src.views.FrmHabitaciones import Ui_Dialog
        view = Ui_Dialog()
        self.habitaciones_ctrl = HabitacionesController(view)
        self.habitaciones_ctrl.show()

    def show_checkin(self):
        self.checkin_ctrl = CheckinController(self.user_data)
        self.checkin_ctrl.show()

    def show_huespedes(self):
        self.huespedes_ctrl = RegistrarHuespedController()
        self.huespedes_ctrl.show()

    def show_reservas(self):
        self.reservas_ctrl = CrearReservaController(self.user_data)
        self.reservas_ctrl.show()

    def show_productos(self):
        self.productos_ctrl = ProductosController(self.user_data)
        self.productos_ctrl.show()

    def show_checkout(self):
        self.checkout_ctrl = CheckoutController(self.user_data)
        self.checkout_ctrl.show()

    def show_reportes(self):
        """REQ-10: Módulo de reportes de ocupación e ingresos."""
        self.reporte_ctrl = ReporteController(self.user_data)
        self.reporte_ctrl.show()

    def show_registrar_usuario(self):
        self.registro_user_ctrl = RegistroController()
        self.registro_user_ctrl.show()

    def show_notificaciones(self):
        """REQ-07: Panel de notificaciones con auto-refresco."""
        self.notif_ctrl = NotificacionesController(self.user_data)
        self.notif_ctrl.show()

    def show_backup(self):
        """REQ-14: Módulo de respaldo (accesible desde menú si se implementa)."""
        self.backup_ctrl = BackupController(self.user_data)
        self.backup_ctrl.show()