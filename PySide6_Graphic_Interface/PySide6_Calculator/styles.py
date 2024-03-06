# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
import qdarktheme
from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
                       PRIMARY_COLOR)

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: #007FFF;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: #00308F;
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: #002D62;
    }}
"""


def SetUpDarkTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}",
            },
        },
        additional_qss=qss
    )