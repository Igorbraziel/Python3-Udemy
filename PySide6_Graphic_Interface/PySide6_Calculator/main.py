import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from main_window import MyMainWindow
from buttons import MyButton
from buttons import ButtonsGrid
from variables import IMAGE_PATH
from display import Display
from info import Info
from styles import SetUpDarkTheme


if __name__ == '__main__':
    # Making the application
    app = QApplication(sys.argv)
    SetUpDarkTheme()
    window = MyMainWindow()
    
    # Defining the icon
    icon = QIcon(str(IMAGE_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    # Making the info
    info = Info('Your Account')
    window.addWidgetToVLayout(info)    
    
    # Making my display line
    display_ = Display()
    window.addWidgetToVLayout(display_)
    
    # Making a Buttons Grid
    buttons_grid = ButtonsGrid(display_, info, window)
    window.addLayoutToVLayout(buttons_grid)
    
    # Making Buttons
    
    # Executing
    window.adjustFixedSize()
    window.show()
    app.exec()