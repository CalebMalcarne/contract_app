from PyQt5 import QtCore, QtGui, QtWidgets


class ImageInfo(object):
    def __init__(self, image_data):
        self.image_data = image_data
        self.form = QtWidgets.QWidget()
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self.form)
        self.form.setLayout(layout)

        name_label = QtWidgets.QLabel("Name:")
        name_edit = QtWidgets.QLineEdit()
        name_edit.setText(self.image_data.get("name", ""))
        name_layout = QtWidgets.QHBoxLayout()
        name_layout.addWidget(name_label)
        name_layout.addWidget(name_edit)
        layout.addLayout(name_layout)

        width_label = QtWidgets.QLabel("Width:")
        width_edit = QtWidgets.QLineEdit()
        width_edit.setText(str(self.image_data.get("width", "")))
        width_layout = QtWidgets.QHBoxLayout()
        width_layout.addWidget(width_label)
        width_layout.addWidget(width_edit)
        layout.addLayout(width_layout)

        height_label = QtWidgets.QLabel("Height:")
        height_edit = QtWidgets.QLineEdit()
        height_edit.setText(str(self.image_data.get("height", "")))
        height_layout = QtWidgets.QHBoxLayout()
        height_layout.addWidget(height_label)
        height_layout.addWidget(height_edit)
        layout.addLayout(height_layout)

        dir_label = QtWidgets.QLabel("Directory:")
        dir_edit = QtWidgets.QLineEdit()
        dir_edit.setText(self.image_data.get("dir", ""))
        dir_layout = QtWidgets.QHBoxLayout()
        dir_layout.addWidget(dir_label)
        dir_layout.addWidget(dir_edit)
        layout.addLayout(dir_layout)

        self.push_button = QtWidgets.QPushButton("Submit")
        self.push_button.clicked.connect(self.submit_data)
        layout.addWidget(self.push_button)

    def submit_data(self):
        # TODO: Implement submit data functionality
        pass


def main():
    app = QtWidgets.QApplication([])

    image_data = {
        "name": "Image 1",
        "width": 800,
        "height": 600,
        "dir": "/path/to/image",
    }
    image_info = ImageInfo(image_data)
    image_info.form.show()

    app.exec_()



main()
