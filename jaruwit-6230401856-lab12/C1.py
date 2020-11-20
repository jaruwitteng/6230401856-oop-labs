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

class slider(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_value = 50
        self.init_value2 = 50
        self.init_ui()
        self.receiver = -1
        self.checker = None

    def init_ui(self):
        app = QApplication(sys.argv)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(self.init_value)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.valueChanged[int].connect(self.change_value)

        self.label = QLabel(self)
        self.label.setText(str(self.init_value))
        self.label.setFont(QFont("Arial", 20))
        self.label.setStyleSheet("color: blue")
        self.label.adjustSize()

        self.slider2 = QSlider(Qt.Horizontal, self)
        self.slider2.setMinimum(0)
        self.slider2.setMaximum(100)
        self.slider2.setValue(self.init_value2)
        self.slider2.setTickPosition(QSlider.TicksBelow)
        self.slider2.setTickInterval(5)
        self.slider2.valueChanged[int].connect(self.change_value2)

        self.label2 = QLabel(self)
        self.label2.setText(str(self.init_value))
        self.label2.setFont(QFont("Arial", 20))
        self.label2.setStyleSheet("color: blue")

        window = QWidget()
        self.fbox = QFormLayout()
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.label)
        self.hbox.addStretch(0)
        self.hbox.addWidget(self.slider)
        self.fbox.addRow(self.hbox)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.label2)
        self.hbox.addStretch(0)
        self.hbox.addWidget(self.slider2)
        self.fbox.addRow(self.hbox)
        self.hbox = QHBoxLayout()
        self.create_button()

        result = QLabel()
        result.setText("Result")
        result.setFont(QFont("Arial", 18))

        self.result_print = QLineEdit()
        self.result_print.setEnabled(False)
        self.result_print.setFont(QFont("Arial", 16))
        self.result_print.setStyleSheet("color : yellow ; background-color: grey")
        self.result_print.setAlignment(Qt.AlignRight)
        self.result_print.setMinimumSize(100, 25)

        self.fbox.addRow(result, self.result_print)

        window.setLayout(self.fbox)
        window.adjustSize()
        window.setWindowTitle("Simple calculator")
        window.show()
        sys.exit(app.exec_())

    def create_button(self):
        self.hbox = QHBoxLayout()
        calculator_choices = ["Add", "Subtract", "Multiply", "Divide"]
        calculator_buttons = [QPushButton(x) for x in calculator_choices]

        for i in calculator_buttons:

            self.hbox.addWidget(i)
            self.fbox.addRow(self.hbox)
            i.clicked.connect(self.sender_def)

    def create_slider(self, value):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(self.init_value)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(5)
        self.newslider.append(slider)

    def create_label(self, size ,font, value):
        label = QLabel()
        label.setFont(QFont(font, size))
        label.setStyleSheet("color: blue")
        label.setText(str(value))
        self.newlabel.append(label)

    def change_value(self, value):
        updated_value = value
        self.label.setText(str(updated_value))
        self.init_value = updated_value

    def change_value2(self, value):
        updated_value2 = value
        self.label2.setText(str(updated_value2))
        self.init_value2 = updated_value2

    def sender_def(self):
        print("asd")
        sender = self.sender()
        if sender.text() == "Add":
            self.receiver = 1
            sender.setStyleSheet("background-color : green")
        elif sender.text() == "Subtract":
            self.receiver = 2
            sender.setStyleSheet("background-color : green")
        elif sender.text() == "Multiply":
            self.receiver = 3
            sender.setStyleSheet("background-color : green")
        elif sender.text() == "Divide":
            self.receiver = 4
            sender.setStyleSheet("background-color : green")
        self.calculator()

    def calculator(self):
        if self.receiver >= 1:
            if self.receiver == 1:
                self.result = self.init_value + self.init_value2
            elif self.receiver == 2:
                self.result = self.init_value - self.init_value2
            elif self.receiver == 3:
                self.result = self.init_value * self.init_value2
            elif self.receiver == 4:
                self.result = self.init_value / self.init_value2
            else:
                print("Error")
        self.result = str(self.result)
        self.result_print.setText(self.result)


def main():
    app = QApplication(sys.argv)
    ex = slider()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()