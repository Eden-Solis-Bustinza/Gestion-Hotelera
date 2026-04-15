                       

                                                                              
 
                                             
 
                                                                           
                                                                       


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 360)
        Dialog.setMinimumSize(QtCore.QSize(650, 360))
        Dialog.setMaximumSize(QtCore.QSize(650, 360))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/images/imagen_login1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(110, 10, 441, 341))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("border-radius: 7px; background-color: #F4F6F6;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.LE_nombres = QtWidgets.QLineEdit(self.frame)
        self.LE_nombres.setGeometry(QtCore.QRect(70, 190, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_nombres.setFont(font)
        self.LE_nombres.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_nombres.setPlaceholderText("Nombres")
        self.LE_nombres.setObjectName("LE_nombres")
        self.LE_contacto = QtWidgets.QLineEdit(self.frame)
        self.LE_contacto.setGeometry(QtCore.QRect(270, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_contacto.setFont(font)
        self.LE_contacto.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_contacto.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.LE_contacto.setPlaceholderText("Contacto")
        self.LE_contacto.setObjectName("LE_contacto")
        self.PB_registrar = QtWidgets.QPushButton(self.frame)
        self.PB_registrar.setGeometry(QtCore.QRect(140, 270, 161, 31))
        self.PB_registrar.setStyleSheet("QPushButton {\n"
"    background-color: #2C3E50;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #16A085;\n"
"}")
        self.PB_registrar.setObjectName("PB_registrar")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(160, 80, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(140, 10, 171, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("assets/images/unnamed.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.LE_numero_d = QtWidgets.QLineEdit(self.frame)
        self.LE_numero_d.setGeometry(QtCore.QRect(70, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_numero_d.setFont(font)
        self.LE_numero_d.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_numero_d.setPlaceholderText("Ingrese documento")
        self.LE_numero_d.setObjectName("LE_numero_d")
        self.CB_tipo_d = QtWidgets.QComboBox(self.frame)
        self.CB_tipo_d.setGeometry(QtCore.QRect(70, 110, 131, 31))
        self.CB_tipo_d.setStyleSheet("QComboBox {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.CB_tipo_d.setObjectName("CB_tipo_d")
        self.LE_correo = QtWidgets.QLineEdit(self.frame)
        self.LE_correo.setGeometry(QtCore.QRect(270, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_correo.setFont(font)
        self.LE_correo.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_correo.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.LE_correo.setObjectName("LE_correo")
        self.DT_nacimiento = QtWidgets.QDateEdit(self.frame)
        self.DT_nacimiento.setGeometry(QtCore.QRect(270, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        self.DT_nacimiento.setFont(font)
        self.DT_nacimiento.setStyleSheet("QDateEdit {\n"
"    color: #2C3E50;\n"
"    background-color: white;\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    alternate-background-color: #F8F9F9; \n"
"    background-color: white; \n"
"    color: black; \n"
"}")
        self.DT_nacimiento.setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.DT_nacimiento.setCalendarPopup(True)
        self.DT_nacimiento.setDate(QtCore.QDate(2026, 3, 26))
        self.DT_nacimiento.setObjectName("DT_nacimiento")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("assets/icons/carnet-de-identidad.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 31, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("assets/icons/comprobado.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 190, 31, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("assets/icons/usuario (1).png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(230, 130, 31, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("assets/icons/llamada-telefonica.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(230, 170, 31, 31))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("assets/icons/correo-electronico.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(230, 210, 31, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("assets/icons/calendario (1).png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.PB_salir = QtWidgets.QPushButton(self.frame)
        self.PB_salir.setGeometry(QtCore.QRect(180, 310, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setBold(False)
        font.setWeight(50)
        self.PB_salir.setFont(font)
        self.PB_salir.setStyleSheet("color: #2C3E50;")
        self.PB_salir.setObjectName("PB_salir")
        self.LE_apellidos = QtWidgets.QLineEdit(self.frame)
        self.LE_apellidos.setGeometry(QtCore.QRect(70, 230, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_apellidos.setFont(font)
        self.LE_apellidos.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_apellidos.setPlaceholderText("Apellidos")
        self.LE_apellidos.setObjectName("LE_apellidos")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(30, 230, 31, 31))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("assets/icons/usuario (1).png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.PB_registrar.setText(_translate("Dialog", "REGISTRAR"))
        self.label_4.setText(_translate("Dialog", "REGISTRAR HUESPED"))
        self.LE_correo.setPlaceholderText(_translate("Dialog", "Correo"))
        self.DT_nacimiento.setDisplayFormat(_translate("Dialog", "dd/MM/yy"))
        self.PB_salir.setText(_translate("Dialog", "SALIR"))
