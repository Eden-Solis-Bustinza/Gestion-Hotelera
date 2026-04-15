from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (
    QMessageBox, QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QLineEdit, QFormLayout, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from src.models.room_model import RoomModel


                               
COLOR_MAP = {
    1: "#16A085",                        
    2: "#F1948A",                       
    3: "#AED6F1",                       
    4: "#F8C471",                            
}


class HabitacionesController:
    def __init__(self, view):
        self.window = QtWidgets.QDialog()
        self.view = view
        self.view.setupUi(self.window)

        self.room_model = RoomModel()
        self._rooms_data = []                                  

        self.window.setWindowState(QtCore.Qt.WindowMaximized)

        self.load_rooms()
        self.setup_connections()

    def show(self):
        self.window.exec_()

    def load_rooms(self):
        """Genera dinámicamente todos los frames de las habitaciones.
        Añade los botones explícitos para cambiar el estado."""
        self._rooms_data = self.room_model.get_all_rooms()

        grid = self.view.gridLayout

                                                                  
        if hasattr(self, '_dynamic_frames'):
            for frame in self._dynamic_frames:
                grid.removeWidget(frame)
                frame.deleteLater()
        self._dynamic_frames = []

                                                           
        for frame_name in ["F_habitacion_1", "F_habitacion_2", "F_habitacion_3"]:
            frame = getattr(self.view, frame_name, None)
            if frame:
                frame.hide()
        
                                                                                     
        if hasattr(self.view, "F_agregar"):
            grid.removeWidget(self.view.F_agregar)

                                      
        for idx, room in enumerate(self._rooms_data):
            color = COLOR_MAP.get(room['id_estado'], "#16A085")
            self._crear_frame_extra(room, color, idx)

                                                                            
        idx_agregar = len(self._rooms_data)
        if hasattr(self.view, "F_agregar"):
            self.view.F_agregar.show()
            row_grid = idx_agregar // 2
            col_grid = idx_agregar % 2
            grid.addWidget(self.view.F_agregar, row_grid, col_grid)

    def _crear_frame_extra(self, room, color, idx):
        """Crea un QFrame dinámico para cada habitación con botón de cambio."""
        grid = self.view.gridLayout

        frame = QtWidgets.QFrame(self.view.SAWC_interfaz_a_h)
        frame.setMinimumSize(250, 260)
        frame.setMaximumSize(250, 260)
        frame.setStyleSheet(f"QFrame {{ background-color: {color}; border-radius: 10px; }}")
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(10, 10, 10, 10)

                    
        lbl_icon = QLabel()
        lbl_icon.setPixmap(
            QtGui.QPixmap("assets/icons/cama.png").scaled(65, 65, Qt.KeepAspectRatio)
        )
        lbl_icon.setAlignment(Qt.AlignCenter)
        lbl_icon.setStyleSheet("background-color: transparent; border: none;")
        layout.addWidget(lbl_icon)

                           
        lbl_titulo = QLabel(f"HABITACIÓN - {room['numero']}")
        lbl_titulo.setAlignment(Qt.AlignCenter)
        lbl_titulo.setStyleSheet("background-color: transparent; border: none; color: white; font-size: 11pt; font-weight: bold;")
        layout.addWidget(lbl_titulo)

                       
        for lbl_text, val in [("Tipo:", room['tipo']), ("Estado:", room['estado'])]:
            h = QHBoxLayout()
            lbl = QLabel(lbl_text)
            lbl.setStyleSheet("color: white; background-color: transparent; border: none; font-size: 9pt;")
            le = QLineEdit(val)
            le.setReadOnly(True)
            le.setStyleSheet("border: 1px solid #ffffff; border-radius: 4px; padding: 2px; background-color: rgba(255,255,255,0.2); color: white; font-size: 9pt;")
            h.addWidget(lbl)
            h.addWidget(le)
            layout.addLayout(h)

                                           
        btn_estado = QPushButton("🔄 Cambiar Estado")
        btn_estado.setStyleSheet("""
            QPushButton { 
                background-color: #2C3E50; color: white; border-radius: 5px; 
                padding: 6px; margin-top: 5px; font-weight: bold; 
            } 
            QPushButton:hover { background-color: #34495E; }
        """)
        btn_estado.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        btn_estado.clicked.connect(lambda checked=False, r=room: self.editar_habitacion(r))
        layout.addWidget(btn_estado)

        self._dynamic_frames.append(frame)
        
        row_grid = idx // 2
        col_grid = idx % 2
        grid.addWidget(frame, row_grid, col_grid)

                                                                          
                                                                           
                                                                          
    def setup_connections(self):
        if hasattr(self.view, 'PB_agregar_h'):
            self.view.PB_agregar_h.clicked.connect(self.abrir_dialogo_agregar)

                                                                          
                                                                           
                                                                          
    def editar_habitacion(self, room):
        """REQ-02: Diálogo para cambiar el estado de la habitación."""
        dlg = QDialog(self.window)
        dlg.setWindowTitle(f"Editar Habitación {room['numero']}")
        dlg.setMinimumSize(350, 280)
        dlg.setStyleSheet("""
            QDialog { background-color: #EBEDEF; }
            QLabel { font-family: 'Berlin Sans FB'; color: #2C3E50; }
            QPushButton {
                background-color: #2C3E50; color: white; border-radius: 5px;
                font-weight: bold; padding: 8px; font-family: 'Berlin Sans FB';
            }
            QPushButton:hover { background-color: #16A085; }
            QComboBox { border: 2px solid #D5DBDB; border-radius: 5px; padding: 5px; background: white; }
            QLineEdit { border: 2px solid #D5DBDB; border-radius: 5px; padding: 5px; background: white; }
        """)

        layout = QVBoxLayout(dlg)
        layout.setContentsMargins(20, 20, 20, 20)

              
        lbl_info = QLabel(
            f"<b>Habitación:</b> {room['numero']}<br>"
            f"<b>Tipo:</b> {room['tipo']}<br>"
            f"<b>Tarifa:</b> S/. {room.get('tarifa_base', 0):.2f}/noche"
        )
        lbl_info.setFont(QFont("Berlin Sans FB", 10))
        layout.addWidget(lbl_info)

        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setStyleSheet("color: #2C3E50;")
        layout.addWidget(sep)

                          
        form = QFormLayout()
        cb_estado = QComboBox()
        estados = self.room_model.get_estados_habitacion()
        for id_e, nombre_e in estados:
            cb_estado.addItem(nombre_e, id_e)
            if id_e == room['id_estado']:
                cb_estado.setCurrentIndex(cb_estado.count() - 1)
        form.addRow("Nuevo estado:", cb_estado)
        layout.addLayout(form)

                 
        btn_layout = QHBoxLayout()
        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.setStyleSheet("background-color: #7F8C8D;")
        btn_cancelar.clicked.connect(dlg.reject)
        btn_guardar = QPushButton("Guardar")
        btn_guardar.clicked.connect(lambda: self._guardar_estado(
            room['id_habitacion'], cb_estado.currentData(), dlg
        ))
        btn_layout.addWidget(btn_cancelar)
        btn_layout.addWidget(btn_guardar)
        layout.addLayout(btn_layout)

        dlg.exec_()

    def _guardar_estado(self, id_habitacion, nuevo_estado_id, dlg):
        ok = self.room_model.update_room_status(id_habitacion, nuevo_estado_id)
        if ok:
            QMessageBox.information(dlg, "✅", "Estado actualizado correctamente.")
            dlg.accept()
            self.load_rooms()                    
        else:
            QMessageBox.critical(dlg, "Error", "No se pudo actualizar el estado.")

    def abrir_dialogo_agregar(self):
        """REQ-02: Diálogo para registrar una nueva habitación."""
        dlg = QDialog(self.window)
        dlg.setWindowTitle("Registrar Nueva Habitación")
        dlg.setMinimumSize(360, 260)
        dlg.setStyleSheet("""
            QDialog { background-color: #EBEDEF; }
            QLabel { font-family: 'Berlin Sans FB'; color: #2C3E50; }
            QPushButton {
                background-color: #2C3E50; color: white; border-radius: 5px;
                font-weight: bold; padding: 8px; font-family: 'Berlin Sans FB';
            }
            QPushButton:hover { background-color: #16A085; }
            QComboBox, QLineEdit {
                border: 2px solid #D5DBDB; border-radius: 5px; padding: 5px; background: white;
            }
        """)

        layout = QVBoxLayout(dlg)
        layout.setContentsMargins(20, 20, 20, 20)

        titulo = QLabel("Nueva Habitación")
        titulo.setFont(QFont("Berlin Sans FB", 13, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)

        form = QFormLayout()
        le_numero = QLineEdit()
        le_numero.setPlaceholderText("Ej: 201")
        form.addRow("Número:", le_numero)

        cb_tipo = QComboBox()
        tipos = self.room_model.get_tipos_habitacion()
        for id_t, nombre_t, tarifa in tipos:
            cb_tipo.addItem(f"{nombre_t}  (S/. {tarifa:.2f}/noche)", id_t)
        form.addRow("Tipo:", cb_tipo)

        le_obs = QLineEdit()
        le_obs.setPlaceholderText("Observaciones (opcional)")
        form.addRow("Observaciones:", le_obs)

        layout.addLayout(form)

        btn_layout = QHBoxLayout()
        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.setStyleSheet("background-color: #7F8C8D;")
        btn_cancelar.clicked.connect(dlg.reject)
        btn_guardar = QPushButton("Registrar")
        btn_guardar.clicked.connect(lambda: self._guardar_nueva(
            le_numero.text(), cb_tipo.currentData(), le_obs.text(), dlg
        ))
        btn_layout.addWidget(btn_cancelar)
        btn_layout.addWidget(btn_guardar)
        layout.addLayout(btn_layout)

        dlg.exec_()

    def _guardar_nueva(self, numero, id_tipo, obs, dlg):
        if not numero.strip():
            QMessageBox.warning(dlg, "Error", "Ingrese el número de habitación.")
            return
        if not id_tipo:
            QMessageBox.warning(dlg, "Error", "Seleccione el tipo de habitación.")
            return

        ok, msg = self.room_model.crear_habitacion(numero, id_tipo, obs)
        if ok:
            QMessageBox.information(dlg, "✅ Éxito", msg)
            dlg.accept()
            self.load_rooms()
        else:
            QMessageBox.critical(dlg, "❌ Error", msg)
