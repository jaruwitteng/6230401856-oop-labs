import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QLabel)
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel("Title")
        author = QLabel("Author")
        review = QLabel("Review")

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1 ,1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        review2 = QLabel("")
        grid.addWidget(review2, 9, 0)
        review3 = QLabel("")
        grid.addWidget(review3, 10, 0)

        button1 = QPushButton("OK", self)
        button1.move(90, 250)
        button2 = QPushButton("Cancel", self)
        button2.move(190, 250)

        self.setLayout(grid)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Review by {}".format(sys.argv[1]))
        self.show()


def main():
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()