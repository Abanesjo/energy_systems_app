from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.button_add_row.clicked.connect(self.add_row)
        self.button_remove_row.clicked.connect(self.delete_row)
        self.button_reset_rows.clicked.connect(self.reset_rows)

    def add_row(self):
        row_count = self.table_fittings.rowCount()
        print(row_count)
        self.table_fittings.insertRow(row_count)

    def delete_row(self):
        row_count = self.table_fittings.rowCount()
        selected_row = self.table_fittings.currentRow()
        if row_count > 1:
            if selected_row == -1:
                self.table_fittings.removeRow(row_count-1)  
            else:
                self.table_fittings.removeRow(selected_row)
        else:
            self.table_fittings.clearContents()

    def reset_rows(self):
        for i in range(1, self.table_fittings.rowCount()):
            self.table_fittings.removeRow(0)
        self.table_fittings.clearContents()
                
            

