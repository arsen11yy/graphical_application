import sys
from PyQt5.QtWidgets import QApplication
from dialog import Dialog

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())
