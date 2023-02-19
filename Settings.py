'''
Created By: Caleb Malcarne
Program: Invoice Filler 


'''


from PyQt5 import QtCore, QtGui, QtWidgets
from edit_Config import *

class settingsWindow(object):
    def setupUi(self, Form, main):
        
        self.config = getConfigData()
        self.main = main
        
        Form.setObjectName("Form")
        Form.setFixedSize(540, 350)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 10, 500, 300))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 2, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 2, 1, 3)
        
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 4, 3, 1, 1)
        
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 2)
        
        self.horizontalSlider = QtWidgets.QSlider(self.widget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(int(self.config["deposit_percent"]))
        
        self.gridLayout.addWidget(self.horizontalSlider, 5, 2, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 3)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.horizontalSlider.valueChanged.connect(self.updatePercent)

    def updatePercent(self):
        self.lineEdit_6.setText(str(self.horizontalSlider.value()))
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.clicked.connect(lambda: self.saveConfig(Form))
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Window Size"))
        self.comboBox.setItemText(0, _translate("Form", "Large"))
        self.comboBox.setItemText(1, _translate("Form", "Medium"))
        self.comboBox.setItemText(2, _translate("Form", "Small"))
        self.label_3.setText(_translate("Form", "Template Path"))
        self.label_5.setText(_translate("Form", "Image Size Threshold"))
        self.lineEdit_6.setText(_translate("Form", self.config["deposit_percent"]))
        self.label_7.setText(_translate("Form", "%"))
        self.label_4.setText(_translate("Form", "Default Deposit Percentage"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.label.setText(_translate("Form", "Settings"))
        self.lineEdit.setText(self.config["template_path"])
        self.lineEdit_2.setText(self.config["image_size_thresh"])
        self.comboBox.setCurrentText(self.config["window_size"])
        
    def saveConfig(self, Form):
        templatePath = self.lineEdit.text()
        threshold = self.lineEdit_2.text()
        deposit_percent = self.lineEdit_6.text()
        windowSize = self.comboBox.currentText()
        
        self.config["template_path"] = templatePath
        self.config["window_size"] = windowSize
        self.config["image_size_thresh"] = threshold
        self.config["deposit_percent"] = deposit_percent
        
        writeConfigData(self.config)
        self.main.resizeWindow(windowSize)
        Form.close()
        
    
