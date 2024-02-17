import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

from opengl_window import OpenGLWindow

if __name__ == "__main__":
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseDesktopOpenGL)
    app = QApplication(sys.argv)
    w = OpenGLWindow()
    w.show()
    sys.exit(app.exec())
