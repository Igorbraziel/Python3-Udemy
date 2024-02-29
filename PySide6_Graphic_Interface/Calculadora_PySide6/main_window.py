from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

class MyMainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        #Making the Widgets
        self.central_widget = QWidget()
        self.VLayout = QVBoxLayout() 
        self.setStyleSheet('background-color: gray')
        self.central_widget.setLayout(self.VLayout)
        self.setCentralWidget(self.central_widget)
        
        # Title
        self.setWindowTitle('CALCULATOR')
        
    # Must be called in the end
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        
    def addWidgetToVLayout(self, widget: QWidget):
        self.VLayout.addWidget(widget)