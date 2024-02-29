from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication()

button1 = QPushButton('Button 1')
button1.setStyleSheet('font-size: 100px; color: green; background-color: red')

button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 100px; color: black; background-color: pink')

main_widget = QWidget()
main_layout = QGridLayout()
main_widget.setLayout(main_layout)

main_layout.addWidget(button1, 1, 1, 1, 1)
main_layout.addWidget(button2, 2, 1, 1, 1)

main_widget.show()

app.exec()