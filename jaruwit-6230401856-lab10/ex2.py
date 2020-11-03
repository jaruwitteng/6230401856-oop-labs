import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("By {}".format(sys.argv[1]))

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('File')

        menunew = QAction('New', self)
        menunew.setStatusTip('New')
        viewMenu.addAction(menunew)

        #menuedit = QAction('Edit', self)
        #menuedit.setStatusTip('Edit')
        #addedit = viewMenu.addAction(menuedit)
        addedit = QMenu('Edit', self)
        addcopy = QAction('Copy', self)
        addpaste = QAction('Paste', self)
        addedit.addAction(addcopy)
        addedit.addAction(addpaste)
        viewMenu.addMenu(addedit)

        menusave = QAction('Save', self)
        menusave.setStatusTip('Save')
        addsave = viewMenu.addAction(menusave)
        menusave.setShortcut('Ctrl+q')

        viewMenu.addSeparator()

        exitButton = QAction(QIcon('maxresdefault.jpg'), 'Exit', self)
        exitButton.setShortcut('Ctrl+q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        addexit = viewMenu.addAction(exitButton)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Exercise 2')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()