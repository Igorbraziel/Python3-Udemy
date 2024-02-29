from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from PySide6.QtCore import Slot
import os

app = QApplication()
window = QMainWindow()
central_widget = QWidget()
layout = QGridLayout()
button = QPushButton('My button')

button.setStyleSheet('font-size: 50px; color: white; background-color: black')

window.setWindowTitle('Window Title')
window.setCentralWidget(central_widget)

central_widget.setLayout(layout)

layout.addWidget(button)

status_bar = window.statusBar()
status_bar.showMessage('Status Bar')

@Slot()
def slot_1(status_bar):
    def inner():
        status_bar.showMessage('I change the status bar')
    return inner

@Slot()
def slot_2(checked: bool):
    print('Is checked?', checked)
    
@Slot()
def slot_3(second_action):
    def inner():
        slot_2(second_action.isChecked())
    return inner

def slot_4():
    os.system('clear')
    

menu_bar = window.menuBar()
first_menu = menu_bar.addMenu('First Menu')

first_action = first_menu.addAction('First Action')
first_action.triggered.connect(slot_1(status_bar))

second_action = first_menu.addAction('Second Action')
second_action.setCheckable(True)
second_action.toggled.connect(slot_2)

second_action.hovered.connect(slot_3(second_action))

button.clicked.connect(slot_4)

window.show()

app.exec()