import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from globals import *
from datetime import date
from document import doc
from imageInfoPy import ImageInfo
from imageObj import image
from PIL import Image



class MainWindow(QtWidgets.QMainWindow):  
    
    def __init__(self):
        super().__init__()
        
        self.setAcceptDrops(True)
        self.setObjectName("MainWindow")
        self.resize(390, 1100)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 0, 350, 1000))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 11, 3, 1, 3)
        
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)        
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 5, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 8, 3, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 10, 3, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 14, 3, 5, 3)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 6, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 3)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 11, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 5)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 4)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 5, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 4)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 9, 0, 1, 6)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 7, 5, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 5, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 30, 0, 4, 6)
        self.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 265, 22))
        self.menubar.setObjectName("menubar")
        self.menuDocument_Maker = QtWidgets.QMenu(self.menubar)
        self.menuDocument_Maker.setObjectName("menuDocument_Maker")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionExport = QtWidgets.QAction(self)
        self.actionExport.setObjectName("actionExport")
        self.actionSettings = QtWidgets.QAction(self)
        self.actionSettings.setObjectName("actionSettings")
        self.menuDocument_Maker.addAction(self.actionExport)
        self.menuDocument_Maker.addAction(self.actionSettings)
        self.menubar.addAction(self.menuDocument_Maker.menuAction())
        
        self.label.setBuddy(self.lineEdit)
        self.label_9.setBuddy(self.checkBox)
        self.label_2.setBuddy(self.lineEdit_2)
        self.label_10.setBuddy(self.lineEdit_8)
        self.label_7.setBuddy(self.lineEdit_6)
        self.label_5.setBuddy(self.lineEdit_4)
        self.label_3.setBuddy(self.lineEdit_3)
        self.label_8.setBuddy(self.lineEdit_7)
        self.label_6.setBuddy(self.lineEdit_5)
                  

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.lineEdit, self.lineEdit_2)
        self.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        self.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        self.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        self.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        self.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        self.setTabOrder(self.lineEdit_7, self.checkBox)
        self.setTabOrder(self.checkBox, self.lineEdit_8)
        self.setTabOrder(self.lineEdit_8, self.textEdit)
        self.setTabOrder(self.textEdit, self.textEdit_2)
        self.setTabOrder(self.textEdit_2, self.pushButton_2)
        self.setTabOrder(self.pushButton_2, self.textEdit_3)  

    def retranslateUi(self, MainWindow):
        self.actionExport.triggered.connect(lambda: self.exportDoc())
        self.pushButton_2.clicked.connect(lambda: self.addImage())
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Date"))
        self.label_9.setText(_translate("MainWindow", "Is Time important"))
        self.label_2.setText(_translate("MainWindow", "Client"))
        self.label_5.setText(_translate("MainWindow", "Start Date"))
        self.label_7.setText(_translate("MainWindow", "estimate Amount"))
        self.label_6.setText(_translate("MainWindow", "End Date"))
        self.label_3.setText(_translate("MainWindow", "Estimate Number"))
        self.label_8.setText(_translate("MainWindow", "Hourly Rate"))
        self.label_13.setText(_translate("MainWindow", "                 Allowances"))
        self.label_4.setText(_translate("MainWindow", "          type"))
        self.label_12.setText(_translate("MainWindow", "        Cost"))
        self.pushButton_2.setText(_translate("MainWindow", "Add image"))
        self.label_10.setText(_translate("MainWindow", "Deposit"))
        self.menuDocument_Maker.setTitle(_translate("MainWindow", "file"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
 
    def exportDoc(self):
        
        data = [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), 
                self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text(),
                self.checkBox.checkState(), self.lineEdit_7.text(), self.lineEdit_8.text()]
        
        print(data)
        
        if data[0] == '':
            data[0] = (str(date.today().strftime("%m-%d-%Y"))).replace('-', '/')  
        

        type = self.textEdit.toPlainText().split('\n')
        amount = self.textEdit_2.toPlainText().split('\n')
        
        allowanceData = [[type[x], amount[x]] for x in range(min(len(type), len(amount)))]
        
        for sublist in allowanceData:
            if sublist[0] == '':
                sublist[0] = "No Data"
            if sublist[1] == '':
                sublist[1] = "No Data"

        out_path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(out_path)
        export = doc(data, allowanceData, out_path)
        if(len(out_path) > 0 ):
            export.fill_contract()
   
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
            
    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for path in files:
            img = Image.open(path)
            split = path.split('/')
            image_name = split[len(split) - 1].split('.')[0]    
            self.ImageWindow(image_name, img.size[1], img.size[0], path)

    def updateImageText(self):
        imageText = ""
        for image in images:
            imageText += f"{image}\n"
        self.textEdit_3.setText(imageText)
                
    def addImage(self):
        global images 
        image_path = str(QtWidgets.QFileDialog.getOpenFileName(self, "Select Image"))
        
        cut_path = image_path.split(',')[0][2:len((image_path.split(',')[0])) - 1]
        split = cut_path.split('/')
        image_name = split[len(split) - 1].split('.')[0]
        
        if cut_path != '':
         img = Image.open(cut_path)  
         self.ImageWindow(image_name, img.size[1], img.size[0], cut_path)
    
    def ImageWindow(self, imageName, width, height, dir):
        self.img_window = QtWidgets.QMainWindow()
        self.ui = ImageInfo()
        self.ui.setupUi(self.img_window, self, imageName, width, height, dir)
        self.img_window.show()
    
    def saveImage(self, data, dir, window):
        global imageLis
        autoResize = data[4]
        customeSize = data[5]
        
        
        print(dir)
        img = image(data[0], dir, data[1], data[2], data[3], autoResize)
        imageLis.append(img)
        

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
