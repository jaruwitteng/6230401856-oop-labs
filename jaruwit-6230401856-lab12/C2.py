import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
from PyQt5.QtCore import Qt
import time

class Paint(QMainWindow):
    def __init__(self):
        super().__init__()
        self.findpath = ""
        self.init_ui()

    def init_ui(self):
        self.text = QTextEdit()
        self.text.setFont(QFont("Arial", 16))
        self.setCentralWidget(self.text)
        self.statusbar = self.statusBar()
        #file menu
        menubar = self.menuBar()
        viewMenu = menubar.addMenu('File')

        menuopen = QAction('Open', self)
        menuopen.setStatusTip('Open file')
        viewMenu.addAction(menuopen)
        menuopen.setShortcut('Ctrl+O')
        menuopen.triggered.connect(self.open)

        savemenu = QAction('Save', self)
        savemenu.setStatusTip('Save file')
        viewMenu.addAction(savemenu)
        savemenu.setShortcut('Ctrl+S')
        savemenu.triggered.connect(self.save)

        #edit menu
        editmenu = menubar.addMenu("Edit")
        color = QMenu("color", self)
        editmenu.addMenu(color)
        background = QAction("Background color", self)
        background.triggered.connect(self.background_color)
        foreground = QAction("Foreground color", self)
        foreground.triggered.connect(self.foreground_color)
        color.addAction(background)
        color.addAction(foreground)
        font = QAction("Font", self)
        editmenu.addAction(font)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('File dialog')
        self.show()

    def open(self):
        openingfile = QFileDialog.getOpenFileName()
        with open(openingfile[0]) as file:
            self.edit.setText(file.read())

    def save(self):
        saving_file, _ = QFileDialog.getSaveFileName(self, "Saving", "Enter name", "Text files (*.txt)")
        if saving_file:
            self.findpath = saving_file
            with open(self.findpath, "w") as f:
                f.write(self.editor.toPlainText())
                f.close()

    def background_color(self):
        self.backgroundcolor = QColorDialog.getColor()
        try:
            self.setStyleSheet("background-color: {} ; color: {}".format(self.backgroundcolor.name(),self.fontcolor.name()))
        except:
            self.setStyleSheet("background-color: {}".format(self.backgroundcolor.name()))

    def foreground_color(self):
        self.fontcolor = QColorDialog.getColor()
        try:
            self.setStyleSheet("background-color: {} ; color: {}".format(self.backgroundcolor.name(),self.fontcolor.name()))
        except:
            self.setStyleSheet("background-color: {}".format(self.fontcolor.name()))


def main():
    app = QApplication(sys.argv)
    ex = Paint()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
