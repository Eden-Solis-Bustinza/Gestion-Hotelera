                       

                                                                      
 
                                             
 
                                                                           
                                                                       


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 525)
        MainWindow.setMinimumSize(QtCore.QSize(1049, 525))
        MainWindow.setMaximumSize(QtCore.QSize(1049, 525))
        MainWindow.setStyleSheet("background-color: #EBEDEF;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1061, 71))
        self.frame.setStyleSheet("border-radius: 7px; background-color: #F8F9F9;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 191, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("assets/images/unnamed.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(930, 0, 61, 71))
        self.label_14.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("assets/icons/cuenta.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.PB_notificaciones = QtWidgets.QPushButton(self.frame)
        self.PB_notificaciones.setGeometry(QtCore.QRect(1000, 0, 51, 71))
        self.PB_notificaciones.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons/notificaciones.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PB_notificaciones.setIcon(icon)
        self.PB_notificaciones.setIconSize(QtCore.QSize(60, 60))
        self.PB_notificaciones.setObjectName("PB_notificaciones")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(290, 120, 221, 161))
        self.frame_2.setStyleSheet("QFrame {\n"
"    background-color: #2C3E50;\n"
"    border-radius: 10px;       \n"
"    border: 1px solid #34495E; \n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background-color: #16A085;\n"
"    border: 1px solid #1ABC9C;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.PB_habitacion = QtWidgets.QPushButton(self.frame_2)
        self.PB_habitacion.setGeometry(QtCore.QRect(30, 122, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PB_habitacion.setFont(font)
        self.PB_habitacion.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.PB_habitacion.setObjectName("PB_habitacion")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(60, 20, 101, 101))
        self.label_8.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("assets/icons/cama.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(40, 120, 221, 161))
        self.frame_3.setStyleSheet("QFrame {\n"
"    background-color: #2C3E50;\n"
"    border-radius: 10px;       \n"
"    border: 1px solid #34495E; \n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background-color: #16A085;\n"
"    border: 1px solid #1ABC9C;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.PB_registro_h = QtWidgets.QPushButton(self.frame_3)
        self.PB_registro_h.setGeometry(QtCore.QRect(30, 120, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.PB_registro_h.setFont(font)
        self.PB_registro_h.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.PB_registro_h.setFlat(False)
        self.PB_registro_h.setObjectName("PB_registro_h")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(70, 20, 81, 101))
        self.label_7.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("assets/icons/registro.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(540, 120, 221, 161))
        self.frame_4.setStyleSheet("QFrame {\n"
"    background-color: #2C3E50;\n"
"    border-radius: 10px;       \n"
"    border: 1px solid #34495E; \n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background-color: #16A085;\n"
"    border: 1px solid #1ABC9C;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.PB_reserva = QtWidgets.QPushButton(self.frame_4)
        self.PB_reserva.setGeometry(QtCore.QRect(30, 122, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PB_reserva.setFont(font)
        self.PB_reserva.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.PB_reserva.setObjectName("PB_reserva")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(60, 20, 101, 101))
        self.label_9.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("assets/icons/calendario.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(290, 320, 221, 161))
        self.frame_6.setStyleSheet("QFrame {\n"
"    background-color: #2C3E50;\n"
"    border-radius: 10px;       \n"
"    border: 1px solid #34495E; \n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background-color: #16A085;\n"
"    border: 1px solid #1ABC9C;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.PB_producto = QtWidgets.QPushButton(self.frame_6)
        self.PB_producto.setGeometry(QtCore.QRect(30, 122, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PB_producto.setFont(font)
        self.PB_producto.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.PB_producto.setObjectName("PB_producto")
        self.label_12 = QtWidgets.QLabel(self.frame_6)
        self.label_12.setGeometry(QtCore.QRect(60, 20, 101, 101))
        self.label_12.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("assets/icons/consumo.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(790, 120, 221, 161))
        self.frame_7.setStyleSheet("QFrame {\n"
"    background-color: #2C3E50;\n"
"    border-radius: 10px;       \n"
"    border: 1px solid #34495E; \n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background-color: #16A085;\n"
"    border: 1px solid #1ABC9C;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.PB_checkin = QtWidgets.QPushButton(self.frame_7)
        self.PB_checkin.setGeometry(QtCore.QRect(30, 122, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PB_checkin.setFont(font)
        self.PB_checkin.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.PB_checkin.setObjectName("PB_checkin")
        self.label_10 = QtWidgets.QLabel(self.frame_7)
        self.label_10.setGeometry(QtCore.QRect(70, 20, 91, 101))
        self.label_10.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("assets/icons/lista-de-verificacion 2.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(40, 320, 221, 161))
        self.frame_8.setStyleSheet("QFrame {\n"
"    background-color: #2C3E50;\n"
"    border-radius: 10px;       \n"
"    border: 1px solid #34495E; \n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background-color: #16A085;\n"
"    border: 1px solid #1ABC9C;\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.PB_checkout = QtWidgets.QPushButton(self.frame_8)
        self.PB_checkout.setGeometry(QtCore.QRect(30, 122, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PB_checkout.setFont(font)
        self.PB_checkout.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.PB_checkout.setObjectName("PB_checkout")
        self.label_11 = QtWidgets.QLabel(self.frame_8)
        self.label_11.setGeometry(QtCore.QRect(60, 20, 101, 101))
        self.label_11.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("assets/icons/lista.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setGeometry(QtCore.QRect(540, 320, 221, 161))
        self.frame_9.setStyleSheet("QFrame {\n"
"    background-color: #2C3E50;\n"
"    border-radius: 10px;       \n"
"    border: 1px solid #34495E; \n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background-color: #16A085;\n"
"    border: 1px solid #1ABC9C;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.PB_reporte = QtWidgets.QPushButton(self.frame_9)
        self.PB_reporte.setGeometry(QtCore.QRect(30, 122, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PB_reporte.setFont(font)
        self.PB_reporte.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.PB_reporte.setObjectName("PB_reporte")
        self.label_13 = QtWidgets.QLabel(self.frame_9)
        self.label_13.setGeometry(QtCore.QRect(60, 20, 101, 101))
        self.label_13.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("assets/icons/informe-de-venta.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(790, 320, 221, 161))
        self.frame_5.setStyleSheet("QFrame {\n"
"    background-color: #2C3E50;\n"
"    border-radius: 10px;       \n"
"    border: 1px solid #34495E; \n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background-color: #16A085;\n"
"    border: 1px solid #1ABC9C;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.PB_registrar_u = QtWidgets.QPushButton(self.frame_5)
        self.PB_registrar_u.setGeometry(QtCore.QRect(30, 122, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PB_registrar_u.setFont(font)
        self.PB_registrar_u.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.PB_registrar_u.setObjectName("PB_registrar_u")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(60, 20, 101, 101))
        self.label_15.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("assets/icons/recursos-humanos.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PB_habitacion.setText(_translate("MainWindow", "HABITACIONES"))
        self.PB_registro_h.setText(_translate("MainWindow", "REGISTRO HUESPEDES"))
        self.PB_reserva.setText(_translate("MainWindow", "RESERVAS"))
        self.PB_producto.setText(_translate("MainWindow", "PRODUCTOS"))
        self.PB_checkin.setText(_translate("MainWindow", "CHECK-IN"))
        self.PB_checkout.setText(_translate("MainWindow", "CHECK-OUT"))
        self.PB_reporte.setText(_translate("MainWindow", "REPORTES"))
        self.PB_registrar_u.setText(_translate("MainWindow", "REGISTRAR USUARIO"))
