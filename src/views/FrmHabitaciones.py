                       

                                                                         
 
                                             
 
                                                                           
                                                                       


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(697, 492)
        Dialog.setMinimumSize(QtCore.QSize(697, 492))
        Dialog.setMaximumSize(QtCore.QSize(697, 492))
        Dialog.setStyleSheet("background-color: #EBEDEF;")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(560, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: Black;\n"
"}")
        self.label_24.setObjectName("label_24")
        self.L_disponible = QtWidgets.QLabel(Dialog)
        self.L_disponible.setGeometry(QtCore.QRect(560, 40, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.L_disponible.setFont(font)
        self.L_disponible.setStyleSheet("QLabel{\n"
"    background-color: #16A085;   \n"
"}")
        self.L_disponible.setText("")
        self.L_disponible.setObjectName("L_disponible")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(590, 40, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: Black;\n"
"}")
        self.label_26.setObjectName("label_26")
        self.L_ocupado = QtWidgets.QLabel(Dialog)
        self.L_ocupado.setGeometry(QtCore.QRect(560, 70, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.L_ocupado.setFont(font)
        self.L_ocupado.setStyleSheet("QLabel{\n"
"    background-color: #F1948A;   \n"
"}")
        self.L_ocupado.setText("")
        self.L_ocupado.setObjectName("L_ocupado")
        self.label_28 = QtWidgets.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(590, 70, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: Black;\n"
"}")
        self.label_28.setObjectName("label_28")
        self.L_limyman = QtWidgets.QLabel(Dialog)
        self.L_limyman.setGeometry(QtCore.QRect(560, 130, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.L_limyman.setFont(font)
        self.L_limyman.setStyleSheet("QLabel{\n"
"    background-color: #F8C471;   \n"
"}")
        self.L_limyman.setText("")
        self.L_limyman.setObjectName("L_limyman")
        self.label_30 = QtWidgets.QLabel(Dialog)
        self.label_30.setGeometry(QtCore.QRect(590, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: Black;\n"
"}")
        self.label_30.setWordWrap(True)
        self.label_30.setObjectName("label_30")
        self.L_reservado = QtWidgets.QLabel(Dialog)
        self.L_reservado.setGeometry(QtCore.QRect(560, 100, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.L_reservado.setFont(font)
        self.L_reservado.setStyleSheet("QLabel{\n"
"    background-color: #AED6F1;   \n"
"}")
        self.L_reservado.setText("")
        self.L_reservado.setObjectName("L_reservado")
        self.label_32 = QtWidgets.QLabel(Dialog)
        self.label_32.setGeometry(QtCore.QRect(590, 100, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: Black;\n"
"}")
        self.label_32.setObjectName("label_32")
        self.SA_interfaz_h = QtWidgets.QScrollArea(Dialog)
        self.SA_interfaz_h.setGeometry(QtCore.QRect(0, 0, 531, 491))
        self.SA_interfaz_h.setWidgetResizable(True)
        self.SA_interfaz_h.setObjectName("SA_interfaz_h")
        self.SAWC_interfaz_a_h = QtWidgets.QWidget()
        self.SAWC_interfaz_a_h.setGeometry(QtCore.QRect(0, 0, 529, 489))
        self.SAWC_interfaz_a_h.setObjectName("SAWC_interfaz_a_h")
        self.gridLayout = QtWidgets.QGridLayout(self.SAWC_interfaz_a_h)
        self.gridLayout.setObjectName("gridLayout")
        self.F_agregar = QtWidgets.QFrame(self.SAWC_interfaz_a_h)
        self.F_agregar.setMinimumSize(QtCore.QSize(250, 230))
        self.F_agregar.setMaximumSize(QtCore.QSize(250, 230))
        self.F_agregar.setStyleSheet("QFrame {\n"
"    background-color: #F8F9F9;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2C3E50;       \n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background-color: #EAECEE;\n"
"    border: 3px solid #1ABC9C;\n"
"}")
        self.F_agregar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F_agregar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F_agregar.setObjectName("F_agregar")
        self.label_45 = QtWidgets.QLabel(self.F_agregar)
        self.label_45.setGeometry(QtCore.QRect(40, 90, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.label_45.setObjectName("label_45")
        self.PB_agregar_h = QtWidgets.QPushButton(self.F_agregar)
        self.PB_agregar_h.setGeometry(QtCore.QRect(30, 20, 201, 181))
        self.PB_agregar_h.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_agregar_h.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px;\n"
"}")
        self.PB_agregar_h.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons/mas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PB_agregar_h.setIcon(icon)
        self.PB_agregar_h.setIconSize(QtCore.QSize(141, 131))
        self.PB_agregar_h.setCheckable(True)
        self.PB_agregar_h.setFlat(True)
        self.PB_agregar_h.setObjectName("PB_agregar_h")
        self.gridLayout.addWidget(self.F_agregar, 1, 1, 1, 1)
        self.F_habitacion_1 = QtWidgets.QFrame(self.SAWC_interfaz_a_h)
        self.F_habitacion_1.setMinimumSize(QtCore.QSize(250, 230))
        self.F_habitacion_1.setMaximumSize(QtCore.QSize(250, 230))
        self.F_habitacion_1.setStyleSheet("QFrame {\n"
"    background-color: #16A085;\n"
"    border-radius: 10px;\n"
"}")
        self.F_habitacion_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F_habitacion_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F_habitacion_1.setObjectName("F_habitacion_1")
        self.label_18 = QtWidgets.QLabel(self.F_habitacion_1)
        self.label_18.setGeometry(QtCore.QRect(80, 10, 91, 101))
        self.label_18.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("assets/icons/cama.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.PB_editar_h1 = QtWidgets.QPushButton(self.F_habitacion_1)
        self.PB_editar_h1.setGeometry(QtCore.QRect(30, 110, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_editar_h1.setFont(font)
        self.PB_editar_h1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_editar_h1.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.PB_editar_h1.setObjectName("PB_editar_h1")
        self.label_43 = QtWidgets.QLabel(self.F_habitacion_1)
        self.label_43.setGeometry(QtCore.QRect(50, 140, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.label_43.setObjectName("label_43")
        self.label_11 = QtWidgets.QLabel(self.F_habitacion_1)
        self.label_11.setGeometry(QtCore.QRect(40, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.LE_tipo = QtWidgets.QLineEdit(self.F_habitacion_1)
        self.LE_tipo.setGeometry(QtCore.QRect(90, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_tipo.setFont(font)
        self.LE_tipo.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #1ABC9C;    \n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: transparent;\n"
"}")
        self.LE_tipo.setReadOnly(True)
        self.LE_tipo.setPlaceholderText("")
        self.LE_tipo.setObjectName("LE_tipo")
        self.LE_estado = QtWidgets.QLineEdit(self.F_habitacion_1)
        self.LE_estado.setGeometry(QtCore.QRect(90, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_estado.setFont(font)
        self.LE_estado.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #1ABC9C;    \n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: transparent;\n"
"}")
        self.LE_estado.setReadOnly(True)
        self.LE_estado.setPlaceholderText("")
        self.LE_estado.setObjectName("LE_estado")
        self.gridLayout.addWidget(self.F_habitacion_1, 0, 0, 1, 1)
        self.F_habitacion_2 = QtWidgets.QFrame(self.SAWC_interfaz_a_h)
        self.F_habitacion_2.setMinimumSize(QtCore.QSize(250, 230))
        self.F_habitacion_2.setMaximumSize(QtCore.QSize(250, 230))
        self.F_habitacion_2.setStyleSheet("QFrame {\n"
"    background-color: #16A085;\n"
"    border-radius: 10px;       \n"
"}")
        self.F_habitacion_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F_habitacion_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F_habitacion_2.setObjectName("F_habitacion_2")
        self.label_16 = QtWidgets.QLabel(self.F_habitacion_2)
        self.label_16.setGeometry(QtCore.QRect(80, 10, 91, 101))
        self.label_16.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("assets/icons/cama.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_12 = QtWidgets.QLabel(self.F_habitacion_2)
        self.label_12.setGeometry(QtCore.QRect(40, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.label_12.setObjectName("label_12")
        self.PB_editar_h2 = QtWidgets.QPushButton(self.F_habitacion_2)
        self.PB_editar_h2.setGeometry(QtCore.QRect(30, 110, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_editar_h2.setFont(font)
        self.PB_editar_h2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_editar_h2.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.PB_editar_h2.setObjectName("PB_editar_h2")
        self.LE_estado2 = QtWidgets.QLineEdit(self.F_habitacion_2)
        self.LE_estado2.setGeometry(QtCore.QRect(90, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_estado2.setFont(font)
        self.LE_estado2.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #1ABC9C;    \n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: transparent;\n"
"}")
        self.LE_estado2.setReadOnly(True)
        self.LE_estado2.setPlaceholderText("")
        self.LE_estado2.setObjectName("LE_estado2")
        self.label_44 = QtWidgets.QLabel(self.F_habitacion_2)
        self.label_44.setGeometry(QtCore.QRect(50, 140, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.label_44.setObjectName("label_44")
        self.LE_tipo2 = QtWidgets.QLineEdit(self.F_habitacion_2)
        self.LE_tipo2.setGeometry(QtCore.QRect(90, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_tipo2.setFont(font)
        self.LE_tipo2.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #1ABC9C;    \n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: transparent;\n"
"}")
        self.LE_tipo2.setReadOnly(True)
        self.LE_tipo2.setPlaceholderText("")
        self.LE_tipo2.setObjectName("LE_tipo2")
        self.gridLayout.addWidget(self.F_habitacion_2, 0, 1, 1, 1)
        self.F_habitacion_3 = QtWidgets.QFrame(self.SAWC_interfaz_a_h)
        self.F_habitacion_3.setMinimumSize(QtCore.QSize(250, 230))
        self.F_habitacion_3.setMaximumSize(QtCore.QSize(250, 230))
        self.F_habitacion_3.setStyleSheet("QFrame {\n"
"    background-color: #16A085;\n"
"    border-radius: 10px;       \n"
"}")
        self.F_habitacion_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F_habitacion_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F_habitacion_3.setObjectName("F_habitacion_3")
        self.LE_tipo3 = QtWidgets.QLineEdit(self.F_habitacion_3)
        self.LE_tipo3.setGeometry(QtCore.QRect(90, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_tipo3.setFont(font)
        self.LE_tipo3.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #1ABC9C;    \n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: transparent;\n"
"}")
        self.LE_tipo3.setReadOnly(True)
        self.LE_tipo3.setPlaceholderText("")
        self.LE_tipo3.setObjectName("LE_tipo3")
        self.label_46 = QtWidgets.QLabel(self.F_habitacion_3)
        self.label_46.setGeometry(QtCore.QRect(50, 140, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.label_46.setObjectName("label_46")
        self.LE_estado3 = QtWidgets.QLineEdit(self.F_habitacion_3)
        self.LE_estado3.setGeometry(QtCore.QRect(90, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_estado3.setFont(font)
        self.LE_estado3.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #1ABC9C;    \n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: transparent;\n"
"}")
        self.LE_estado3.setReadOnly(True)
        self.LE_estado3.setPlaceholderText("")
        self.LE_estado3.setObjectName("LE_estado3")
        self.PB_editar_h3 = QtWidgets.QPushButton(self.F_habitacion_3)
        self.PB_editar_h3.setGeometry(QtCore.QRect(30, 110, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_editar_h3.setFont(font)
        self.PB_editar_h3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_editar_h3.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.PB_editar_h3.setObjectName("PB_editar_h3")
        self.label_13 = QtWidgets.QLabel(self.F_habitacion_3)
        self.label_13.setGeometry(QtCore.QRect(40, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.label_13.setObjectName("label_13")
        self.label_19 = QtWidgets.QLabel(self.F_habitacion_3)
        self.label_19.setGeometry(QtCore.QRect(80, 10, 91, 101))
        self.label_19.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("assets/icons/cama.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.F_habitacion_3, 1, 0, 1, 1)
        self.SA_interfaz_h.setWidget(self.SAWC_interfaz_a_h)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_24.setText(_translate("Dialog", "LEYENDA:"))
        self.label_26.setText(_translate("Dialog", "Disponible"))
        self.label_28.setText(_translate("Dialog", "Ocupado"))
        self.label_30.setText(_translate("Dialog", "Limpieza / Mantenimiento"))
        self.label_32.setText(_translate("Dialog", "Reservado"))
        self.label_45.setText(_translate("Dialog", "Tipo:"))
        self.PB_editar_h1.setText(_translate("Dialog", "HABITACION - 101"))
        self.label_43.setText(_translate("Dialog", "Tipo:"))
        self.label_11.setText(_translate("Dialog", "Estado:"))
        self.label_12.setText(_translate("Dialog", "Estado:"))
        self.PB_editar_h2.setText(_translate("Dialog", "HABITACION - 102"))
        self.label_44.setText(_translate("Dialog", "Tipo:"))
        self.label_46.setText(_translate("Dialog", "Tipo:"))
        self.PB_editar_h3.setText(_translate("Dialog", "HABITACION - 103"))
        self.label_13.setText(_translate("Dialog", "Estado:"))
