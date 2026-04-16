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

                                                                    
        self._timer_notif = QtCore.QTimer()
        self._timer_notif.timeout.connect(self._actualizar_badge_notificaciones)
        self._timer_notif.start(60_000)
        self._actualizar_badge_notificaciones()                         

    def show(self):
        self.window.show()

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

        if rol_id == 2:                    
            self.view.PB_registrar_u.hide()
            self.view.PB_reporte.hide()
        elif rol_id == 3:                     
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
        
                                                    
        self.view.label_14.mousePressEvent = self.mostrar_perfil
        self.view.label_14.setCursor(QtCore.Qt.PointingHandCursor)

    def mostrar_perfil(self, event):
        from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QWidget, QLineEdit, QComboBox, QFormLayout
        from PyQt5.QtGui import QFont, QColor
        from PyQt5.QtCore import Qt
        from src.controllers.login_controller import LoginController
        from src.models.user_model import UserModel
        
        is_admin = self.user_data.get('id_rol', 1) == 1
        user_model = UserModel()
        
        dlg = QDialog(self.window)
        dlg.setWindowTitle("👤 Perfil de Usuario")
        
        if is_admin:
            dlg.setFixedSize(900, 450)
            main_layout = QHBoxLayout(dlg)
            col_perfil = QVBoxLayout()
            col_admin = QVBoxLayout()
            main_layout.addLayout(col_perfil, 1)
            main_layout.addLayout(col_admin, 3)
        else:
            dlg.setFixedSize(320, 240)
            col_perfil = QVBoxLayout(dlg)
            
        dlg.setStyleSheet("""
            QDialog { background-color: #F8F9F9; }
            QLabel { color: #2C3E50; }
            QTableWidget { font-family: 'Segoe UI'; background: white; }
            QHeaderView::section { background-color: #2C3E50; color: white; font-weight: bold; padding: 4px; }
        """)
        
        col_perfil.setSpacing(15)
        lbl_titulo = QLabel("TU CUENTA")
        lbl_titulo.setFont(QFont("Berlin Sans FB", 14, QFont.Bold))
        lbl_titulo.setAlignment(Qt.AlignCenter)
        col_perfil.addWidget(lbl_titulo)
        
        nombre = self.user_data.get('nombre', 'Administrador')
        email = self.user_data.get('email', 'admin@hotel.com')
        rol = self._nombre_rol(self.user_data.get('id_rol', 1))
        
        def _add_fila(texto):
            lbl = QLabel(texto)
            lbl.setFont(QFont("Segoe UI", 11))
            col_perfil.addWidget(lbl)
            
        _add_fila(f"<b>Nombre:</b> {nombre}")
        _add_fila(f"<b>Usuario:</b> {email}")
        _add_fila(f"<b>Rol Nivel:</b> {rol}")
        col_perfil.addStretch()
        
        btn_logout = QPushButton("CERRAR SESIÓN")
        btn_logout.setCursor(Qt.PointingHandCursor)
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
            self.login_window = LoginController()
            self.login_window.show()
            
        btn_logout.clicked.connect(logout)
        col_perfil.addWidget(btn_logout)
        
        if is_admin:
            lbl_admin = QLabel("GESTIÓN DE USUARIOS")
            lbl_admin.setFont(QFont("Berlin Sans FB", 14, QFont.Bold))
            col_admin.addWidget(lbl_admin)
            
            tb_users = QTableWidget()
            tb_users.setColumnCount(6)
            tb_users.setHorizontalHeaderLabels(["ID", "Nombre", "Email", "Rol", "Estado", "Acción"])
            tb_users.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
            tb_users.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
            tb_users.setEditTriggers(QTableWidget.NoEditTriggers)
            tb_users.setSelectionBehavior(QTableWidget.SelectRows)
            col_admin.addWidget(tb_users)
            
            def refrescar_tabla():
                tb_users.setRowCount(0)
                usuarios = user_model.get_all_users()
                for usr in usuarios:
                    row = tb_users.rowCount()
                    tb_users.insertRow(row)
                    
                    id_item = QTableWidgetItem(str(usr['id']))
                    id_item.setTextAlignment(Qt.AlignCenter)
                    nom_item = QTableWidgetItem(usr['nombre'])
                    mail_item = QTableWidgetItem(usr['email'])
                    rol_item = QTableWidgetItem(usr['rol'])
                    
                    estado_str = "Activo" if usr['activo'] else "Inactivo"
                    est_item = QTableWidgetItem(estado_str)
                    est_item.setTextAlignment(Qt.AlignCenter)
                    
                    if not usr['activo']:
                        rojo = QColor("#FADBD8")
                        for it in (id_item, nom_item, mail_item, rol_item, est_item):
                            it.setBackground(rojo)
                            
                    tb_users.setItem(row, 0, id_item)
                    tb_users.setItem(row, 1, nom_item)
                    tb_users.setItem(row, 2, mail_item)
                    tb_users.setItem(row, 3, rol_item)
                    tb_users.setItem(row, 4, est_item)
                    
                    w_acciones = QWidget()
                    l_acciones = QHBoxLayout(w_acciones)
                    l_acciones.setContentsMargins(0, 0, 0, 0)
                    
                    btn_edit = QPushButton("✏️")
                    btn_edit.setToolTip("Editar usuario")
                    btn_edit.setCursor(Qt.PointingHandCursor)
                    btn_edit.clicked.connect(lambda _, u=usr: abrir_editar(u))
                    
                    btn_toggle = QPushButton("🔴" if usr['activo'] else "🟢")
                    btn_toggle.setToolTip("Desactivar" if usr['activo'] else "Activar")
                    btn_toggle.setCursor(Qt.PointingHandCursor)
                    btn_toggle.clicked.connect(lambda _, u=usr: toggle_estado(u))
                    
                    if usr['id'] == self.user_data.get('id'):
                        btn_toggle.setEnabled(False)
                        btn_toggle.setToolTip("No puedes desactivarte a ti mismo")
                        
                    l_acciones.addWidget(btn_edit)
                    l_acciones.addWidget(btn_toggle)
                    tb_users.setCellWidget(row, 5, w_acciones)
                    
            def toggle_estado(usr):
                nuevo = not usr['activo']
                if user_model.toggle_user_status(usr['id'], nuevo):
                    refrescar_tabla()
            
            def abrir_editar(usr):
                mod_dlg = QDialog(dlg)
                mod_dlg.setWindowTitle(f"Editar Usuario #{usr['id']}")
                mod_dlg.setFixedSize(350, 250)
                flay = QFormLayout(mod_dlg)
                
                le_nom = QLineEdit(usr['nombre'])
                le_email = QLineEdit(usr['email'])
                
                cb_rol = QComboBox()
                roles = user_model.get_roles()
                for r in roles:
                    cb_rol.addItem(r[1], r[0])
                idx = cb_rol.findData(usr['id_rol'])
                if idx >= 0: cb_rol.setCurrentIndex(idx)
                
                le_pass = QLineEdit()
                le_pass.setPlaceholderText("Dejar en blanco para no cambiar")
                le_pass.setEchoMode(QLineEdit.Password)
                
                flay.addRow("Nombre:", le_nom)
                flay.addRow("Email:", le_email)
                flay.addRow("Rol:", cb_rol)
                flay.addRow("Nueva Contraseña:", le_pass)
                
                btn_box = QHBoxLayout()
                btn_save = QPushButton("Guardar")
                btn_save.clicked.connect(lambda: guardar_cambios(usr['id'], le_nom.text(), le_email.text(), cb_rol.currentData(), le_pass.text(), mod_dlg))
                btn_cancel = QPushButton("Cancelar")
                btn_cancel.clicked.connect(mod_dlg.reject)
                btn_box.addWidget(btn_cancel)
                btn_box.addWidget(btn_save)
                
                flay.addRow(btn_box)
                mod_dlg.exec_()
                
            def guardar_cambios(id_u, n, e, id_r, p, mdlg):
                from PyQt5.QtWidgets import QMessageBox
                if not n.strip() or not e.strip():
                    QMessageBox.warning(mdlg, "Error", "Nombre y correo son requeridos.")
                    return
                if user_model.update_user_details_admin(id_u, n, e, id_r, p if p else None):
                    QMessageBox.information(mdlg, "Éxito", "Usuario actualizado.")
                    mdlg.accept()
                    refrescar_tabla()
                else:
                    QMessageBox.critical(mdlg, "Error", "No se pudo actualizar.")
                    
            refrescar_tabla()
            
        dlg.exec_()

                                                                          
                                                                           
                                                                          
    def _actualizar_badge_notificaciones(self):
        """REQ-07: Genera notificaciones automáticas y actualiza el tooltip del botón."""
        try:
            self._notif_model.generar_notificaciones()
            total = self._notif_model.contar_notificaciones_hoy()
            if total > 0:
                self.view.PB_notificaciones.setToolTip(
                    f"🔔 {total} notificación(es) hoy — haz clic para ver"
                )
                                                                        
                self.view.PB_notificaciones.setStyleSheet(
                    "QPushButton { background-color: #E74C3C; border-radius: 5px; }"
                    "QPushButton:hover { background-color: #C0392B; }"
                )
            else:
                self.view.PB_notificaciones.setToolTip("Sin notificaciones nuevas")
                self.view.PB_notificaciones.setStyleSheet("")
        except Exception as e:
            print(f"Error al actualizar badge: {e}")

                                                                          
                                                                           
                                                                          
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