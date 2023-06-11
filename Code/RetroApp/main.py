from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QAction, QFileDialog, QGridLayout, QGroupBox, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.Qsci import QsciScintilla, QsciLexerPython
import sys


class CloseableTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)

    def close_tab(self, index):
        widget = self.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.removeTab(index)


class QueryEditor(QsciScintilla):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLexer(QsciLexerPython())
        self.setFont(QFont("Courier New", 11))
        self.setAutoCompletionThreshold(2)
        self.setAutoCompletionSource(QsciScintilla.AcsAll)
        self.setAutoCompletionCaseSensitivity(False)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tab_widget = CloseableTabWidget()
        self.setCentralWidget(self.tab_widget)
        self.create_menu()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Report-App")

    def create_menu(self):
        ventana_archivo = QAction("Nueva Pestaña", self)
        ventana_script = QAction("Buscar Script", self)

        ventana_archivo.triggered.connect(self.create_new_tab)
        ventana_script.triggered.connect(self.open_file_dialog)

        file_menu = self.menuBar().addMenu("Archivo")
        fila_2 = self.menuBar().addMenu("Scripts")

        fila_2.addAction(ventana_script)
        file_menu.addAction(ventana_archivo)

    def create_new_tab(self):
        new_tab = QWidget()
        layout = QGridLayout(new_tab)

        # Crear el grupo para el área de consultas
        group_box = QGroupBox("Consulta")
        group_layout = QVBoxLayout()
        
        # Crear un área de texto para la consulta
        text_edit = QTextEdit()
        group_layout.addWidget(text_edit)
        
        # Crear un botón para ejecutar la consulta
        execute_button = QPushButton("Ejecutar")
        group_layout.addWidget(execute_button)
        
        group_box.setLayout(group_layout)


        layout.addWidget(group_box)
        self.tab_widget.addTab(new_tab, f'Pestaña {self.tab_widget.count()}')

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos de texto (*.txt)")
        if file_path:
            print(f"Archivo seleccionado: {file_path}")

    def close_current_tab(self):
        current_index = self.tab_widget.currentIndex()
        if current_index != -1:
            self.tab_widget.close_tab(current_index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
