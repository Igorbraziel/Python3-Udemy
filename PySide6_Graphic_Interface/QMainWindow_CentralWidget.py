# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QStatusBar

app = QApplication()
window = QMainWindow()
central_widget = QWidget()
layout = QGridLayout()
button = QPushButton('My button')

def change_status_bar(status_bar: QStatusBar) -> None:
    status_bar.showMessage('I change the status bar')    

button.setStyleSheet('font-size: 100px; color: white; background-color: black')

window.setWindowTitle('Window Title')
window.setCentralWidget(central_widget)

central_widget.setLayout(layout)

layout.addWidget(button)

status_bar = window.statusBar()
status_bar.showMessage('Status Bar')

menu_bar = window.menuBar()
first_menu = menu_bar.addMenu('First Menu')
first_action = first_menu.addAction('First Action')
first_action.triggered.connect(lambda: change_status_bar(status_bar))

window.show()

app.exec()