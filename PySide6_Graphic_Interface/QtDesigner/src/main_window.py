from window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from PySide6.QtCore import Slot, QObject, QEvent
from PySide6.QtGui import QKeyEvent
from typing import cast
import sys



class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setupUi(self)
        self.buttonSend.clicked.connect(self.changeLabelResult)
        self.lineName.installEventFilter(self)
        
    
    @Slot()
    def changeLabelResult(self):
        text = self.lineName.text()
        self.labelResult.setText(text)
        
        
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        
        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            text = self.lineName.text()
            self.labelResult.setText(text + event.text())
            
        return super().eventFilter(watched, event)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec()