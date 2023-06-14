from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
import sys
from mainwindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



# SI FALLA QUE no se tilde el sistema y de el codigo de error por la salida
# Poner un boton para elegir el lenguaje