                       

                                                                
 
                                             
 
                                                                           
                                                                       


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(647, 384)
        self.F_habitacion_N = QtWidgets.QFrame(Dialog)
        self.F_habitacion_N.setGeometry(QtCore.QRect(30, 10, 250, 230))
        self.F_habitacion_N.setMinimumSize(QtCore.QSize(250, 230))
        self.F_habitacion_N.setMaximumSize(QtCore.QSize(250, 230))
        self.F_habitacion_N.setStyleSheet("QFrame {\n"
"    background-color: #16A085;\n"
"    border-radius: 10px;       \n"
"}")
        self.F_habitacion_N.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F_habitacion_N.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F_habitacion_N.setObjectName("F_habitacion_N")
        self.LE_tipoN = QtWidgets.QLineEdit(self.F_habitacion_N)
        self.LE_tipoN.setGeometry(QtCore.QRect(90, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_tipoN.setFont(font)
        self.LE_tipoN.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #1ABC9C;    \n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: transparent;\n"
"}")
        self.LE_tipoN.setReadOnly(True)
        self.LE_tipoN.setPlaceholderText("")
        self.LE_tipoN.setObjectName("LE_tipoN")
        self.label_46 = QtWidgets.QLabel(self.F_habitacion_N)
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
        self.LE_estadoN = QtWidgets.QLineEdit(self.F_habitacion_N)
        self.LE_estadoN.setGeometry(QtCore.QRect(90, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_estadoN.setFont(font)
        self.LE_estadoN.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #1ABC9C;    \n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: transparent;\n"
"}")
        self.LE_estadoN.setReadOnly(True)
        self.LE_estadoN.setPlaceholderText("")
        self.LE_estadoN.setObjectName("LE_estadoN")
        self.PB_editar_hN = QtWidgets.QPushButton(self.F_habitacion_N)
        self.PB_editar_hN.setGeometry(QtCore.QRect(30, 110, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_editar_hN.setFont(font)
        self.PB_editar_hN.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.PB_editar_hN.setObjectName("PB_editar_hN")
        self.label_13 = QtWidgets.QLabel(self.F_habitacion_N)
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
        self.label_19 = QtWidgets.QLabel(self.F_habitacion_N)
        self.label_19.setGeometry(QtCore.QRect(80, 10, 91, 101))
        self.label_19.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("assets/icons/cama.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.F_notificacionN_2 = QtWidgets.QFrame(Dialog)
        self.F_notificacionN_2.setGeometry(QtCore.QRect(10, 260, 600, 70))
        self.F_notificacionN_2.setMinimumSize(QtCore.QSize(600, 70))
        self.F_notificacionN_2.setMaximumSize(QtCore.QSize(600, 70))
        self.F_notificacionN_2.setStyleSheet("QFrame {\n"
"    border-bottom: 1px solid #D5DBDB;\n"
"    background-color: transparent;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: #F8F9F9;\n"
"}")
        self.F_notificacionN_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F_notificacionN_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F_notificacionN_2.setObjectName("F_notificacionN_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.F_notificacionN_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, 10, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.L_colorN_2 = QtWidgets.QLabel(self.F_notificacionN_2)
        self.L_colorN_2.setMinimumSize(QtCore.QSize(20, 20))
        self.L_colorN_2.setMaximumSize(QtCore.QSize(20, 20))
        self.L_colorN_2.setStyleSheet("QLabel{\n"
"    background-color: #16A085;   \n"
"}")
        self.L_colorN_2.setText("")
        self.L_colorN_2.setScaledContents(True)
        self.L_colorN_2.setWordWrap(False)
        self.L_colorN_2.setObjectName("L_colorN_2")
        self.horizontalLayout.addWidget(self.L_colorN_2)
        self.LE_tipoN_2 = QtWidgets.QLineEdit(self.F_notificacionN_2)
        self.LE_tipoN_2.setMinimumSize(QtCore.QSize(100, 31))
        self.LE_tipoN_2.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_tipoN_2.setFont(font)
        self.LE_tipoN_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_tipoN_2.setReadOnly(True)
        self.LE_tipoN_2.setPlaceholderText("Tipo")
        self.LE_tipoN_2.setObjectName("LE_tipoN_2")
        self.horizontalLayout.addWidget(self.LE_tipoN_2)
        self.LE_mensajeN_2 = QtWidgets.QLineEdit(self.F_notificacionN_2)
        self.LE_mensajeN_2.setMinimumSize(QtCore.QSize(300, 31))
        self.LE_mensajeN_2.setMaximumSize(QtCore.QSize(300, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_mensajeN_2.setFont(font)
        self.LE_mensajeN_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_mensajeN_2.setReadOnly(True)
        self.LE_mensajeN_2.setPlaceholderText("Notificacion")
        self.LE_mensajeN_2.setObjectName("LE_mensajeN_2")
        self.horizontalLayout.addWidget(self.LE_mensajeN_2)
        self.LE_fyhN_2 = QtWidgets.QLineEdit(self.F_notificacionN_2)
        self.LE_fyhN_2.setMinimumSize(QtCore.QSize(100, 31))
        self.LE_fyhN_2.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_fyhN_2.setFont(font)
        self.LE_fyhN_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_fyhN_2.setReadOnly(True)
        self.LE_fyhN_2.setPlaceholderText("Fecha y hora")
        self.LE_fyhN_2.setObjectName("LE_fyhN_2")
        self.horizontalLayout.addWidget(self.LE_fyhN_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_46.setText(_translate("Dialog", "Tipo:"))
        self.PB_editar_hN.setText(_translate("Dialog", "HABITACION - 103"))
        self.label_13.setText(_translate("Dialog", "Estado:"))
