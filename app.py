from PySide2.QtWidgets import QApplication
from controllers.Hexadecimal import Hexadecimal

if __name__  == "__main__":
    app = QApplication()
    window = Hexadecimal()
    window.setMaximumSize(470, 387)
    window.setMinimumSize(470, 387)
    window.setWindowTitle("LyA")
    window.show()
    app.exec_()