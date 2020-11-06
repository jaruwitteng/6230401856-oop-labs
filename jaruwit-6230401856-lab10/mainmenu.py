import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 600)
        self.setWindowTitle('Message')

        searchbar = QLabel("Search Window", self)
        searchbar.move(20, 30)
        searchbar.resize(100,20)

        text = QLineEdit("Search here!!!", self)
        text.setGeometry(20, 50, 120, 25)

        testpush = QPushButton("Search", self)
        testpush.setToolTip("search")
        testpush.resize(100, 20)
        testpush.move(20, 80)
        testpush.clicked.connect(self.search)

        recommend = QLabel("Recommended of the week", self)
        recommend.move(20, 120)
        recommend.resize(200,50)

        recommend1 = QPushButton("Story 1", self)
        recommend1.setToolTip("Story1")
        recommend1.resize(150, 150)
        recommend1.move(20, 155)
        recommend1.clicked.connect(self.story1)

        recommend2 = QPushButton("Story 2", self)
        recommend2.setToolTip("Story2")
        recommend2.resize(150, 150)
        recommend2.move(180, 155)

        recommend3 = QPushButton("Story 3", self)
        recommend3.setToolTip("Story3")
        recommend3.resize(100, 100)
        recommend3.move(20, 320)

        recommend4 = QPushButton("Story 4", self)
        recommend4.setToolTip("Story4")
        recommend4.resize(100, 100)
        recommend4.move(125, 320)

        recommend5 = QPushButton("Story 5", self)
        recommend5.setToolTip("Story5")
        recommend5.resize(100, 100)
        recommend5.move(230, 320)

        self.toolbar = QtWidgets.QToolBar("Tool bar")
        self.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolbar)
        self.toolbar.resize(300,200)

        browse_photo = QAction(QIcon("search.jpg"), "browse", self)
        load_photo = QAction(QIcon("continue.jpg"), "load", self)
        create_photo = QAction(QIcon("create.jpg"), "create", self)
        profile_photo = QAction(QIcon("profile.jpg"), "profile", self)
        quit_photo = QAction(QIcon("quit.png"), "quit", self)

        browse = self.toolbar.addAction(browse_photo)
        load = self.toolbar.addAction(load_photo)
        create = self.toolbar.addAction(create_photo)
        profile = self.toolbar.addAction(profile_photo)
        quit = self.toolbar.addAction(quit_photo)

        self.show()

    def search(self):
        print("searching in progess")

    def story1(self):
        print("Enter story")

    def load(self):
        pass

    def write(self):
        pass

    def profile(self):
        pass

    def quit(self):
        pass

def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
