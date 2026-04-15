from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from src.views.FrmCheckin import Ui_Dialog
from src.models.checkin_model import CheckinModel
from datetime import datetime

class CheckinController:
    # Recibimos el user_data para saber qué recepcionista está haciendo el checkin
    def __init__(self, user_data): 
        self.window = QtWidgets.QDialog()
        self.view = Ui_Dialog()
        self.view.setupUi(self.window)
        
        self.user_data = user_data
        self.model = CheckinModel()
        
        self.id_huesped_actual = None # Variable de control de estado
        
        self.setup_ui_defaults()
        self.setup_connections()

    def show(self):
        self.window.exec_()

    def setup_ui_defaults(self):
        """Configuración de seguridad inicial y control de fechas"""
        # Bloquear botón de Check-in hasta que se busque un DNI válido
        self.view.PB_marcar_checkin.setEnabled(False)
        self.view.CB_numero_h.setEnabled(False)
        
        # Ocultar el control y el ícono sobrantes de tipo de habitación
        self.view.CB_tipo_h.hide()
        self.view.label_19.hide()

        # --- REGLAS DE NEGOCIO PARA LA INTERFAZ ---
        # Desbloqueamos SOLO lo que el recepcionista puede negociar
        self.view.SB_numero_h.setReadOnly(False)
        self.view.LE_monto_a.setReadOnly(False)
        self.view.DT_fyh_salida.setReadOnly(False)

        # BLOQUEO CRÍTICO: La fecha de ingreso es intocable (Tiempo real)
        self.view.DT_fyh_ingreso.setReadOnly(True)

        # Capturamos el tiempo real de la computadora
        ahora = QtCore.QDateTime.currentDateTime()
        self.view.DT_fyh_ingreso.setDateTime(ahora)
        
        # Bloqueo lógico: La fecha de salida no puede ser anterior a la fecha de ingreso
        self.view.DT_fyh_salida.setMinimumDateTime(ahora)

        # Salida por defecto: Al día siguiente a las 12:00 PM
        manana = ahora.addDays(1)
        manana.setTime(QtCore.QTime(12, 0))
        self.view.DT_fyh_salida.setDateTime(manana)

        # Cargar combos
        self.cargar_habitaciones()
        self.cargar_metodos_pago()

    def cargar_habitaciones(self):
        habitaciones = self.model.get_habitaciones_disponibles()
        self.view.CB_numero_h.clear()
        if not habitaciones:
            self.view.CB_numero_h.addItem("Sin habitaciones disponibles")
            return
            
        for id_hab, numero, tipo in habitaciones:
            # Guardamos el ID en la data y mostramos "Numero - Tipo"
            self.view.CB_numero_h.addItem(f"{numero} - {tipo}", id_hab)

    def cargar_metodos_pago(self):
        metodos = self.model.get_metodos_pago()
        self.view.CB_medio_p.clear()
        for id_metodo, nombre in metodos:
            self.view.CB_medio_p.addItem(nombre, id_metodo)

    def setup_connections(self):
        self.view.PB_buscar.clicked.connect(self.buscar_huesped)
        self.view.PB_marcar_checkin.clicked.connect(self.procesar_checkin)
        self.view.PB_salir.clicked.connect(self.window.close)

    def buscar_huesped(self):
        dni = self.view.LE_numero_d.text().strip()
        if not dni:
            QMessageBox.warning(self.window, "Error", "Ingrese un número de documento.")
            return

        huesped = self.model.buscar_huesped_por_dni(dni)
        
        if huesped:
            # Desbloquear el sistema
            self.id_huesped_actual = huesped['id']
            self.view.LE_nombres_apellidos.setText(huesped['nombres'])
            self.view.LE_contacto.setText(huesped['contacto'])
            
            self.view.CB_numero_h.setEnabled(True)
            self.view.PB_marcar_checkin.setEnabled(True)
            self.view.LE_id_r.setText("INGRESO DIRECTO")
            QMessageBox.information(self.window, "Encontrado", "Huésped validado. Proceda con el Check-in.")
        else:
            self.id_huesped_actual = None
            self.view.PB_marcar_checkin.setEnabled(False)
            self.view.CB_numero_h.setEnabled(False)
            self.view.LE_nombres_apellidos.clear()
            self.view.LE_contacto.clear()
            QMessageBox.warning(self.window, "No encontrado", "El DNI no está registrado. Por favor, registre al huésped primero.")

    def procesar_checkin(self):
        # Validar si hubo manipulación
        if not self.id_huesped_actual:
            return

        id_habitacion = self.view.CB_numero_h.currentData()
        if not id_habitacion:
            QMessageBox.warning(self.window, "Error", "No hay habitaciones disponibles seleccionadas.")
            return

        num_huespedes = self.view.SB_numero_h.value()
        if num_huespedes <= 0:
            QMessageBox.warning(self.window, "Error", "El número de huéspedes debe ser mayor a cero.")
            return

        monto_adelantado = self.view.LE_monto_a.text().strip()
        if not monto_adelantado.replace('.', '', 1).isdigit():
            monto_adelantado = 0.0
        else:
            monto_adelantado = float(monto_adelantado)

        id_metodo = self.view.CB_medio_p.currentData()
        fecha_in = self.view.DT_fyh_ingreso.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        fecha_out = self.view.DT_fyh_salida.dateTime().toString("yyyy-MM-dd HH:mm:ss")

        # Ejecutar Transacción
        # BUG-01 FIX: user_data['id'] es el id_usuario real, NO id_rol
        exito = self.model.registrar_checkin_directo(
            self.id_huesped_actual, id_habitacion, num_huespedes,
            fecha_in, fecha_out, monto_adelantado, id_metodo,
            self.user_data.get('id', 1)
        )

        if exito:
            QMessageBox.information(self.window, "Éxito", "Check-in registrado. La habitación ahora está OCUPADA.")
            self.window.close()
        else:
            QMessageBox.critical(self.window, "Error Transaccional", "Ocurrió un error al procesar el Check-in. Operación revertida por seguridad.")