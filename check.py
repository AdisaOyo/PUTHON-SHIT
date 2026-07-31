from sre_parse import State
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel,QWidget, QPushButton, QRadioButton, QButtonGroup, QCheckBox,
                             QLayout, QGridLayout, QBoxLayout, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import (QPixmap, QIcon, QFont)
from PyQt5.QtCore import (Qt, QSize)

# constructing main window class
class Main_Window(QMainWindow):
    # defining __init__ function
    def __init__(self):
        super().__init__()
        self.setGeometry(1000, 200, 600, 600)
        self.setWindowTitle("Radio Button Practice")
        self.setWindowIcon(QIcon(r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG"))
        self.setStyleSheet("background-color: #E0E0E0; "
                           )

        #setting tittle label
        self.Title_label = QLabel("JUVENILE RECORDS", self)
        #setting menue bar label
        self.Menu_bar_label = QLabel("",self)
        #setting Welcome page text
        self.Welcom_text_label = QLabel("Young, Free, Creative", self)
        #setting welcome page image
        self.Welcome_page_image_label = QLabel(self)
        self.Welcome_page_image = QPixmap(r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG")
        self.Welcome_page_image_label.setPixmap(self.Welcome_page_image)
        self.Welcome_page_image_label.setScaledContents(True)
        #setting menu bar checkbox options for artists
        self.Sway_checkbox = QCheckBox("Don Corleone", self)
        self.Ecko_checkbox = QCheckBox("ECKØ", self)
        self.Drksn_checkbox = QCheckBox("DRKSN", self)
        #setting checkbox menu text
        self.checkbox_body_text = QLabel("", self)
        #setting payment method label
        self.payment_method_label = QLabel()

        self.initUI()
        pass
    # defining initUI function
    def initUI(self):

        # editing Title_label properties
        self.Title_label.setGeometry(0, 0, 600, 60)
        self.Title_label.setStyleSheet("background-color: pink; "
                           "font-family: gothic; "
                           "font-size: 50px; "
                           "font-style: italic; ")
        self.Title_label.setWordWrap(True)
        self.Title_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # editing menue bar label
        self.Menu_bar_label.setStyleSheet("background-color: #799791; ")
        self.Menu_bar_label.setGeometry(0, 60, 200, (self.height() - self.Title_label.height()))

        # editing welcome page text
        self.Welcom_text_label.setWordWrap(True)
        self.Welcom_text_label.setGeometry((self.Menu_bar_label.width()),
                                           (self.Title_label.height()), 
                                           (self.width()-self.Menu_bar_label.width()), 
                                           100)
        self.Welcom_text_label.setStyleSheet("font-family: Times New Roman; "
                                             "font-style: italic; "
                                             "font-weight: bold; "
                                             "font-size: 50px; "
                                             "background-color: yellow; "
                                             )
        self.Welcom_text_label.setScaledContents(True)
        self.Welcom_text_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # editing welcome page image
        self.Welcome_page_image_label.setGeometry((self.Menu_bar_label.width()),
                                                  (self.Title_label.height() + self.Welcom_text_label.height()), 
                                                  (self.width()-self.Menu_bar_label.width()), 
                                                   self.height() - (self.Title_label.height() + self.Welcom_text_label.height()))

        # editing checkboxes
        ##editing SWAY
        self.Sway_checkbox.setGeometry(0, 
                                       self.Title_label.height() + 10,
                                       self.Menu_bar_label.width(), 
                                       50)
        self.Sway_checkbox.setStyleSheet("font-size: 30px; "
                                     "font-family: Ariel; "
                                     "background-color: #A9B76E; "
                                     "padding: 10px; "
                                     )
        self.Sway_checkbox.setChecked(False)
        self.Sway_checkbox.stateChanged.connect(self.checkbox_changed)
        ##editing ECKØ
        self.Ecko_checkbox.setGeometry(0, 
                                       self.Title_label.height() + self.Sway_checkbox.height() + 20,
                                       self.Menu_bar_label.width(), 
                                       50)
        self.Ecko_checkbox.setStyleSheet("font-size: 30px; "
                                         "font-family: Ariel; "
                                         "background-color: #A9B76E; "
                                         "padding: 10px; "
                                         )
        self.Ecko_checkbox.setChecked(False)
        self.Ecko_checkbox.stateChanged.connect(self.checkbox_changed)
        ##editing DRKSN
        self.Drksn_checkbox.setGeometry(0, 
                                       self.Title_label.height() + self.Sway_checkbox.height() + self.Ecko_checkbox.height() + 30,
                                       self.Menu_bar_label.width(), 
                                       50)
        self.Drksn_checkbox.setStyleSheet("font-size: 30px; "
                                         "font-family: Ariel; "
                                         "background-color: #A9B76E; "
                                         "padding: 10px; "
                                         )
        self.Drksn_checkbox.setChecked(False)
        self.Drksn_checkbox.stateChanged.connect(self.checkbox_changed)

        # editing checkbox body text
        self.checkbox_body_text.setGeometry((self.Menu_bar_label.width()),
                                            (self.Title_label.height() + self.Welcom_text_label.height()), 
                                            200, 
                                            50)
        
        # editing payment option label
        self.payment_method_label.setGeometry(0, 
                                              0,
                                              self.Menu_bar_label.width(), 
                                              50)
        self.payment_method_label.setStyleSheet("background-color: black; "
                           )
    
        pass
    #defining checkbox change properties
    def checkbox_changed(self, state):
        checkbox = self.sender()
        if state == Qt.Checked:
            self.checkbox_body_text.setText(f"{checkbox.text()} is selected")
        pass

    #
    
        
        
    
    

# defining main function
def main():
    App = QApplication(sys.argv)
    Window = Main_Window()
    Window.show()
    sys.exit(App.exec_())

# calling __main__
if __name__ == "__main__":
    main()