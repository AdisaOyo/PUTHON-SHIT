import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QLayout, QVBoxLayout, QWidget)
from PyQt5.QtGui import (QFont, QIcon, QPixmap)
from PyQt5.QtCore import (Qt, QSize)

class MainWIndow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("JUVENILE WRLD")
        self.setGeometry(50, 50, 1000, 1000)
        self.setIconSize(QSize(500,500))
        self.setWindowIcon(QIcon(r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG"))
        

    def initUI(self):
        pass

def main():
    App = QApplication(sys.argv)
    Main_Window = MainWIndow()
    Main_Window.show()
    sys.exit(App.exec_())

    pass

if __name__ == "__main__":
    main()