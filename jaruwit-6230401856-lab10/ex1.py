import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QLabel)
from PyQt5.QtCore import QCoreApplication, Qt


class Exercise1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("Quit", self)
        btn.setToolTip("Close Application")
        #btn.clicked.connect(self.closeEvent)
        btn.clicked.connect(QApplication.instance().quit)
        label = QLabel("My name is {}".format(sys.argv[1]), self)
        label.move(0, 0)
        btn.resize(btn.sizeHint())
        btn.move(225, 50)
        self.setGeometry(30, 450, 500, 150)
        self.setWindowTitle("Exercise 1")
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "Message",
            "Are you sure to quit?",
            QMessageBox.Close | QMessageBox.Cancel,
            QMessageBox.Cancel)

        if reply == QMessageBox.Close:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


def Main():
    app = QApplication(sys.argv)
    w = Exercise1()
    sys.exit(app.exec_())


if __name__ == '__main__':
    Main()