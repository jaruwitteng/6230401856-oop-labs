import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 120)
        self.setWindowTitle('Problem 1')

        label_name = QLabel("Name")
        self.text = QLineEdit("Enter Your name!!", self)

        fbox = QFormLayout(self)
        fbox.addRow(label_name, self.text)
        vbox = QVBoxLayout(self)

        hbox = QHBoxLayout(self)
        self.pyqt = QtWidgets.QCheckBox("PyQt")
        self.pygame = QtWidgets.QCheckBox("PyGame")
        self.pytorch = QtWidgets.QCheckBox("PyTorch")

        hbox.addWidget(self.pyqt)
        self.pyqt.setChecked(True)
        hbox.addWidget(self.pygame)
        hbox.addWidget(self.pytorch)
        hbox.addStretch()
        fbox.addRow(QLabel("Library"), hbox)
        self.pyqt.stateChanged.connect(lambda state=self.pyqt.isChecked(), no="PyQt": self.statechanged(state, no))
        self.pygame.stateChanged.connect(lambda state=self.pygame.isChecked(), no="PyGame": self.statechanged(state, no))
        self.pytorch.stateChanged.connect(lambda state=self.pytorch.isChecked(), no="PyTorch": self.statechanged(state, no))

        hbox = QHBoxLayout(self)
        hbox.addStretch(1)
        # summit = hbox.addWidget(QPushButton("Summit"))
        summit = QPushButton("Summit", self)
        summit.move(150, 55)
        summit.clicked.connect(self.sumitted)
        hbox.addWidget(QPushButton("Cancel"))
        fbox.addRow(hbox)

        self.show()

    def statechanged(self, toggle, no):
        if toggle == QtCore.Qt.Checked:
            print(str(no) + " is selected")
        else:
            print(str(no) + " is deselected")


    def sumitted(self):
        print("Name is {}".format(self.text.text()))


def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()