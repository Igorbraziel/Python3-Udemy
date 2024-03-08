from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from variables import BIG_FONT_SIZE, DEFAULT_MARGIN, MINIMUM_WIDTH
from utils import isNumOrDot, isEmpty, isValidNumber

class Display(QLineEdit):
    signalEnter = Signal()
    signalDelete = Signal()
    signalEscape = Signal()
    signalNegative = Signal()
    signalClear = Signal()
    signalInput = Signal(str)
    signalOperator = Signal(str)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[DEFAULT_MARGIN for i in range(4)])
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        key = event.key()
        text = event.text()
        KEYS = Qt.Key
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Delete, KEYS.Key_Backspace]
        isEscape = key in [KEYS.Key_Escape]
        
        if isEnter or text == '=':
            self.signalEnter.emit()
            return event.ignore()
        elif isDelete:
            self.signalDelete.emit()
            return event.ignore()
        elif isEscape or text.lower() == 'e' :
            self.signalEscape.emit()
            return event.ignore()
        elif text.upper() == 'N':
            self.signalNegative.emit()
            return event.ignore()
        elif text.upper() == 'C':
            self.signalClear.emit()
            event.ignore()
        elif isNumOrDot(text):
            self.signalInput.emit(text)
            return event.ignore()
        elif not isEmpty(text) and text in '+-/*pP' and text != '^':
            if text.lower() == 'p':
                text = '^'
            self.signalOperator.emit(text)
            return event.ignore()
        elif isEmpty(text):
            return event.ignore()
        
        