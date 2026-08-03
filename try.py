# omporting modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout)
from PyQt5.QtGui import (QFont, QFontDatabase, QIcon, QPixmap)
from PyQt5.QtCore import (Qt, QTimer, QTime)

# construction digital clock class [Main Window]
class Digital_Clock(QWidget):
    def __init__(self):
        super().__init__()

        #setting up time display label
        self.time_label = QLabel(self)
        ##creating time objects to set style sheet
        self.setObjectName("clockWindow")
        self.time_label.setObjectName("time_label")

        # setting up timer to update time
        self.timer = QTimer(self)

        self.initUI()

        pass
    # defining init UI function
    def initUI(self):

        # editing main window
        self.setWindowTitle("I HOPE I CAN HARD CODE THIS")
        self.setWindowIcon(QIcon(r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG"))
        self.setGeometry(600, 800, 300, 100)

        # editing time label with custom font and colour
        self.time_label.setAlignment(Qt.AlignCenter)
        font_id = QFontDatabase.addApplicationFont(r"BRO CODE/ds_digital/DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # update every second

        #setting up global style sheet
        self.setObjectName("clockWindow")
        self.time_label.setObjectName("time_label")
        self.setStyleSheet("""
                            QWidget#clockWindow {
                                background-color: black;
                            }

                            QLabel#time_label {
                                color: hsv(50, 255, 70);
                                background-color: transparent;
                            }
                            """)                                  

        # setting up widget layout
        VBox = QVBoxLayout()
        VBox.addWidget(self.time_label)
        self.setLayout(VBox)

        pass
    # defining update time function
    def update_time(self):

        # getting current time to update
        current_time = QTime.currentTime()
        self.time_label.setText(current_time.toString("hh:mm:ss AP"))

        pass

# calling main function
if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = Digital_Clock()
    Window.show()
    sys.exit(App.exec_())