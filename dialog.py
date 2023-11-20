from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot

class Dialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("dialog.ui", self)

    def validate_input(self, value, boundary_name):
        try:
            int(value)
            return True
        except ValueError:
            self.show_error_dialog("Ошибка ввода", f"Параметр {boundary_name} должен быть целым числом.")
            return False

    def show_error_dialog(self, title, message):
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle(title)
        error_dialog.setText(message)
        error_dialog.exec_()

    @pyqtSlot()
    def calculate(self):
        a = self.lineEditA.text()
        b = self.lineEditB.text()

        if not (self.validate_input(a, "A") and self.validate_input(b, "B")):
            return

        a, b = int(a), int(b)

        for i in range(a, b + 1):
            self.listWidget.addItem(str(i))
