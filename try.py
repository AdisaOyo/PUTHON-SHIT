'''
PyQt Radio Buttons
'''

import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QLayout, QPushButton, QLabel, QApplication, QRadioButton, QButtonGroup,
                             QBoxLayout, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtGui import (QPixmap, QIcon, QFont)
from PyQt5.QtCore import (Qt, QSize)

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon (r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG"))
        self.setWindowTitle ("RADIO BUTTONS")
        self.setGeometry(1000, 200, 600, 600)
        self.setStyleSheet("background-color: grey; "
                           )

        #creatign radiobuttons
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("Verve", self)

        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.initUI()
        pass
    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)

        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet("QRadioButton{"\
                           "font-size: 40px; "
                           "font-family: Times New Roman; "
                           "padding: 10px; "
                           "}")
        

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
        pass
    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")
        #print("selection made!!!")
        pass

def main():
    App = QApplication(sys.argv)
    Window = Main_Window()
    Window.show()
    sys.exit(App.exec_())
if __name__ == "__main__":
    main()