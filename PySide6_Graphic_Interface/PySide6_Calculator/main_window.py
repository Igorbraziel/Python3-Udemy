from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLayout, QMessageBox

class MyMainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        #Making the Widgets
        self.central_widget = QWidget()
        self.VLayout = QVBoxLayout()
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
        
    def addLayoutToVLayout(self, layout: QLayout):
        self.VLayout.addLayout(layout)
        
    def makeMessageBox(self) -> QMessageBox:
        return QMessageBox(self)
        