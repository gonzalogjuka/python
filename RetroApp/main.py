from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QLabel, QLineEdit
import sys
from mainwindow import MainWindow


class CustomMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

