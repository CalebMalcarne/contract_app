'''
Created By: Caleb Malcarne
Program: Invoice Filler 


'''

from PyQt5 import QtCore, QtGui, QtWidgets


class ImageInfo(object):
    def setupUi(self, Form, main, imageName, width, height, dir):
        self.main = main
        self.name = imageName
        self.width = width
        self.height = height
        self.dir = dir
        
        Form.setObjectName("Form")
        Form.resize(425, 490)
        Form.setFixedSize(425, 490)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 420, 100, 60))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 401, 400))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 0, 1, 2)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 2, 1, 1)
        
        
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 3, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 4, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 6, 0, 1, 4)
        
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 3, 2, 1, 1)
        self.radioButton_3.setText("Keep Size")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.lineEdit_3.setText(self.name)
        self.lineEdit_2.setText(str(self.width))
        self.lineEdit.setText(str(self.height))
        self.radioButton.nextCheckState()
        self.pushButton.clicked.connect(lambda: self.submitData(Form))
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.radioButton_2.setText(_translate("Form", "Custom Size"))
        self.label.setText(_translate("Form", "Description"))
        self.label_3.setText(_translate("Form", "Width"))
        self.radioButton.setText(_translate("Form", "Auto-Resize"))
        self.label_2.setText(_translate("Form", "Length"))
        self.label_4.setText(_translate("Form", "Image Title"))
        
    def submitData(self, Form):
        data = [self.lineEdit_3.text(),self.lineEdit_2.text(),self.lineEdit.text(),
               self.textEdit.toPlainText(), self.radioButton.isChecked(), self.radioButton_2.isChecked(), self.radioButton_3]
        
        self.main.saveImage(data, self.dir)
        self.main.updateImageText()
        Form.close()
        
        
        #test
