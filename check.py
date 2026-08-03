# calling imports
import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLayout, QVBoxLayout)
from PyQt5.QtGui import (QIcon, QFont, QFontDatabase, QPixmap)
from PyQt5.QtCore import (Qt, QTimer, QTime, QSize)

# calling Digital_Clock class [Main Window]
class Digital_Clock(QWidget):
    ## defining __init__()
    def __init__(self):
        super().__init__()

        ### creating timer_label
        self.timer_label = QLabel()

        ### creating timer
        self.timer = QTimer(self)

        ### creating widget objects
        self.timer_label.setObjectName("timer_label")
        self.setObjectName("Main_Window")

        ### calling initUI()
        self.initUI()


        pass
    ### defining initUI()
    def initUI(self):

        ### editing main window
        self.setWindowTitle("OKAY, REAL HARD CODE TRY NOW LOL")
        self.setWindowIcon(QIcon(r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG"))

        ### setting up timer update system
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) # set timer to update every second

        ## editing time_label
        self.timer_label.setAlignment(Qt.AlignCenter)
        font_id = QFontDatabase.addApplicationFont(r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\ds_digital\DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.timer_label.setFont(my_font)

        ### setting up layout
        VBox = QVBoxLayout()
        VBox.addWidget(self.timer_label)
        self.setLayout(VBox)

        ### creating global style sheet
        self.setStyleSheet("""
                            QWidget#Main_Window{
                                background-color: black; 
                            }
                            QWidget#Main_Window:hover{
                                background-color: blue; 
                            }
                            QLabel#timer_label{
                                color: hsv(50, 255, 70);
                                background-color: transparent;
                            }

                            """)
    # defining update_time() function
    def update_time(self):
        current_time = QTime().currentTime()
        self.timer_label.setText(current_time.toString("hh:mm:ss AP"))
# calling program to run
if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = Digital_Clock()
    Window.show()
    sys.exit(App.exec_())