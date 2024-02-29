# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)
button = QPushButton('Button Text')
button.setStyleSheet('font-size: 40px; color: blue; width: 400px; height: 200px')
button.show()

app.exec()
