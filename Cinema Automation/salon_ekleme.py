# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'salon_ekleme.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_salon_ekleme(object):
    def setupUi(self, salon_ekleme):
        salon_ekleme.setObjectName("salon_ekleme")
        salon_ekleme.resize(494, 305)
        salon_ekleme.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.salon_ekleme_paneli = QtWidgets.QLabel(salon_ekleme)
        self.salon_ekleme_paneli.setGeometry(QtCore.QRect(90, 60, 331, 31))
        self.salon_ekleme_paneli.setStyleSheet("padding-left:35px;\n"
"font-weight:bold;\n"
"font-size:21px;\n"
"color:white;\n"
"")
        self.salon_ekleme_paneli.setObjectName("salon_ekleme_paneli")
        self.salon_adi = QtWidgets.QLabel(salon_ekleme)
        self.salon_adi.setGeometry(QtCore.QRect(90, 120, 101, 16))
        self.salon_adi.setStyleSheet("color:white;\n"
"font-size:20px;\n"
"")
        self.salon_adi.setObjectName("salon_adi")
        self.salon_adi_edit = QtWidgets.QLineEdit(salon_ekleme)
        self.salon_adi_edit.setGeometry(QtCore.QRect(190, 120, 161, 21))
        self.salon_adi_edit.setObjectName("salon_adi_edit")
        self.ana_menu_button = QtWidgets.QPushButton(salon_ekleme)
        self.ana_menu_button.setGeometry(QtCore.QRect(30, 240, 207, 33))
        self.ana_menu_button.setStyleSheet("background-color:white;font-size:15px;color:red;font-weight:bold;font-style:italic;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ana_menu_button.setIcon(icon)
        self.ana_menu_button.setIconSize(QtCore.QSize(25, 25))
        self.ana_menu_button.setObjectName("ana_menu_button")
        self.cikisButton = QtWidgets.QPushButton(salon_ekleme)
        self.cikisButton.setGeometry(QtCore.QRect(240, 240, 206, 33))
        self.cikisButton.setStyleSheet("background-color:white;font-size:15px;color:red;font-weight:bold;font-style:italic;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cikisButton.setIcon(icon1)
        self.cikisButton.setIconSize(QtCore.QSize(25, 25))
        self.cikisButton.setObjectName("cikisButton")
        self.salon_ekle_button_2 = QtWidgets.QPushButton(salon_ekleme)
        self.salon_ekle_button_2.setGeometry(QtCore.QRect(30, 190, 421, 33))
        self.salon_ekle_button_2.setStyleSheet("background-color:white; \n"
"color:red;\n"
"font-size:15px;font-style:italic;font-weight:bold;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salon_ekle_button_2.setIcon(icon2)
        self.salon_ekle_button_2.setIconSize(QtCore.QSize(25, 25))
        self.salon_ekle_button_2.setObjectName("salon_ekle_button_2")

        self.retranslateUi(salon_ekleme)
        QtCore.QMetaObject.connectSlotsByName(salon_ekleme)

    def retranslateUi(self, salon_ekleme):
        _translate = QtCore.QCoreApplication.translate
        salon_ekleme.setWindowTitle(_translate("salon_ekleme", "Salon Ekle"))
        self.salon_ekleme_paneli.setText(_translate("salon_ekleme", "Salon Ekleme Paneli"))
        self.salon_adi.setText(_translate("salon_ekleme", "Salon Adı:"))
        self.ana_menu_button.setText(_translate("salon_ekleme", "Ana Menü"))
        self.cikisButton.setText(_translate("salon_ekleme", "Çıkış"))
        self.salon_ekle_button_2.setText(_translate("salon_ekleme", "Salon Ekle"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    salon_ekleme = QtWidgets.QDialog()
    ui = Ui_salon_ekleme()
    ui.setupUi(salon_ekleme)
    salon_ekleme.show()
    sys.exit(app.exec_())
