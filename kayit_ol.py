# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayit_ol.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KAYITOL(object):
    def setupUi(self, KAYITOL):
        KAYITOL.setObjectName("KAYITOL")
        KAYITOL.setEnabled(True)
        KAYITOL.resize(485, 506)
        KAYITOL.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.formLayoutWidget = QtWidgets.QWidget(KAYITOL)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(KAYITOL)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 376, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(KAYITOL)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 371, 22))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.formLayoutWidget_2 = QtWidgets.QWidget(KAYITOL)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 341, 106))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.textEdit = QtWidgets.QTextEdit(KAYITOL)
        self.textEdit.setGeometry(QtCore.QRect(30, 250, 391, 171))
        self.textEdit.setObjectName("textEdit")
        self.KayitOl = QtWidgets.QDialogButtonBox(KAYITOL)
        self.KayitOl.setGeometry(QtCore.QRect(150, 450, 156, 23))
        self.KayitOl.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.KayitOl.setObjectName("KayitOl")
        self.checkBox_3 = QtWidgets.QCheckBox(KAYITOL)
        self.checkBox_3.setGeometry(QtCore.QRect(260, 400, 144, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.frame = QtWidgets.QFrame(KAYITOL)
        self.frame.setGeometry(QtCore.QRect(330, 10, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.label_3.raise_()
        self.formLayoutWidget_2.raise_()
        self.textEdit.raise_()
        self.KayitOl.raise_()
        self.checkBox.raise_()
        self.checkBox_3.raise_()
        self.frame.raise_()

        self.retranslateUi(KAYITOL)
        QtCore.QMetaObject.connectSlotsByName(KAYITOL)

    def retranslateUi(self, KAYITOL):
        _translate = QtCore.QCoreApplication.translate
        KAYITOL.setWindowTitle(_translate("KAYITOL", "KAYIT OL"))
        self.label.setText(_translate("KAYITOL", "ISIM:"))
        self.label_2.setText(_translate("KAYITOL", "SOYISIM:"))
        self.label_3.setText(_translate("KAYITOL", "CINSIYET:"))
        self.radioButton.setText(_translate("KAYITOL", "Kadin"))
        self.radioButton_3.setText(_translate("KAYITOL", "Erkek"))
        self.label_4.setText(_translate("KAYITOL", "MEDENI DURUM:"))
        self.checkBox_2.setText(_translate("KAYITOL", "Evli"))
        self.checkBox.setText(_translate("KAYITOL", "Bekar"))
        self.label_5.setText(_translate("KAYITOL", "MAIL:"))
        self.label_6.setText(_translate("KAYITOL", "MAIL TEKRAR:"))
        self.label_7.setText(_translate("KAYITOL", "SIFRE:"))
        self.label_8.setText(_translate("KAYITOL", "SIFRE TEKRAR:"))
        self.textEdit.setHtml(_translate("KAYITOL", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">UYELIK SOZLESMESI</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Alisveris sitemize uye olmak icin uye islemleri sayfasinda yer alan uye bilgilerinin doldurulmasi gerekmektedir.Bu bilgilerin iletisim ve ulasim icin kullanilacagi bilinerek dogru ve eksiksiz doldurulmalidir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Isbu uyelik sozlemesinin kabul edilmesiyle birlikte, kosullarin anlasildigi, kullanici olarak sitede sunulan hizmetlerden yararlanirken sartlara tabi oldugunuzu kabul etmis sayilirsiniz.Ancak sitesye uye olmaniz herhangi bir yukumluluk altina girdiginiz anlamina gelmemektedir. Dilediginiz zaman uyeliginizi sonlandirabilirsiniz.</span></p></body></html>"))
        self.checkBox_3.setText(_translate("KAYITOL", "Okudum,onayliyorum"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KAYITOL = QtWidgets.QWidget()
    ui = Ui_KAYITOL()
    ui.setupUi(KAYITOL)
    KAYITOL.show()
    sys.exit(app.exec_())
