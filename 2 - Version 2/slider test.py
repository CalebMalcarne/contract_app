import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class SliderDemo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Slider Demo')
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Value: 1')
        self.slider = QtWidgets.QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.updateValue)

        #self.setLayout(self.label)
        self.show()

    def updateValue(self, value):
        self.label.setText('Value: {}'.format(value))

app = QtWidgets.QApplication(sys.argv)
demo = SliderDemo()
sys.exit(app.exec_())
