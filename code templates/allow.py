import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from globals import *


class Allowance(QtWidgets.QMainWindow):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, parent = None):
        super().__init__()
        self.parent = parent
        
        
        self.setObjectName("Dialog")
        self.resize(420, 224)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(50, 180, 321, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(10, 10, 400, 161))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.retranslateUi()
        #self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(lambda: self.close())
        self.buttonBox.accepted.connect(lambda: self.add_allowance()) 
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Allowance Type"))
        self.label_2.setText(_translate("Dialog", "Allowance Amount"))
        
    def close(self):
        self.close()
        
    def add_allowance(self):
        type = self.lineEdit.text()
        amount = self.lineEdit_2.text()
        allowances[type] = amount
        print(allowances)
        self.update_allow_text()
        
    def update_allow_text(self):
        temp_ = ""
        for i in allowances:
            temp = f"{i}, {allowances[i]} \n"
            temp_ += temp
        
        print(temp_)
                   
        