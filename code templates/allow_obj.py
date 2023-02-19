from PyQt5 import QtCore, QtGui, QtWidgets

class allow_obj():
    def __init__(self, label, button):
        self._label = label
        self._button = button
        
    def getBtn(self):
        return self._button
    
    def getLabel(self):
        return self._label

