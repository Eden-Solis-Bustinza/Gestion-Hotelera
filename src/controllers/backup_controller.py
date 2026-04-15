from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QTableWidget, QTableWidgetItem,
    QLineEdit, QFileDialog, QGroupBox, QHeaderView, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from src.models.backup_model import BackupModel
import os


class BackupController:

    def __init__(self, user_data):
        self.user_data = user_data
        self.model = BackupModel()

        self.window = QDialog()
        self.window.setWindowTitle("💾 Respaldo de Base de Datos")
        self.window.setMinimumSize(800, 500)
        self.window.setWindowState(QtCore.Qt.WindowMaximized)
        self.window.setStyleSheet("""
            QDialog { background-color: #EBEDEF; }
            QGroupBox {
                font-family: 'Berlin Sans FB'; font-size: 11pt;
                border: 2px solid #2C3E50; border-radius: 8px;
                margin-top: 10px; padding: 6px;
            }
            QGroupBox::title { subcontrol-origin: margin; left: 12px; padding: 0 4px; color: #2C3E50; }
            QPushButton {
                background-color: #2C3E50; color: white; border-radius: 5px;
                font-weight: bold; padding: 8px 16px; font-family: 'Berlin Sans FB';
            }
            QPushButton:hover { background-color: #16A085; }
            QLineEdit {
                border: 2px solid #D5DBDB; border-radius: 5px;
                padding: 5px; background: white; font-family: 'Berlin Sans FB';
            }
            QTableWidget { background: white; font-family: 'Berlin Sans FB'; }
            QHeaderView::section {
                background-color: #2C3E50; color: white;
                padding: 6px; font-weight: bold;
            }
        """)
        self._build_ui()

    def _build_ui(self):
        main = QVBoxLayout(self.window)
        main.setContentsMargins(20, 20, 20, 20)
        main.setSpacing(14)

                
        titulo = QLabel("RESPALDO DE BASE DE DATOS — SQL Server")
        titulo.setFont(QFont("Berlin Sans FB", 15, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color: #2C3E50;")
        main.addWidget(titulo)

                                   
        gb_nuevo = QGroupBox("Ejecutar nuevo respaldo")
        gb_lay = QHBoxLayout(gb_nuevo)

        lbl_ruta = QLabel("Carpeta destino:")
        lbl_ruta.setFont(QFont("Berlin Sans FB", 10))
        gb_lay.addWidget(lbl_ruta)

        self.LE_ruta = QLineEdit()
        self.LE_ruta.setPlaceholderText("Selecciona la carpeta donde guardar el .bak")
        self.LE_ruta.setText(os.path.expanduser("~\\Desktop"))
        gb_lay.addWidget(self.LE_ruta)

        btn_explorar = QPushButton("📁  Explorar")
        btn_explorar.setStyleSheet("background-color: #7F8C8D;")
        btn_explorar.clicked.connect(self.seleccionar_carpeta)
        gb_lay.addWidget(btn_explorar)

        self.PB_backup = QPushButton("⬆  GENERAR BACKUP")
        self.PB_backup.clicked.connect(self.ejecutar_backup)
        gb_lay.addWidget(self.PB_backup)

        main.addWidget(gb_nuevo)

                             
        gb_hist = QGroupBox("Historial de respaldos")
        hist_lay = QVBoxLayout(gb_hist)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["ID", "Fecha", "Ruta", "Estado", "Usuario"])
        self.tabla.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabla.setAlternatingRowColors(True)
        self.tabla.setStyleSheet("alternate-background-color: #F8F9F9;")
        hist_lay.addWidget(self.tabla)

        btn_refresh = QPushButton("🔄  Actualizar historial")
        btn_refresh.setStyleSheet("background-color: #1ABC9C;")
        btn_refresh.clicked.connect(self.cargar_historial)
        hist_lay.addWidget(btn_refresh, alignment=Qt.AlignRight)

        main.addWidget(gb_hist)

                
        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.setStyleSheet("background-color: #7F8C8D;")
        btn_cerrar.clicked.connect(self.window.close)
        h = QHBoxLayout()
        h.addStretch()
        h.addWidget(btn_cerrar)
        main.addLayout(h)

                                   
        self.cargar_historial()

    def seleccionar_carpeta(self):
        carpeta = QFileDialog.getExistingDirectory(
            self.window, "Seleccionar carpeta destino", os.path.expanduser("~")
        )
        if carpeta:
            self.LE_ruta.setText(carpeta)

    def ejecutar_backup(self):
        ruta = self.LE_ruta.text().strip()
        if not ruta or not os.path.isdir(ruta):
            QMessageBox.warning(self.window, "Error",
                                "La carpeta destino no existe o no es válida.")
            return

        self.PB_backup.setEnabled(False)
        self.PB_backup.setText("⏳  Generando backup...")

        id_usuario = self.user_data.get("id", 1)
        exito, resultado = self.model.ejecutar_backup(ruta, id_usuario)

        self.PB_backup.setEnabled(True)
        self.PB_backup.setText("⬆  GENERAR BACKUP")

        if exito:
            QMessageBox.information(
                self.window, "✅ Backup exitoso",
                f"Respaldo generado correctamente en:\n{resultado}"
            )
        else:
            QMessageBox.critical(
                self.window, "❌ Error en backup",
                f"No se pudo generar el respaldo:\n{resultado}"
            )

        self.cargar_historial()

    def cargar_historial(self):
        historial = self.model.get_historial_backups()
        self.tabla.setRowCount(0)

        COLOR_ESTADO = {
            "Exitoso":    "#D5F5E3",
            "Fallido":    "#FADBD8",
            "En Proceso": "#FEF9E7",
        }

        for reg in historial:
            row = self.tabla.rowCount()
            self.tabla.insertRow(row)
            valores = [
                str(reg["id"]),
                reg["fecha"],
                reg["ruta"],
                reg["estado"],
                reg["usuario"],
            ]
            color = COLOR_ESTADO.get(reg["estado"], "#FFFFFF")
            for col, val in enumerate(valores):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignCenter)
                item.setBackground(QtWidgets.QTableWidgetItem().background())
                self.tabla.setItem(row, col, item)
                self.tabla.item(row, col).setBackground(
                    QtWidgets.QApplication.palette().color(
                        QtWidgets.QPalette.Base
                    )
                )
            bg = QtCore.Qt.green if reg["estado"] == "Exitoso" else (
                 QtCore.Qt.red if reg["estado"] == "Fallido" else QtCore.Qt.yellow)
            for col in range(self.tabla.columnCount()):
                if self.tabla.item(row, col):
                    self.tabla.item(row, col).setBackground(
                        QtWidgets.QColor(color)
                    )

    def show(self):
        self.window.exec_()
