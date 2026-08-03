# COURSE PRACTICE EXERCISE: BRO CODE TUTORIAL - DIGITAL CLOCK

# calling imports
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QMainWindow,
                             QLabel, QLayout, 
                             QPushButton, QRadioButton,
                             QCheckBox,QGridLayout,
                             QBoxLayout, QVBoxLayout,
                             QHBoxLayout, QLineEdit)
from PyQt5.QtGui import (QFont, QFontDatabase, QIcon, QPixmap)
from PyQt5.QtCore import (Qt, QSize, QTimer, QTime)

# Constructing Digital Clock class [Main Window]
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        # setting up label to show time
        self.time_label = QLabel(self)
        # setting up timer to update time
        self.timer = QTimer(self)

        self.initUI()


        pass
    def initUI(self):

        #  editing main window 
        self.setWindowTitle("BRO CODE - DIGITAL CLOCK")
        self.setGeometry(1000, 800, 300, 100)
        self.setWindowIcon(QIcon (r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG"))

        # editing time label
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 150px; "
                                      "color: hsv(120, 190, 70); "
                                      )

        # editing main window background colour
        self.setStyleSheet("background-color: black; ")

        # setting font
        font_id = QFontDatabase.addApplicationFont(r"BRO CODE/ds_digital/DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        # adding timer widget to the update time slot
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # update every second

        # calling current time function
        self.update_time()

        pass
    # defining function to update time
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

        pass

# Calling Main function [This runs the program]
'''
def main():
    App = QApplication(sys.argv)
    Window = QWidget()
    Window.show()
    sys.exit(App.exec_())
'''

# Apparently I can just do this instead of always
# calling the main() functon 🤦🏾
if __name__ == "__main__":
    App = QApplication(sys.argv)
    Clock_Window = DigitalClock()
    Clock_Window.show()
    sys.exit(App.exec_())
    #main()
