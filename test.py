import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider
from PyQt5.QtCore import Qt

class SliderExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a label to display the value of the slider
        self.label = QLabel()
        self.label.setText("0")

        # Create the slider
        self.slider = QSlider()
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(0)

        # Connect the valueChanged signal of the slider to the updateValue function
        self.slider.valueChanged.connect(self.updateValue)

        # Set the layout of the widget
        self.setLayout(self.label, self.slider)

    def updateValue(self):
        # Update the label with the value of the slider
        self.label.setText(str(self.slider.value()))


app = QApplication(sys.argv)
ex = SliderExample()
ex.show()
sys.exit(app.exec_())
