# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_Registration_Form.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(801, 709)
        Dialog.setStyleSheet("background-color: rgb(213, 248, 232)")
        self.uName_label = QtWidgets.QLabel(Dialog)
        self.uName_label.setGeometry(QtCore.QRect(50, 120, 121, 16))
        self.uName_label.setStyleSheet("color: #33423B")
        self.uName_label.setObjectName("uName_label")
        self.firstName_label = QtWidgets.QLabel(Dialog)
        self.firstName_label.setGeometry(QtCore.QRect(50, 170, 91, 16))
        self.firstName_label.setStyleSheet("color: #33423B")
        self.firstName_label.setObjectName("firstName_label")
        self.gender_label = QtWidgets.QLabel(Dialog)
        self.gender_label.setGeometry(QtCore.QRect(50, 420, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gender_label.setFont(font)
        self.gender_label.setStyleSheet("color: #B84C6F")
        self.gender_label.setObjectName("gender_label")
        self.maritalStatus_label = QtWidgets.QLabel(Dialog)
        self.maritalStatus_label.setGeometry(QtCore.QRect(50, 480, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maritalStatus_label.setFont(font)
        self.maritalStatus_label.setStyleSheet("color: #B84C6F")
        self.maritalStatus_label.setObjectName("maritalStatus_label")
        self.lastName_label = QtWidgets.QLabel(Dialog)
        self.lastName_label.setGeometry(QtCore.QRect(50, 220, 91, 16))
        self.lastName_label.setStyleSheet("color: #33423B")
        self.lastName_label.setObjectName("lastName_label")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(50, 270, 81, 16))
        self.password_label.setStyleSheet("color: #33423B")
        self.password_label.setObjectName("password_label")
        self.rePassword_label = QtWidgets.QLabel(Dialog)
        self.rePassword_label.setGeometry(QtCore.QRect(50, 320, 111, 16))
        self.rePassword_label.setStyleSheet("color: #33423B")
        self.rePassword_label.setObjectName("rePassword_label")
        self.uName_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uName_lineEdit.setGeometry(QtCore.QRect(50, 140, 291, 21))
        self.uName_lineEdit.setStyleSheet("background-color: white")
        self.uName_lineEdit.setObjectName("uName_lineEdit")
        self.firstName_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.firstName_lineEdit.setGeometry(QtCore.QRect(50, 190, 291, 21))
        self.firstName_lineEdit.setStyleSheet("background-color: white")
        self.firstName_lineEdit.setObjectName("firstName_lineEdit")
        self.lastName_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lastName_lineEdit.setGeometry(QtCore.QRect(50, 240, 291, 21))
        self.lastName_lineEdit.setStyleSheet("background-color: white")
        self.lastName_lineEdit.setObjectName("lastName_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(50, 290, 291, 21))
        self.password_lineEdit.setStyleSheet("background-color: white")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.rePassword_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.rePassword_lineEdit.setGeometry(QtCore.QRect(50, 340, 291, 21))
        self.rePassword_lineEdit.setStyleSheet("background-color: white")
        self.rePassword_lineEdit.setObjectName("rePassword_lineEdit")
        self.uRegForm_label = QtWidgets.QLabel(Dialog)
        self.uRegForm_label.setGeometry(QtCore.QRect(50, 30, 681, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.uRegForm_label.setFont(font)
        self.uRegForm_label.setStyleSheet("color: #8E1F42")
        self.uRegForm_label.setObjectName("uRegForm_label")
        self.account_label = QtWidgets.QLabel(Dialog)
        self.account_label.setGeometry(QtCore.QRect(50, 90, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.account_label.setFont(font)
        self.account_label.setStyleSheet("color: #B84C6F")
        self.account_label.setObjectName("account_label")
        self.contactInfo_label = QtWidgets.QLabel(Dialog)
        self.contactInfo_label.setGeometry(QtCore.QRect(440, 90, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.contactInfo_label.setFont(font)
        self.contactInfo_label.setStyleSheet("color: #B84C6F")
        self.contactInfo_label.setObjectName("contactInfo_label")
        self.pir_pol_textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.pir_pol_textBrowser.setGeometry(QtCore.QRect(470, 390, 271, 81))
        self.pir_pol_textBrowser.setStyleSheet("background-color: white; color: #33423B")
        self.pir_pol_textBrowser.setObjectName("pir_pol_textBrowser")
        self.gen_female_radioButton = QtWidgets.QRadioButton(Dialog)
        self.gen_female_radioButton.setGeometry(QtCore.QRect(130, 440, 71, 20))
        self.gen_female_radioButton.setStyleSheet("color: #33423B")
        self.gen_female_radioButton.setObjectName("gen_female_radioButton")
        self.gen_male_radioButton = QtWidgets.QRadioButton(Dialog)
        self.gen_male_radioButton.setGeometry(QtCore.QRect(50, 440, 71, 20))
        self.gen_male_radioButton.setStyleSheet("color: #33423B")
        self.gen_male_radioButton.setObjectName("gen_male_radioButton")
        self.gen_prefNotToSay_radioButton = QtWidgets.QRadioButton(Dialog)
        self.gen_prefNotToSay_radioButton.setGeometry(QtCore.QRect(210, 440, 131, 20))
        self.gen_prefNotToSay_radioButton.setStyleSheet("color: #33423B")
        self.gen_prefNotToSay_radioButton.setObjectName("gen_prefNotToSay_radioButton")
        self.ms_single_radioButton = QtWidgets.QRadioButton(Dialog)
        self.ms_single_radioButton.setGeometry(QtCore.QRect(130, 500, 61, 20))
        self.ms_single_radioButton.setStyleSheet("color: #33423B")
        self.ms_single_radioButton.setObjectName("ms_single_radioButton")
        self.ms_married_radioButton = QtWidgets.QRadioButton(Dialog)
        self.ms_married_radioButton.setGeometry(QtCore.QRect(50, 500, 71, 20))
        self.ms_married_radioButton.setStyleSheet("color: #33423B")
        self.ms_married_radioButton.setObjectName("ms_married_radioButton")
        self.ms_prefNotToSay_radioButton = QtWidgets.QRadioButton(Dialog)
        self.ms_prefNotToSay_radioButton.setGeometry(QtCore.QRect(210, 500, 131, 20))
        self.ms_prefNotToSay_radioButton.setStyleSheet("color: #33423B")
        self.ms_prefNotToSay_radioButton.setObjectName("ms_prefNotToSay_radioButton")
        self.cellPhone_label = QtWidgets.QLabel(Dialog)
        self.cellPhone_label.setGeometry(QtCore.QRect(440, 220, 91, 16))
        self.cellPhone_label.setStyleSheet("color: #33423B")
        self.cellPhone_label.setObjectName("cellPhone_label")
        self.country_label = QtWidgets.QLabel(Dialog)
        self.country_label.setGeometry(QtCore.QRect(440, 320, 81, 16))
        self.country_label.setStyleSheet("color: #33423B")
        self.country_label.setObjectName("country_label")
        self.reEmail_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.reEmail_lineEdit.setGeometry(QtCore.QRect(440, 190, 291, 21))
        self.reEmail_lineEdit.setStyleSheet("background-color: white")
        self.reEmail_lineEdit.setObjectName("reEmail_lineEdit")
        self.email_label = QtWidgets.QLabel(Dialog)
        self.email_label.setGeometry(QtCore.QRect(440, 120, 81, 16))
        self.email_label.setStyleSheet("color: #33423B")
        self.email_label.setObjectName("email_label")
        self.reEmail_label = QtWidgets.QLabel(Dialog)
        self.reEmail_label.setGeometry(QtCore.QRect(440, 170, 91, 16))
        self.reEmail_label.setStyleSheet("color: #33423B")
        self.reEmail_label.setObjectName("reEmail_label")
        self.workPhone_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.workPhone_lineEdit.setGeometry(QtCore.QRect(440, 290, 291, 21))
        self.workPhone_lineEdit.setStyleSheet("background-color: white")
        self.workPhone_lineEdit.setObjectName("workPhone_lineEdit")
        self.city_label = QtWidgets.QLabel(Dialog)
        self.city_label.setGeometry(QtCore.QRect(600, 320, 31, 16))
        self.city_label.setStyleSheet("color: #33423B")
        self.city_label.setObjectName("city_label")
        self.email_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(440, 140, 291, 21))
        self.email_lineEdit.setStyleSheet("background-color: white")
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.workPhone_label = QtWidgets.QLabel(Dialog)
        self.workPhone_label.setGeometry(QtCore.QRect(440, 270, 101, 16))
        self.workPhone_label.setStyleSheet("color: #33423B")
        self.workPhone_label.setObjectName("workPhone_label")
        self.cellPhone_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.cellPhone_lineEdit.setGeometry(QtCore.QRect(440, 240, 291, 21))
        self.cellPhone_lineEdit.setStyleSheet("background-color: white")
        self.cellPhone_lineEdit.setObjectName("cellPhone_lineEdit")
        self.country_comboBox = QtWidgets.QComboBox(Dialog)
        self.country_comboBox.setGeometry(QtCore.QRect(440, 340, 141, 26))
        self.country_comboBox.setStyleSheet("background-color: white; color: #33423B")
        self.country_comboBox.setObjectName("country_comboBox")
        self.country_comboBox.addItem("")
        self.city_comboBox = QtWidgets.QComboBox(Dialog)
        self.city_comboBox.setGeometry(QtCore.QRect(600, 340, 131, 26))
        self.city_comboBox.setStyleSheet("background-color: white; color: #33423B")
        self.city_comboBox.setObjectName("city_comboBox")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.city_comboBox.addItem("")
        self.personal_info_label = QtWidgets.QLabel(Dialog)
        self.personal_info_label.setGeometry(QtCore.QRect(50, 390, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.personal_info_label.setFont(font)
        self.personal_info_label.setStyleSheet("color: #B84C6F")
        self.personal_info_label.setObjectName("personal_info_label")
        self.i_agree_checkBox = QtWidgets.QCheckBox(Dialog)
        self.i_agree_checkBox.setGeometry(QtCore.QRect(440, 390, 21, 20))
        self.i_agree_checkBox.setText("")
        self.i_agree_checkBox.setObjectName("i_agree_checkBox")
        self.singUp_button = QtWidgets.QPushButton(Dialog)
        self.singUp_button.setGeometry(QtCore.QRect(440, 480, 191, 41))
        font = QtGui.QFont()
        font.setFamily(".SF NS Display")
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.singUp_button.setFont(font)
        self.singUp_button.setMouseTracking(True)
        self.singUp_button.setStyleSheet("background-color: #B84C6F; color: silver")
        self.singUp_button.setObjectName("singUp_button")
        # ############ Sign Up Button Event ######################
        self.singUp_button.clicked.connect(self.signUp_btn_event)
        # ########################################################
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(640, 480, 111, 41))
        font = QtGui.QFont()
        font.setFamily(".SF NS Display")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cancel_button.setFont(font)
        self.cancel_button.setMouseTracking(True)
        self.cancel_button.setStyleSheet("background-color: rgb(240, 170, 201); color: #8F6F79")
        self.cancel_button.setObjectName("cancel_button")
        # ############ Cancel Button Event ######################
        self.cancel_button.clicked.connect(self.cancel_btn_event)
        # ########################################################

        self.button_click_text_area = QtWidgets.QLabel(Dialog)
        self.button_click_text_area.setGeometry(QtCore.QRect(50, 550, 701, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.button_click_text_area.setFont(font)
        self.button_click_text_area.setStyleSheet("color: #B84C6F; text-align: center")
        self.button_click_text_area.setText("")
        self.button_click_text_area.setObjectName("button_click_text_area")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def signUp_btn_event(self):
        self.button_click_text_area.setText("Your account is created!")

    def cancel_btn_event(self):
        self.button_click_text_area.setText("You canceled your registration!")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.uName_label.setText(_translate("Dialog", "Username (E-mail)"))
        self.firstName_label.setText(_translate("Dialog", "First Name (*)"))
        self.gender_label.setText(_translate("Dialog", "Gender"))
        self.maritalStatus_label.setText(_translate("Dialog", "Marital Status"))
        self.lastName_label.setText(_translate("Dialog", "Last Name (*)"))
        self.password_label.setText(_translate("Dialog", "Password"))
        self.rePassword_label.setText(_translate("Dialog", "Retype Password"))
        self.uRegForm_label.setText(_translate("Dialog", "USER REGISTRATION FORM"))
        self.account_label.setText(_translate("Dialog", "Account"))
        self.contactInfo_label.setText(_translate("Dialog", "Contact Information"))
        self.pir_pol_textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">By clicking this checkbox, you agree to our Terms. Learn how we collect, use and share your data in our Data Policy and how we use cookies and similar technology in our Cookies Policy. You may receive SMS Notifications from us and can opt out any time.</span></p></body></html>"))
        self.gen_female_radioButton.setText(_translate("Dialog", "Female"))
        self.gen_male_radioButton.setText(_translate("Dialog", "Male"))
        self.gen_prefNotToSay_radioButton.setText(_translate("Dialog", "Prefer not to say"))
        self.ms_single_radioButton.setText(_translate("Dialog", "Single"))
        self.ms_married_radioButton.setText(_translate("Dialog", "Married"))
        self.ms_prefNotToSay_radioButton.setText(_translate("Dialog", "Prefer not to say"))
        self.cellPhone_label.setText(_translate("Dialog", "Cell Phone No"))
        self.country_label.setText(_translate("Dialog", "Country"))
        self.email_label.setText(_translate("Dialog", "E-Mail"))
        self.reEmail_label.setText(_translate("Dialog", "Retype E-Mail"))
        self.city_label.setText(_translate("Dialog", "City"))
        self.workPhone_label.setText(_translate("Dialog", "Work Phone No"))
        self.country_comboBox.setItemText(0, _translate("Dialog", "Netherlands"))
        self.city_comboBox.setItemText(0, _translate("Dialog", "Almere"))
        self.city_comboBox.setItemText(1, _translate("Dialog", "Amsterdam"))
        self.city_comboBox.setItemText(2, _translate("Dialog", "Breda"))
        self.city_comboBox.setItemText(3, _translate("Dialog", "Eindhoven"))
        self.city_comboBox.setItemText(4, _translate("Dialog", "Groningen"))
        self.city_comboBox.setItemText(5, _translate("Dialog", "Nijmegen"))
        self.city_comboBox.setItemText(6, _translate("Dialog", "Rotterdam"))
        self.city_comboBox.setItemText(7, _translate("Dialog", "The Hague"))
        self.city_comboBox.setItemText(8, _translate("Dialog", "Tilburg"))
        self.city_comboBox.setItemText(9, _translate("Dialog", "Utrecht"))
        self.personal_info_label.setText(_translate("Dialog", "Personal Information"))
        self.singUp_button.setText(_translate("Dialog", "Sign Up"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())