                       

                                                                           
 
                                             
 
                                                                           
                                                                       


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(840, 478)
        Dialog.setMinimumSize(QtCore.QSize(840, 478))
        Dialog.setMaximumSize(QtCore.QSize(840, 478))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 841, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/images/imagen_login1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(120, 40, 611, 381))
        self.scrollArea.setStyleSheet("QScrollArea {\n"
"    border: 2px solid #2C3E50;\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #F0F0F0; \n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #2C3E50; \n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"    margin: 2px; \n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #1ABC9C; \n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.SAWC_interfaz_a_n = QtWidgets.QWidget()
        self.SAWC_interfaz_a_n.setGeometry(QtCore.QRect(0, 0, 607, 377))
        self.SAWC_interfaz_a_n.setObjectName("SAWC_interfaz_a_n")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SAWC_interfaz_a_n)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.F_notificacion1 = QtWidgets.QFrame(self.SAWC_interfaz_a_n)
        self.F_notificacion1.setMinimumSize(QtCore.QSize(600, 70))
        self.F_notificacion1.setMaximumSize(QtCore.QSize(600, 70))
        self.F_notificacion1.setStyleSheet("QFrame {\n"
"    border-bottom: 1px solid #D5DBDB;\n"
"    background-color: transparent;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: #F8F9F9;\n"
"}")
        self.F_notificacion1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F_notificacion1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F_notificacion1.setObjectName("F_notificacion1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.F_notificacion1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, 10, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.L_disponible = QtWidgets.QLabel(self.F_notificacion1)
        self.L_disponible.setMinimumSize(QtCore.QSize(20, 20))
        self.L_disponible.setMaximumSize(QtCore.QSize(20, 20))
        self.L_disponible.setStyleSheet("QLabel{\n"
"    background-color: #16A085;   \n"
"}")
        self.L_disponible.setText("")
        self.L_disponible.setScaledContents(True)
        self.L_disponible.setWordWrap(False)
        self.L_disponible.setObjectName("L_disponible")
        self.horizontalLayout.addWidget(self.L_disponible)
        self.LE_tipo1 = QtWidgets.QLineEdit(self.F_notificacion1)
        self.LE_tipo1.setMinimumSize(QtCore.QSize(100, 31))
        self.LE_tipo1.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_tipo1.setFont(font)
        self.LE_tipo1.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_tipo1.setReadOnly(True)
        self.LE_tipo1.setPlaceholderText("Tipo")
        self.LE_tipo1.setObjectName("LE_tipo1")
        self.horizontalLayout.addWidget(self.LE_tipo1)
        self.LE_mensaje1 = QtWidgets.QLineEdit(self.F_notificacion1)
        self.LE_mensaje1.setMinimumSize(QtCore.QSize(300, 31))
        self.LE_mensaje1.setMaximumSize(QtCore.QSize(300, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_mensaje1.setFont(font)
        self.LE_mensaje1.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_mensaje1.setReadOnly(True)
        self.LE_mensaje1.setPlaceholderText("Notificacion")
        self.LE_mensaje1.setObjectName("LE_mensaje1")
        self.horizontalLayout.addWidget(self.LE_mensaje1)
        self.LE_fyh1 = QtWidgets.QLineEdit(self.F_notificacion1)
        self.LE_fyh1.setMinimumSize(QtCore.QSize(100, 31))
        self.LE_fyh1.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_fyh1.setFont(font)
        self.LE_fyh1.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_fyh1.setReadOnly(True)
        self.LE_fyh1.setPlaceholderText("Fecha y hora")
        self.LE_fyh1.setObjectName("LE_fyh1")
        self.horizontalLayout.addWidget(self.LE_fyh1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.F_notificacion1)
        self.F_notificacion2 = QtWidgets.QFrame(self.SAWC_interfaz_a_n)
        self.F_notificacion2.setMinimumSize(QtCore.QSize(600, 70))
        self.F_notificacion2.setMaximumSize(QtCore.QSize(600, 70))
        self.F_notificacion2.setStyleSheet("QFrame {\n"
"    border-bottom: 1px solid #D5DBDB;\n"
"    background-color: transparent;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: #F8F9F9;\n"
"}")
        self.F_notificacion2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F_notificacion2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F_notificacion2.setObjectName("F_notificacion2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.F_notificacion2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, -1, 10, 5)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.L_reservado = QtWidgets.QLabel(self.F_notificacion2)
        self.L_reservado.setMinimumSize(QtCore.QSize(20, 20))
        self.L_reservado.setMaximumSize(QtCore.QSize(20, 20))
        self.L_reservado.setStyleSheet("QLabel{\n"
"    background-color: #AED6F1;   \n"
"}")
        self.L_reservado.setText("")
        self.L_reservado.setScaledContents(True)
        self.L_reservado.setWordWrap(False)
        self.L_reservado.setObjectName("L_reservado")
        self.horizontalLayout_4.addWidget(self.L_reservado)
        self.LE_tipo2 = QtWidgets.QLineEdit(self.F_notificacion2)
        self.LE_tipo2.setMinimumSize(QtCore.QSize(100, 31))
        self.LE_tipo2.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_tipo2.setFont(font)
        self.LE_tipo2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_tipo2.setReadOnly(True)
        self.LE_tipo2.setPlaceholderText("Tipo")
        self.LE_tipo2.setObjectName("LE_tipo2")
        self.horizontalLayout_4.addWidget(self.LE_tipo2)
        self.LE_mensaje2 = QtWidgets.QLineEdit(self.F_notificacion2)
        self.LE_mensaje2.setMinimumSize(QtCore.QSize(300, 31))
        self.LE_mensaje2.setMaximumSize(QtCore.QSize(300, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_mensaje2.setFont(font)
        self.LE_mensaje2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_mensaje2.setReadOnly(True)
        self.LE_mensaje2.setPlaceholderText("Notificacion")
        self.LE_mensaje2.setObjectName("LE_mensaje2")
        self.horizontalLayout_4.addWidget(self.LE_mensaje2)
        self.LE_fyh2 = QtWidgets.QLineEdit(self.F_notificacion2)
        self.LE_fyh2.setMinimumSize(QtCore.QSize(100, 31))
        self.LE_fyh2.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_fyh2.setFont(font)
        self.LE_fyh2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_fyh2.setReadOnly(True)
        self.LE_fyh2.setPlaceholderText("Fecha y hora")
        self.LE_fyh2.setObjectName("LE_fyh2")
        self.horizontalLayout_4.addWidget(self.LE_fyh2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.F_notificacion2)
        self.F_notificacion3 = QtWidgets.QFrame(self.SAWC_interfaz_a_n)
        self.F_notificacion3.setMinimumSize(QtCore.QSize(600, 70))
        self.F_notificacion3.setMaximumSize(QtCore.QSize(600, 70))
        self.F_notificacion3.setStyleSheet("QFrame {\n"
"    border-bottom: 1px solid #D5DBDB;\n"
"    background-color: transparent;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: #F8F9F9;\n"
"}")
        self.F_notificacion3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F_notificacion3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F_notificacion3.setObjectName("F_notificacion3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.F_notificacion3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(10, -1, 10, 5)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.L_ocupado = QtWidgets.QLabel(self.F_notificacion3)
        self.L_ocupado.setMinimumSize(QtCore.QSize(20, 20))
        self.L_ocupado.setMaximumSize(QtCore.QSize(20, 20))
        self.L_ocupado.setStyleSheet("QLabel{\n"
"    background-color: #F1948A;   \n"
"}")
        self.L_ocupado.setText("")
        self.L_ocupado.setScaledContents(True)
        self.L_ocupado.setWordWrap(False)
        self.L_ocupado.setObjectName("L_ocupado")
        self.horizontalLayout_6.addWidget(self.L_ocupado)
        self.LE_tipo3 = QtWidgets.QLineEdit(self.F_notificacion3)
        self.LE_tipo3.setMinimumSize(QtCore.QSize(100, 31))
        self.LE_tipo3.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_tipo3.setFont(font)
        self.LE_tipo3.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_tipo3.setReadOnly(True)
        self.LE_tipo3.setPlaceholderText("Tipo")
        self.LE_tipo3.setObjectName("LE_tipo3")
        self.horizontalLayout_6.addWidget(self.LE_tipo3)
        self.LE_mensaje3 = QtWidgets.QLineEdit(self.F_notificacion3)
        self.LE_mensaje3.setMinimumSize(QtCore.QSize(300, 31))
        self.LE_mensaje3.setMaximumSize(QtCore.QSize(300, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_mensaje3.setFont(font)
        self.LE_mensaje3.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_mensaje3.setReadOnly(True)
        self.LE_mensaje3.setPlaceholderText("Notificacion")
        self.LE_mensaje3.setObjectName("LE_mensaje3")
        self.horizontalLayout_6.addWidget(self.LE_mensaje3)
        self.LE_fyh3 = QtWidgets.QLineEdit(self.F_notificacion3)
        self.LE_fyh3.setMinimumSize(QtCore.QSize(100, 31))
        self.LE_fyh3.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_fyh3.setFont(font)
        self.LE_fyh3.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_fyh3.setReadOnly(True)
        self.LE_fyh3.setPlaceholderText("Fecha y hora")
        self.LE_fyh3.setObjectName("LE_fyh3")
        self.horizontalLayout_6.addWidget(self.LE_fyh3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.F_notificacion3)
        self.F_notificacion4 = QtWidgets.QFrame(self.SAWC_interfaz_a_n)
        self.F_notificacion4.setMinimumSize(QtCore.QSize(600, 70))
        self.F_notificacion4.setMaximumSize(QtCore.QSize(600, 70))
        self.F_notificacion4.setStyleSheet("QFrame {\n"
"    border-bottom: 1px solid #D5DBDB;\n"
"    background-color: transparent;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: #F8F9F9;\n"
"}")
        self.F_notificacion4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F_notificacion4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F_notificacion4.setObjectName("F_notificacion4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.F_notificacion4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(10, -1, 10, 5)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.L_limyman = QtWidgets.QLabel(self.F_notificacion4)
        self.L_limyman.setMinimumSize(QtCore.QSize(20, 20))
        self.L_limyman.setMaximumSize(QtCore.QSize(20, 20))
        self.L_limyman.setStyleSheet("QLabel{\n"
"    background-color: #F8C471;   \n"
"}")
        self.L_limyman.setText("")
        self.L_limyman.setScaledContents(True)
        self.L_limyman.setWordWrap(False)
        self.L_limyman.setObjectName("L_limyman")
        self.horizontalLayout_8.addWidget(self.L_limyman)
        self.LE_tipo4 = QtWidgets.QLineEdit(self.F_notificacion4)
        self.LE_tipo4.setMinimumSize(QtCore.QSize(100, 31))
        self.LE_tipo4.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_tipo4.setFont(font)
        self.LE_tipo4.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_tipo4.setReadOnly(True)
        self.LE_tipo4.setPlaceholderText("Tipo")
        self.LE_tipo4.setObjectName("LE_tipo4")
        self.horizontalLayout_8.addWidget(self.LE_tipo4)
        self.LE_mensaje4 = QtWidgets.QLineEdit(self.F_notificacion4)
        self.LE_mensaje4.setMinimumSize(QtCore.QSize(300, 31))
        self.LE_mensaje4.setMaximumSize(QtCore.QSize(300, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_mensaje4.setFont(font)
        self.LE_mensaje4.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_mensaje4.setReadOnly(True)
        self.LE_mensaje4.setPlaceholderText("Notificacion")
        self.LE_mensaje4.setObjectName("LE_mensaje4")
        self.horizontalLayout_8.addWidget(self.LE_mensaje4)
        self.LE_fyh4 = QtWidgets.QLineEdit(self.F_notificacion4)
        self.LE_fyh4.setMinimumSize(QtCore.QSize(100, 31))
        self.LE_fyh4.setMaximumSize(QtCore.QSize(80, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_fyh4.setFont(font)
        self.LE_fyh4.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_fyh4.setReadOnly(True)
        self.LE_fyh4.setPlaceholderText("Fecha y hora")
        self.LE_fyh4.setObjectName("LE_fyh4")
        self.horizontalLayout_8.addWidget(self.LE_fyh4)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addWidget(self.F_notificacion4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.SAWC_interfaz_a_n)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
