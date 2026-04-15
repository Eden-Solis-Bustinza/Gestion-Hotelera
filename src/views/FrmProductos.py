                       

                                                                      
 
                                             
 
                                                                           
                                                                       


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 600)
        Dialog.setMinimumSize(QtCore.QSize(950, 600))
        Dialog.setMaximumSize(QtCore.QSize(950, 600))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 951, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/images/imagen_login1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(150, 10, 661, 581))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("border-radius: 7px; background-color: #F4F6F6;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(330, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("assets/images/unnamed.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(360, 210, 121, 1))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.GB_venta_p = QtWidgets.QGroupBox(self.frame)
        self.GB_venta_p.setGeometry(QtCore.QRect(300, 180, 321, 371))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.GB_venta_p.setFont(font)
        self.GB_venta_p.setStyleSheet("QGroupBox {\n"
"    border: 2px solid Black;\n"
"    border-radius: 5px;\n"
"}")
        self.GB_venta_p.setObjectName("GB_venta_p")
        self.TW_productos = QtWidgets.QTableWidget(self.GB_venta_p)
        self.TW_productos.setGeometry(QtCore.QRect(10, 80, 301, 131))
        self.TW_productos.setStyleSheet("QHeaderView::section {\n"
"    background-color: #2C3E50;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: 1px solid #1A252F;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color: #1ABC9C;\n"
"}")
        self.TW_productos.setRowCount(3)
        self.TW_productos.setObjectName("TW_productos")
        self.TW_productos.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.TW_productos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TW_productos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TW_productos.setHorizontalHeaderItem(2, item)
        self.TW_productos.verticalHeader().setVisible(False)
        self.CB_producto_v = QtWidgets.QComboBox(self.GB_venta_p)
        self.CB_producto_v.setGeometry(QtCore.QRect(60, 30, 131, 31))
        self.CB_producto_v.setStyleSheet("QComboBox {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}\n"
"")
        self.CB_producto_v.setObjectName("CB_producto_v")
        self.label_11 = QtWidgets.QLabel(self.GB_venta_p)
        self.label_11.setGeometry(QtCore.QRect(20, 30, 31, 31))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("assets/icons/agregar-producto.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.GB_venta_p)
        self.label_12.setGeometry(QtCore.QRect(210, 30, 31, 31))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("assets/icons/cantidad.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.SB_cantidad = QtWidgets.QSpinBox(self.GB_venta_p)
        self.SB_cantidad.setGeometry(QtCore.QRect(250, 30, 51, 31))
        self.SB_cantidad.setStyleSheet("QSpinBox {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.SB_cantidad.setObjectName("SB_cantidad")
        self.LE_subtotal = QtWidgets.QLineEdit(self.GB_venta_p)
        self.LE_subtotal.setGeometry(QtCore.QRect(30, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_subtotal.setFont(font)
        self.LE_subtotal.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_subtotal.setPlaceholderText("Subtotal")
        self.LE_subtotal.setObjectName("LE_subtotal")
        self.LE_igv = QtWidgets.QLineEdit(self.GB_venta_p)
        self.LE_igv.setGeometry(QtCore.QRect(30, 330, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_igv.setFont(font)
        self.LE_igv.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_igv.setPlaceholderText("IGV")
        self.LE_igv.setObjectName("LE_igv")
        self.GB_metodo_pago = QtWidgets.QGroupBox(self.GB_venta_p)
        self.GB_metodo_pago.setGeometry(QtCore.QRect(10, 220, 301, 51))
        self.GB_metodo_pago.setObjectName("GB_metodo_pago")
        self.RB_inmediato = QtWidgets.QRadioButton(self.GB_metodo_pago)
        self.RB_inmediato.setGeometry(QtCore.QRect(40, 20, 82, 17))
        self.RB_inmediato.setObjectName("RB_inmediato")
        self.RB_alcheckout = QtWidgets.QRadioButton(self.GB_metodo_pago)
        self.RB_alcheckout.setGeometry(QtCore.QRect(180, 20, 82, 17))
        self.RB_alcheckout.setObjectName("RB_alcheckout")
        self.LE_total = QtWidgets.QLineEdit(self.GB_venta_p)
        self.LE_total.setGeometry(QtCore.QRect(180, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_total.setFont(font)
        self.LE_total.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_total.setPlaceholderText("Total")
        self.LE_total.setObjectName("LE_total")
        self.PB_pagar = QtWidgets.QPushButton(self.GB_venta_p)
        self.PB_pagar.setGeometry(QtCore.QRect(180, 330, 111, 31))
        self.PB_pagar.setStyleSheet("QPushButton {\n"
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
        self.PB_pagar.setObjectName("PB_pagar")
        self.GB_datos_cliente = QtWidgets.QGroupBox(self.frame)
        self.GB_datos_cliente.setGeometry(QtCore.QRect(30, 90, 591, 71))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.GB_datos_cliente.setFont(font)
        self.GB_datos_cliente.setStyleSheet("QGroupBox {\n"
"    border: 2px solid Black;\n"
"    border-radius: 5px;\n"
"}")
        self.GB_datos_cliente.setObjectName("GB_datos_cliente")
        self.LE_nombres_apellidos = QtWidgets.QLineEdit(self.GB_datos_cliente)
        self.LE_nombres_apellidos.setGeometry(QtCore.QRect(260, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_nombres_apellidos.setFont(font)
        self.LE_nombres_apellidos.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_nombres_apellidos.setPlaceholderText("Nombres y apellidos")
        self.LE_nombres_apellidos.setObjectName("LE_nombres_apellidos")
        self.label_8 = QtWidgets.QLabel(self.GB_datos_cliente)
        self.label_8.setGeometry(QtCore.QRect(220, 20, 31, 31))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("assets/icons/usuario (1).png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_18 = QtWidgets.QLabel(self.GB_datos_cliente)
        self.label_18.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("assets/icons/cama (1).png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.CB_numero_h = QtWidgets.QComboBox(self.GB_datos_cliente)
        self.CB_numero_h.setGeometry(QtCore.QRect(60, 20, 131, 31))
        self.CB_numero_h.setStyleSheet("QComboBox {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}\n"
"")
        self.CB_numero_h.setObjectName("CB_numero_h")
        self.LE_contacto = QtWidgets.QLineEdit(self.GB_datos_cliente)
        self.LE_contacto.setGeometry(QtCore.QRect(450, 20, 131, 31))
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
        self.label_9 = QtWidgets.QLabel(self.GB_datos_cliente)
        self.label_9.setGeometry(QtCore.QRect(410, 20, 31, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("assets/icons/llamada-telefonica.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.GB_inventario = QtWidgets.QGroupBox(self.frame)
        self.GB_inventario.setGeometry(QtCore.QRect(30, 180, 251, 151))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.GB_inventario.setFont(font)
        self.GB_inventario.setStyleSheet("QGroupBox {\n"
"    border: 2px solid Black;\n"
"    border-radius: 5px;\n"
"}")
        self.GB_inventario.setObjectName("GB_inventario")
        self.CB_categoria = QtWidgets.QComboBox(self.GB_inventario)
        self.CB_categoria.setGeometry(QtCore.QRect(100, 20, 131, 31))
        self.CB_categoria.setStyleSheet("QComboBox {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}\n"
"")
        self.CB_categoria.setObjectName("CB_categoria")
        self.CB_producto = QtWidgets.QComboBox(self.GB_inventario)
        self.CB_producto.setGeometry(QtCore.QRect(100, 60, 131, 31))
        self.CB_producto.setStyleSheet("QComboBox {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}\n"
"")
        self.CB_producto.setObjectName("CB_producto")
        self.label_15 = QtWidgets.QLabel(self.GB_inventario)
        self.label_15.setGeometry(QtCore.QRect(30, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_19 = QtWidgets.QLabel(self.GB_inventario)
        self.label_19.setGeometry(QtCore.QRect(30, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.LE_cantidad = QtWidgets.QLineEdit(self.GB_inventario)
        self.LE_cantidad.setGeometry(QtCore.QRect(100, 100, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_cantidad.setFont(font)
        self.LE_cantidad.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_cantidad.setReadOnly(True)
        self.LE_cantidad.setPlaceholderText("Cantidad de productos")
        self.LE_cantidad.setObjectName("LE_cantidad")
        self.label_22 = QtWidgets.QLabel(self.GB_inventario)
        self.label_22.setGeometry(QtCore.QRect(30, 100, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.GB_agregar_p = QtWidgets.QGroupBox(self.frame)
        self.GB_agregar_p.setGeometry(QtCore.QRect(30, 340, 251, 211))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.GB_agregar_p.setFont(font)
        self.GB_agregar_p.setStyleSheet("QGroupBox {\n"
"    border: 2px solid Black;\n"
"    border-radius: 5px;\n"
"}")
        self.GB_agregar_p.setObjectName("GB_agregar_p")
        self.CB_categoria_2 = QtWidgets.QComboBox(self.GB_agregar_p)
        self.CB_categoria_2.setGeometry(QtCore.QRect(100, 20, 131, 31))
        self.CB_categoria_2.setStyleSheet("QComboBox {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}\n"
"")
        self.CB_categoria_2.setObjectName("CB_categoria_2")
        self.label_20 = QtWidgets.QLabel(self.GB_agregar_p)
        self.label_20.setGeometry(QtCore.QRect(30, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.GB_agregar_p)
        self.label_21.setGeometry(QtCore.QRect(30, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.LE_producto = QtWidgets.QLineEdit(self.GB_agregar_p)
        self.LE_producto.setGeometry(QtCore.QRect(100, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_producto.setFont(font)
        self.LE_producto.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_producto.setPlaceholderText("Nombre del producto")
        self.LE_producto.setObjectName("LE_producto")
        self.label_23 = QtWidgets.QLabel(self.GB_agregar_p)
        self.label_23.setGeometry(QtCore.QRect(30, 100, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.LE_cantidad_2 = QtWidgets.QLineEdit(self.GB_agregar_p)
        self.LE_cantidad_2.setGeometry(QtCore.QRect(100, 100, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.LE_cantidad_2.setFont(font)
        self.LE_cantidad_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D5DBDB;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2C3E50;\n"
"}")
        self.LE_cantidad_2.setPlaceholderText("Agregar cantidad")
        self.LE_cantidad_2.setObjectName("LE_cantidad_2")
        self.PB_cargar = QtWidgets.QPushButton(self.GB_agregar_p)
        self.PB_cargar.setGeometry(QtCore.QRect(80, 150, 81, 31))
        self.PB_cargar.setStyleSheet("QPushButton {\n"
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
        self.PB_cargar.setObjectName("PB_cargar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "PRODUCTOS"))
        self.GB_venta_p.setTitle(_translate("Dialog", "Venta de productos"))
        item = self.TW_productos.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Producto"))
        item = self.TW_productos.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Cantidad"))
        item = self.TW_productos.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Subtotal"))
        self.GB_metodo_pago.setTitle(_translate("Dialog", "Metodo de pago"))
        self.RB_inmediato.setText(_translate("Dialog", "Inmediato"))
        self.RB_alcheckout.setText(_translate("Dialog", "Al check-out"))
        self.PB_pagar.setText(_translate("Dialog", "PAGAR"))
        self.GB_datos_cliente.setTitle(_translate("Dialog", "Datos del cliente:"))
        self.GB_inventario.setTitle(_translate("Dialog", "Inventario"))
        self.label_15.setText(_translate("Dialog", "Categoria:"))
        self.label_19.setText(_translate("Dialog", "Producto"))
        self.label_22.setText(_translate("Dialog", "Cantidad"))
        self.GB_agregar_p.setTitle(_translate("Dialog", "Agregar producto"))
        self.label_20.setText(_translate("Dialog", "Categoria:"))
        self.label_21.setText(_translate("Dialog", "Producto"))
        self.label_23.setText(_translate("Dialog", "Cantidad"))
        self.PB_cargar.setText(_translate("Dialog", "CARGAR"))
