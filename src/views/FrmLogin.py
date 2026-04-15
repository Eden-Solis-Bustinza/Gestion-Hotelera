                       

                                                                  
 
                                             
 
                                                                           
                                                                       


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(468, 341)
        Dialog.setMinimumSize(QtCore.QSize(468, 341))
        Dialog.setMaximumSize(QtCore.QSize(468, 341))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 471, 341))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/images/imagen_login1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(110, 30, 241, 291))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("border-radius: 7px; background-color: #F4F6F6;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.LE_correo = QtWidgets.QLineEdit(self.frame)
        self.LE_correo.setGeometry(QtCore.QRect(70, 120, 131, 31))
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
        self.LE_correo.setPlaceholderText("Correo")
        self.LE_correo.setObjectName("LE_correo")
        self.LE_contrasena = QtWidgets.QLineEdit(self.frame)
        self.LE_contrasena.setGeometry(QtCore.QRect(70, 160, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_contrasena.setFont(font)
        self.LE_contrasena.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_contrasena.setObjectName("LE_contrasena")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("assets/icons/usuario.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 31, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("assets/icons/cerrar-con-llave.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.PB_ingresar = QtWidgets.QPushButton(self.frame)
        self.PB_ingresar.setGeometry(QtCore.QRect(40, 210, 161, 31))
        self.PB_ingresar.setStyleSheet("QPushButton {\n"
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
        self.PB_ingresar.setObjectName("PB_ingresar")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 90, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 20, 171, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("assets/images/unnamed.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.PB_recuperar_c = QtWidgets.QPushButton(self.frame)
        self.PB_recuperar_c.setGeometry(QtCore.QRect(40, 240, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setBold(False)
        font.setWeight(50)
        self.PB_recuperar_c.setFont(font)
        self.PB_recuperar_c.setStyleSheet("color: #2C3E50;")
        self.PB_recuperar_c.setObjectName("PB_recuperar_c")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.LE_contrasena.setPlaceholderText(_translate("Dialog", "Contraseña"))
        self.PB_ingresar.setText(_translate("Dialog", "INGRESAR"))
        self.label_4.setText(_translate("Dialog", "INICIAR SESION"))
        self.PB_recuperar_c.setText(_translate("Dialog", "RECUPERAR CONTRASEÑA"))
