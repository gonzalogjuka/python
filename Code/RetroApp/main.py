import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTextEdit, QAction


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()

    def tabCloseRequested(self, index):
        # Cerrar la pestaña
        self.removeTab(index)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Retro App")
        self.setGeometry(100, 100, 800, 600)
        self.tab_widget = TabWidget()
        self.setCentralWidget(self.tab_widget)
        self.tab_counter = 1

        self.create_new_tab()  # Crear la primera pestaña al iniciar la aplicación

        self.create_menu()

    def create_new_tab(self):
        # Crear una nueva pestaña
        tab = QWidget()
        self.tab_widget.addTab(tab, f'Pestaña {self.tab_counter}')

        # Agregar el contenido a la pestaña
        layout = QVBoxLayout(tab)
        text_edit = QTextEdit()
        layout.addWidget(text_edit)

        # Incrementar el contador de pestañas
        self.tab_counter += 1

    def create_menu(self):
        # Crear el menú
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Archivo")

        new_action = QAction("Nuevo", self)
        new_action.triggered.connect(self.create_new_tab)
        file_menu.addAction(new_action)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
