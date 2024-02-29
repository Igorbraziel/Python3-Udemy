import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from main_window import MyMainWindow
from variables import IMAGE_PATH
from display import Display
from info import Info


if __name__ == '__main__':
    # Making the application
    app = QApplication(sys.argv)
    window = MyMainWindow()
    
    # Defining the icon
    icon = QIcon(str(IMAGE_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    # Making the info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)    
    
    # Making my display line
    display_ = Display()
    window.addWidgetToVLayout(display_)
    
    # Executing
    window.adjustFixedSize()
    window.show()
    app.exec()