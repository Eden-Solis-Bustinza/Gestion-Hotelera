from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (
    QMessageBox, QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTableWidget, QTableWidgetItem,
    QDateEdit, QGroupBox, QHeaderView, QFrame, QSizePolicy
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QColor
from src.models.reporte_model import ReporteModel
from datetime import datetime, timedelta


class ReporteController:
    """
    REQ-10: Reporte de Ocupación e Ingresos.
    Construye la UI completamente en código porque no existe FrmReporte diseñado.
    """

    def __init__(self, user_data):
        self.user_data = user_data
        self.model = ReporteModel()

        self.window = QDialog()
        self.window.setWindowTitle("📊 Reportes de Ocupación e Ingresos")
        self.window.setMinimumSize(1000, 650)
        self.window.setWindowState(QtCore.Qt.WindowMaximized)
        self.window.setStyleSheet("""
            QDialog { background-color: #EBEDEF; }
            QGroupBox {
                font-family: 'Berlin Sans FB'; font-size: 11pt; font-weight: bold;
                border: 2px solid #2C3E50; border-radius: 8px;
                margin-top: 10px; padding: 6px;
            }
            QGroupBox::title { subcontrol-origin: margin; left: 12px; padding: 0 4px; color: #2C3E50; }
            QLabel { font-family: 'Berlin Sans FB'; }
            QPushButton {
                background-color: #2C3E50; color: white;
                border-radius: 5px; font-weight: bold; padding: 8px 16px;
                font-family: 'Berlin Sans FB';
            }
            QPushButton:hover { background-color: #16A085; }
            QDateEdit {
                border: 2px solid #D5DBDB; border-radius: 5px;
                padding: 4px; background: white; font-family: 'Berlin Sans FB';
            }
            QTableWidget { background: white; gridline-color: #D5DBDB; font-family: 'Berlin Sans FB'; }
            QHeaderView::section {
                background-color: #2C3E50; color: white;
                padding: 6px; font-weight: bold; font-family: 'Berlin Sans FB';
            }
        """)

        self._build_ui()

                                                                          
                                                                           
                                                                          
    def _build_ui(self):
        main_layout = QVBoxLayout(self.window)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)

                                                                          
        title = QLabel("REPORTE DE OCUPACIÓN E INGRESOS")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Berlin Sans FB", 16, QFont.Bold))
        title.setStyleSheet("color: #2C3E50; margin-bottom: 6px;")
        main_layout.addWidget(title)

                                                                          
        filtro_gb = QGroupBox("Filtrar por rango de fechas")
        filtro_layout = QHBoxLayout(filtro_gb)

        filtro_layout.addWidget(QLabel("Desde:"))
        self.DE_desde = QDateEdit()
        self.DE_desde.setCalendarPopup(True)
        self.DE_desde.setDate(QDate.currentDate().addDays(-30))
        filtro_layout.addWidget(self.DE_desde)

        filtro_layout.addWidget(QLabel("Hasta:"))
        self.DE_hasta = QDateEdit()
        self.DE_hasta.setCalendarPopup(True)
        self.DE_hasta.setDate(QDate.currentDate())
        filtro_layout.addWidget(self.DE_hasta)

        self.PB_generar = QPushButton("🔍  GENERAR REPORTE")
        self.PB_generar.clicked.connect(self.generar_reporte)
        filtro_layout.addWidget(self.PB_generar)

        filtro_layout.addStretch()
        main_layout.addWidget(filtro_gb)

                                                                           
        resumen_layout = QHBoxLayout()
        self.lbl_ventas    = self._tarjeta("Comprobantes", "0",        "#2C3E50")
        self.lbl_ingresos  = self._tarjeta("Ingresos S/.", "0.00",     "#16A085")
        self.lbl_promedio  = self._tarjeta("Promedio S/.", "0.00",     "#1ABC9C")
        self.lbl_noches    = self._tarjeta("Noches vendidas", "0",     "#AED6F1")
        for frame in [self.lbl_ventas, self.lbl_ingresos, self.lbl_promedio, self.lbl_noches]:
            resumen_layout.addWidget(frame)
        main_layout.addLayout(resumen_layout)

                                                                           
        detalle_gb = QGroupBox("Detalle de Comprobantes")
        det_layout = QVBoxLayout(detalle_gb)
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(9)
        self.tabla.setHorizontalHeaderLabels([
            "Comprobante", "Huésped", "Habitación", "Tipo",
            "Días", "Subtotal", "Total S/.", "Método Pago", "Fecha Pago"
        ])
        self.tabla.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tabla.horizontalHeader().setSectionResizeMode(7, QHeaderView.Stretch)
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabla.setAlternatingRowColors(True)
        self.tabla.setStyleSheet("alternate-background-color: #F8F9F9;")
        det_layout.addWidget(self.tabla)
        main_layout.addWidget(detalle_gb)

                                                                        
        bottom_layout = QHBoxLayout()

        self.gb_tipo = QGroupBox("Ingresos por Tipo de Habitación")
        tipo_layout = QVBoxLayout(self.gb_tipo)
        self.tabla_tipo = QTableWidget()
        self.tabla_tipo.setColumnCount(3)
        self.tabla_tipo.setHorizontalHeaderLabels(["Tipo", "Comprobantes", "Ingresos S/."])
        self.tabla_tipo.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tabla_tipo.setEditTriggers(QTableWidget.NoEditTriggers)
        tipo_layout.addWidget(self.tabla_tipo)

        self.gb_metodo = QGroupBox("Distribución Métodos de Pago")
        metodo_layout = QVBoxLayout(self.gb_metodo)
        self.tabla_metodo = QTableWidget()
        self.tabla_metodo.setColumnCount(3)
        self.tabla_metodo.setHorizontalHeaderLabels(["Método", "Comprobantes", "Monto S/."])
        self.tabla_metodo.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tabla_metodo.setEditTriggers(QTableWidget.NoEditTriggers)
        metodo_layout.addWidget(self.tabla_metodo)

        bottom_layout.addWidget(self.gb_tipo)
        bottom_layout.addWidget(self.gb_metodo)
        main_layout.addLayout(bottom_layout)

                                                                           
        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.setStyleSheet("background-color: #7F8C8D;")
        btn_cerrar.clicked.connect(self.window.close)
        h = QHBoxLayout()
        h.addStretch()
        h.addWidget(btn_cerrar)
        main_layout.addLayout(h)

    def _tarjeta(self, titulo, valor_inicial, color):
        """Crea una tarjeta de KPI y devuelve (frame, label_valor)."""
        frame = QFrame()
        frame.setStyleSheet(f"""
            QFrame {{
                background-color: {color}; border-radius: 10px;
                min-height: 80px; min-width: 180px;
            }}
        """)
        layout = QVBoxLayout(frame)
        lbl_titulo = QLabel(titulo)
        lbl_titulo.setFont(QFont("Berlin Sans FB", 10))
        lbl_titulo.setStyleSheet("color: white; background-color: transparent;")
        lbl_titulo.setAlignment(Qt.AlignCenter)

        lbl_valor = QLabel(valor_inicial)
        lbl_valor.setFont(QFont("Berlin Sans FB", 20, QFont.Bold))
        lbl_valor.setStyleSheet("color: white; background-color: transparent;")
        lbl_valor.setAlignment(Qt.AlignCenter)

        layout.addWidget(lbl_titulo)
        layout.addWidget(lbl_valor)
                                                                               
        frame._lbl_valor = lbl_valor
        return frame

                                                                          
                                                                           
                                                                          
    def generar_reporte(self):
        f_desde = self.DE_desde.date().toString("yyyy-MM-dd") + " 00:00:00"
        f_hasta = self.DE_hasta.date().toString("yyyy-MM-dd") + " 23:59:59"

        if self.DE_desde.date() > self.DE_hasta.date():
            QMessageBox.warning(self.window, "Fechas", "La fecha 'Desde' debe ser anterior a 'Hasta'.")
            return

                 
        resumen = self.model.get_resumen_ingresos(f_desde, f_hasta)
        self.lbl_ventas._lbl_valor.setText(str(resumen.get("cantidad", 0)))
        self.lbl_ingresos._lbl_valor.setText(f"S/. {resumen.get('total_ingresos', 0):.2f}")
        self.lbl_promedio._lbl_valor.setText(f"S/. {resumen.get('promedio', 0):.2f}")
        self.lbl_noches._lbl_valor.setText(str(resumen.get("total_noches", 0)))

                 
        detalles = self.model.get_reporte_ingresos(f_desde, f_hasta)
        self.tabla.setRowCount(0)
        for row_data in detalles:
            row = self.tabla.rowCount()
            self.tabla.insertRow(row)
            valores = [
                row_data.get("numero_comprobante", ""),
                row_data.get("huesped", ""),
                row_data.get("habitacion", ""),
                row_data.get("tipo", ""),
                str(row_data.get("dias_estancia", "")),
                f"S/. {float(row_data.get('subtotal', 0)):.2f}",
                f"S/. {float(row_data.get('total_general', 0)):.2f}",
                row_data.get("metodo_pago", ""),
                str(row_data.get("fecha_pago", ""))[:16],
            ]
            for col, val in enumerate(valores):
                item = QTableWidgetItem(str(val))
                item.setTextAlignment(Qt.AlignCenter)
                self.tabla.setItem(row, col, item)

                            
        tipos = self.model.get_ocupacion_por_tipo(f_desde, f_hasta)
        self.tabla_tipo.setRowCount(0)
        for t in tipos:
            row = self.tabla_tipo.rowCount()
            self.tabla_tipo.insertRow(row)
            self.tabla_tipo.setItem(row, 0, QTableWidgetItem(t["tipo"]))
            self.tabla_tipo.setItem(row, 1, QTableWidgetItem(str(t["cantidad"])))
            self.tabla_tipo.setItem(row, 2, QTableWidgetItem(f"S/. {t['ingresos']:.2f}"))

                         
        metodos = self.model.get_metodos_pago_stats(f_desde, f_hasta)
        self.tabla_metodo.setRowCount(0)
        for m in metodos:
            row = self.tabla_metodo.rowCount()
            self.tabla_metodo.insertRow(row)
            self.tabla_metodo.setItem(row, 0, QTableWidgetItem(m["metodo"]))
            self.tabla_metodo.setItem(row, 1, QTableWidgetItem(str(m["cantidad"])))
            self.tabla_metodo.setItem(row, 2, QTableWidgetItem(f"S/. {m['monto']:.2f}"))

        if not detalles:
            QMessageBox.information(self.window, "Sin datos",
                                    "No hay comprobantes registrados en ese rango de fechas.")

    def show(self):
        self.window.exec_()
