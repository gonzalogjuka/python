import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit


class InputWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de Input")
        self.setGeometry(100, 100, 800, 600)

        self.create_text_editor()

    def create_text_editor(self):
        self.text_editor = QTextEdit()
        self.setCentralWidget(self.text_editor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputWindow()
    window.show()
    sys.exit(app.exec_())
