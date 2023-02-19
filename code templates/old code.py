'''

def allow_window(self):
    if self.w is None:
        self.w = Allowance(MainWindow)
        self.w.show()

    else:
        self.w = None  # Discard reference.
            
 def add_allow_wind(self):
        global allow_index
        global allow_objs
        
        if allow_index < 10:
            self.shift_display()
            _translate = QtCore.QCoreApplication.translate
            
            self.label_test = QtWidgets.QLabel(self.layoutWidget)
            self.label_test.setObjectName(str(allow_index))
            
            
            self.label_test_ = QtWidgets.QLabel(self.layoutWidget)
            self.label_test_. setObjectName(str(allow_index))
            
            
            
            self.gridLayout.addWidget(self.label_test, 12 + allow_index, 0, 1, 1)
            self.gridLayout.addWidget(self.label_test_, 12 + allow_index, 4, 1, 2)
            
            self.label_test.setText(_translate("MainWindow", "allowance_test " + str(allow_index)))
            self.label_test_.setText(_translate("MainWindow", "Allowance " + str(allow_index)))
            
            allow_index += 1
            
            print(self.label_test.objectName())
            print(allow_objs)
             
    def shift_display(self):
        global length
        global text_thick
        _translate = QtCore.QCoreApplication.translate
        
        
        self.gridLayout.removeWidget(self.label_11)
        self.gridLayout.removeWidget(self.pushButton_2)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        
        self.gridLayout.addWidget(self.label_11, 13 + allow_index, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton_2, 13 + allow_index, 4, 1, 2)        
        
        self.label_11.setText(_translate("MainWindow", "Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Add image"))
        
        length += 50
        self.resize(450, length)
        text_thick += 50
        self.layoutWidget.setGeometry(QtCore.QRect(20, 0, 400, text_thick))
              
    def remove_allow(self):
        global allow_index
        spinVal = self.spinBox.value()
        
        delIndex = 25 + spinVal
        
        
        
        self.gridLayout.itemAt(delIndex).widget().deleteLater()
        self.gridLayout.itemAt(delIndex + 1).widget().deleteLater()
        #print(self.gridLayout.itemAt(25).widget().objectName())
'''