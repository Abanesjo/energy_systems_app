from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys
import os
import qdarktheme


app = QApplication(sys.argv)
app.setStyleSheet(qdarktheme.load_stylesheet())
stylesheet = qdarktheme.load_stylesheet('light')
QApplication.instance().setStyleSheet(stylesheet)

w = MainWindow(app)
w.show()
app.exec()