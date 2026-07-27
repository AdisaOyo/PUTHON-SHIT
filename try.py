'''
PyQt5 push buttons
'''

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QLabel, QToolBar, QGridLayout, 
                             QVBoxLayout, QHBoxLayout, QBoxLayout, QPushButton)
from PyQt5.QtGui import (QIcon, QFont, QPixmap)
from PyQt5.QtCore import (Qt, QSize)

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.setWindowIcon (QIcon (r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG"))
        self.setWindowTitle("Push Buttons")
        self.setGeometry(400, 400, 600, 600)
        self.setIconSize(QSize(1000,1000))
        self.setStyleSheet("background-color: pink; "
                           )

        self.label_goodbye = QLabel("HELLO!", self)
        self.label_goodbye.setGeometry(0, 0, 200, 100)
        self.label_goodbye.setStyleSheet("background-color: red; "
                           )


    def initUi(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.button1 = QPushButton("Botton 1", self)
        self.button2 = QPushButton("Botton 2", self)
        #button1.setGeometry(50, 50, 100, 50)
        self.button1.setGeometry(0, 200, 200, 100)
        self.button1.setStyleSheet("font-size: 20px; ")
        self.button1.clicked.connect(self.on_button1_click)
        self.button2.setGeometry(150, 200, 200, 100)
        self.button2.setStyleSheet("font-size: 20px; ")
        self.button2.clicked.connect(self.on_button2_click)
        

    def on_button1_click(self):
        print("Button 1 clicked")
        self.button1.setText("CLicked!!")
        self.button1.setDisabled(True)
        self.label_goodbye.setText("GOODBYE!")

    def on_button2_click(self):
        print("Button 2 clicked")
        self.button2.setText("CLicked!!")
        self.button2.setDisabled(True)
        self.label_goodbye.setText("HELLO AGAIN!")

## Always prefix your buttons with self. if you want to access them in other functions. Otherwise, they will be local variables and won't be accessible outside the function they are defined in.
        

def main():
    App = QApplication(sys.argv)
    App_Window = MainWindow()
    App_Window.show()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()