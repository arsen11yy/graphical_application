# data_processing_lib/data_processor.py
from PyQt5.QtWidgets import QMessageBox

def validate_input(value, boundary_name):
    try:
        int(value)
        return True
    except ValueError:
        show_error_dialog("Ошибка ввода", f"Параметр {boundary_name} должен быть целым числом.")
        return False

def show_error_dialog(title, message):
    error_dialog = QMessageBox()
    error_dialog.setIcon(QMessageBox.Critical)
    error_dialog.setWindowTitle(title)
    error_dialog.setText(message)
    error_dialog.exec_()
