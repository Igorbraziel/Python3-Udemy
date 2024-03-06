from typing import TYPE_CHECKING
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE, DARKEST_PRIMARY_COLOR
from utils import isNumOrDot, isValidNumber

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MyMainWindow

class MyButton(QPushButton):
    def __init__(self, text: str, parent: QWidget | None = None):
        super().__init__(text, parent)
        self.configButtonStyle()
        
    def configButtonStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 100)
        

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MyMainWindow', parent: QWidget | None = None):
        super().__init__(parent)
        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0',  '', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._leftNumber = None
        self._rightNumber = None
        self._op = None
        self.makeGrid()
        
        
    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)
        
    
    def makeGrid(self):
        self.display.signalEnter.connect(self._eq_)
        self.display.signalDelete.connect(self.removeLastDisplayDigit)
        self.display.signalEscape.connect(self.window.close)
        self.display.signalInput.connect(self.insertNumbers)
        self.display.signalOperator.connect(self._operatorWrite)
        for i, row in enumerate(self._grid_mask):
            for j , button_text in enumerate(row):
                button = MyButton(button_text)
                if not isNumOrDot(button_text) and len(button_text) > 0:
                    button.setProperty('cssClass', 'specialButton')
                    self.configSpecialButton(button)
                if button_text == '0':
                    self.addWidget(button, i, j, 1, 2)
                elif button_text != '':
                    self.addWidget(button, i, j)
                    
                slot = self._makeSlot(self.insertTextInDisplay, button)
                self.connectButtonClicked(button, slot)
                
                    
    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def inner():
            func(*args, **kwargs)
        return inner
    
            
    def insertTextInDisplay(self, button: QPushButton):
        display_text = self.display.text() + button.text()
        if isValidNumber(display_text):
            self.display.insert(button.text())
            
            
    @Slot()
    def insertNumbers(self, numberText: str):
        display_text = self.display.text() + numberText
        if isValidNumber(display_text):
            self.display.insert(numberText)
            
    
    def connectButtonClicked(self, button: QPushButton, slot: Slot):
        button.clicked.connect(slot)
        
    @Slot()    
    def removeLastDisplayDigit(self):
        display_text = self.display.text()
        new_display_text = ''
        for i in range(len(display_text)):
            if i + 1 < len(display_text):
                new_display_text += display_text[i]
        self.display.setText(new_display_text)
        
        
    def _clear(self, msg: str = 'Your Account'):
        self._leftNumber = None
        self._rightNumber = None
        self._op = None
        self.equation = msg
        self.display.clear()
        
    def _operatorClicked(self, button: MyButton):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()
        
        if not isValidNumber(displayText) and self._leftNumber is None:
            self._showMessageBox('No number at left')
            return
    
        if self._leftNumber is None:
            self._leftNumber = float(displayText)
            
        self._op = buttonText
        self.equation = f'{self._leftNumber} {self._op} ???'
        
    @Slot()
    def _operatorWrite(self, text: str):
        buttonText = text
        displayText = self.display.text()
        self.display.clear()
        
        if not isValidNumber(displayText) and self._leftNumber is None:
            self._showMessageBox('No number at left')
            return
    
        if self._leftNumber is None:
            self._leftNumber = float(displayText)
            
        self._op = buttonText
        self.equation = f'{self._leftNumber} {self._op} ???'
        
    @Slot()
    def _eq_(self):
        displayText = self.display.text()
        
        if not isValidNumber(displayText) or self._leftNumber is None or self._op is None:
            self._showMessageBox('No number at right')
            return

        if self._rightNumber is None:
            self._rightNumber = float(displayText)
            
        self.equation = f'{self._leftNumber} {self._op} {self._rightNumber}'
        
        try:
            if self._op == '^':
                result = round(eval(self.equation.replace('^', '**')), 2)
            else:
                result = round(eval(self.equation), 2)
        except ZeroDivisionError:
            result = 'ZeroDivisionError'
        except OverflowError:
            result = 'OverflowError'
        except:
            result = 'Unknown Error'
        
        if isinstance(result, str):
            self._showMessageBox(result)
            result = None
        else:
            self.info.setText(f'{self.equation} = {result}')
        self.equation = self.info.text()
        self.display.clear()
        self._leftNumber = result
        self._op = None
        self._rightNumber = None
                
        
    def configSpecialButton(self, button: QPushButton):
        button_text = button.text()
        
        if button_text == 'C':
            slot = self._makeSlot(self._clear, 'Your Account')
            self.connectButtonClicked(button, slot)
        elif button_text == '◀':
            slot = self._makeSlot(self.removeLastDisplayDigit)
            self.connectButtonClicked(button, slot)
        elif button_text in '+-/*^':
            slot = self._makeSlot(self._operatorClicked, button)
            self.connectButtonClicked(button, slot)
        elif button_text == '=':
            slot = self._makeSlot(self._eq_)
            self.connectButtonClicked(button, slot)
            
    
    def _showMessageBox(self, text: str):
        msgBox = self.window.makeMessageBox()
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.setStandardButtons(
            msgBox.StandardButton.Cancel
        )
        msgBox.setText(text)
        msgBox.adjustSize()
        msgBox.exec()
        self._clear()