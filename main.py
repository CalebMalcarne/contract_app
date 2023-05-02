'''
Created By: Caleb Malcarne
Program: Invoice Filler 

File Contents:
This file contrains all code for the mail widget for the fourm
It also contains all of the functions 
'''

import sys
import os
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PIL import Image
from imageObj import image
from imageInfoPy import ImageInfo
from Settings import settingsWindow
from datetime import date
from document import doc
from globals import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        # Create a central widget and set it as the central widget for the main window
        central_widget = QWidget(self)
        self.setWindowTitle("Contract Filler")
        self.setCentralWidget(central_widget)
        self.setMaximumSize(QSize(16777215, 16777215))
        

        # Create a grid layout and set it as the layout for the central widget
        grid = QGridLayout()
        central_widget.setLayout(grid)

        grid.setColumnMinimumWidth(1, 10)       
  
        self.Label = QLabel("date_label")
        self.Label.setText("Date")
        grid.addWidget(self.Label, 0, 0)
        
        self.lineEdit = QLineEdit()
        grid.addWidget(self.lineEdit, 0, 2)
        
        #----------------------------------#
        
        self.Label_2 = QLabel("client_label")
        self.Label_2.setText("Client")
        grid.addWidget(self.Label_2, 1, 0)
        
        self.lineEdit_2 = QLineEdit()
        grid.addWidget(self.lineEdit_2, 1, 2)     
        
        #----------------------------------#
        
        self.Label_3 = QLabel("estNum_label")
        self.Label_3.setText("Estimate Number")
        grid.addWidget(self.Label_3, 2, 0)
        
        self.lineEdit_3 = QLineEdit()
        grid.addWidget(self.lineEdit_3, 2, 2) 
        
        #----------------------------------#
        
        self.Label_4 = QLabel("startDate_label")
        self.Label_4.setText("Start Date")
        grid.addWidget(self.Label_4, 3, 0)
        
        self.lineEdit_4 = QLineEdit()
        grid.addWidget(self.lineEdit_4, 3, 2)      

        #----------------------------------#
        
        self.Label_5 = QLabel("startDate_label")
        self.Label_5.setText("End Date")
        grid.addWidget(self.Label_5, 4, 0)
        
        self.lineEdit_5 = QLineEdit()
        grid.addWidget(self.lineEdit_5, 4, 2)               
        #----------------------------------#
        
        self.Label_6 = QLabel("estAmount_label")
        self.Label_6.setText("Estimate Amount")
        grid.addWidget(self.Label_6, 5, 0)
        
        self.lineEdit_6 = QLineEdit()
        grid.addWidget(self.lineEdit_6, 5, 2)      

        #----------------------------------#      
        self.Label_7 = QLabel("Hourly_label")
        self.Label_7.setText("Hourly Rate")
        grid.addWidget(self.Label_7, 6, 0)
        
        self.lineEdit_7 = QLineEdit()
        grid.addWidget(self.lineEdit_7, 6, 2)
        
        #----------------------------------#         
        self.Label_8 = QLabel("time_label")
        self.Label_8.setText("Is Time Important")
        grid.addWidget(self.Label_8, 7, 0)
                
        self.checkBox = QCheckBox()
        grid.addWidget(self.checkBox, 7, 2)
        
        #----------------------------------#    
        self.Label_9 = QLabel("deposit_label")
        self.Label_9.setText("Deposit")
        grid.addWidget(self.Label_9, 8, 0)
        
        self.lineEdit_8 = QLineEdit()
        grid.addWidget(self.lineEdit_8, 8, 2)  
        #----------------------------------#
     
        self.Label_10 = QLabel("allow_label")
        self.Label_10.setText("Allowances")
        grid.addWidget(self.Label_10, 9, 1) 
                  
        #----------------------------------#        
        self.textEdit = QTextEdit()
        grid.addWidget(self.textEdit, 10, 0)
        
        self.textEdit_2 = QTextEdit()
        grid.addWidget(self.textEdit_2, 10, 2)    
        #----------------------------------#  
        
        self.pushButton = QPushButton("Add Image")
        grid.addWidget(self.pushButton, 11, 2)
        
        #----------------------------------# 
        self.Label_11 = QLabel("Image_label")
        self.Label_11.setText("Images")
        grid.addWidget(self.Label_11, 12, 1)             
        #----------------------------------# 
        
        self.textEdit_3 = QTextEdit()       
        grid.addWidget(self.textEdit_3, 13, 0, 1, 3)
        
        #File Menu
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        file_menu = QMenu("File", self)
        self.menu_bar.addMenu(file_menu)
        self.export_action = file_menu.addAction("Export")
        self.export_action_2 = file_menu.addAction("Settings")
        self.export_action.triggered.connect(self.exportDoc)
        self.export_action_2.triggered.connect(self.settingsWindow)
        self.pushButton.clicked.connect(lambda: self.addImage())
        
        self.resizeWindow(widnow_size)

    def resizeWindow(self, size):
        desktop = QDesktopWidget()
        screen_width = desktop.screenGeometry().width()
        screen_height = desktop.screenGeometry().height()
           
        if size == "Large":
            self.lineEdit.setMinimumHeight(0)   
            self.lineEdit.setMaximumHeight(16777215)

            self.lineEdit_2.setMinimumHeight(0)   
            self.lineEdit_2.setMaximumHeight(16777215)

            self.lineEdit_3.setMinimumHeight(0)   
            self.lineEdit_3.setMaximumHeight(16777215)

            self.lineEdit_4.setMinimumHeight(0)   
            self.lineEdit_4.setMaximumHeight(16777215)

            self.lineEdit_5.setMinimumHeight(0)   
            self.lineEdit_5.setMaximumHeight(16777215)

            self.lineEdit_6.setMinimumHeight(0)   
            self.lineEdit_6.setMaximumHeight(16777215)
            
            self.lineEdit_7.setMinimumHeight(0)   
            self.lineEdit_7.setMaximumHeight(16777215)
            
            self.lineEdit_8.setMinimumHeight(0)   
            self.lineEdit_8.setMaximumHeight(16777215)
            
            self.textEdit.setMinimumHeight(0)   
            self.textEdit.setMaximumHeight(16777215)
            
            self.textEdit_2.setMinimumHeight(0)   
            self.textEdit_2.setMaximumHeight(16777215)
            
            self.textEdit_3.setMinimumHeight(0)   
            self.textEdit_3.setMaximumHeight(16777215)
            
        elif size == "Medium":        
            self.lineEdit.setFixedHeight(30)
            self.lineEdit_2.setFixedHeight(30)
            self.lineEdit_3.setFixedHeight(30)
            self.lineEdit_4.setFixedHeight(30)
            self.lineEdit_5.setFixedHeight(30)
            self.lineEdit_6.setFixedHeight(30)
            self.lineEdit_7.setFixedHeight(30)
            self.lineEdit_8.setFixedHeight(30)
            
            self.textEdit.setFixedHeight(150)

            self.textEdit_2.setFixedHeight(150)
            
            self.textEdit_3.setFixedHeight(150)
            
        elif size == "Small": 
            self.lineEdit.setFixedHeight(20)
            self.lineEdit_2.setFixedHeight(20)
            self.lineEdit_3.setFixedHeight(20)
            self.lineEdit_4.setFixedHeight(20)
            self.lineEdit_5.setFixedHeight(20)
            self.lineEdit_6.setFixedHeight(20)
            self.lineEdit_7.setFixedHeight(20)
            self.lineEdit_8.setFixedHeight(20)
            
            self.textEdit.setFixedHeight(100)
            
            self.textEdit_2.setFixedHeight(100)
            
            self.textEdit_3.setFixedHeight(100)
            
    def exportDoc(self):
        
        data = [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), 
                self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text(),
                self.checkBox.checkState(), self.lineEdit_7.text(), self.lineEdit_8.text()]
    
        
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
                
        ImagePaths = self.textEdit_3.toPlainText().split('\n')
        ImagePaths.remove(ImagePaths[len(ImagePaths) - 1])
        print(ImagePaths)

        out_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(out_path)
        export = doc(data, allowanceData, ImagePaths ,out_path)
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
        for image in imageLis:
            path = image.getDir()
            imageText += f"{path}\n"
        self.textEdit_3.setText(imageText)
                
    def addImage(self):
        global images 
        image_path = str(QFileDialog.getOpenFileName(self, "Select Image"))
        
        cut_path = image_path.split(',')[0][2:len((image_path.split(',')[0])) - 1]
        split = cut_path.split('/')
        image_name = split[len(split) - 1].split('.')[0]
        
        if cut_path != '':
         img = Image.open(cut_path)  
         self.ImageWindow(image_name, img.size[1], img.size[0], cut_path)
    
    def ImageWindow(self, imageName, width, height, dir):
        self.img_window = QMainWindow()
        self.ui = ImageInfo()
        self.ui.setupUi(self.img_window, self, imageName, width, height, dir)
        self.img_window.show()
 
    def settingsWindow(self):
        self.settings_window = QMainWindow()
        self.ui = settingsWindow()
        self.ui.setupUi(self.settings_window, self)
        self.settings_window.show()
    
    def saveImage(self, data, dir):
        global imageLis
        autoResize = data[4]
        customeSize = data[5]
           
        print(dir)
        img = image(data[0], dir, data[1], data[2], data[3], autoResize, customeSize)
        imageLis.append(img)
            
            
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
