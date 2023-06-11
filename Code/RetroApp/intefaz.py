from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QAction, QFileDialog, QVBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QColor, QFont
from PyQt5 import Qsci
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
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

class QueryEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.editor = Qsci.QsciScintilla(self)
        self.editor.setLexer(Qsci.QsciLexerPython())  # Establecer corrector de Python
        self.editor.setMarginWidth(0, "000")  # Números de línea a la izquierda
        self.editor.setMarginLineNumbers(0, True)
        self.editor.setFolding(Qsci.QsciScintilla.BoxedFoldStyle)
        self.editor.setBraceMatching(Qsci.QsciScintilla.SloppyBraceMatch)
        self.main_layout.addWidget(self.editor)
        self.setFixedHeight(150)  # Establecer la altura deseada


class ResultViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.result_label = QLabel("Resultado:")
        self.result_text = QLabel("")
        self.main_layout.addWidget(self.result_label)
        self.main_layout.addWidget(self.result_text)


class QuerySection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.query_editor = QueryEditor(self)
        self.execute_button = QPushButton("Ejecutar")
        self.result_viewer = ResultViewer(self)
        self.main_layout.addWidget(self.query_editor)
        self.main_layout.addWidget(self.execute_button)
        self.main_layout.addWidget(self.result_viewer)
        self.execute_button.clicked.connect(self.execute_query)

    def execute_query(self):
        query = self.query_editor.editor.text()
        # Aquí puedes realizar la ejecución de la consulta y obtener el resultado
        result = "Resultado de la consulta"

        self.result_viewer.result_text.setText(result)

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
        self.tab_widget.addTab(new_tab, f'Pestaña {self.tab_widget.count()}')
        query_section = QuerySection(new_tab)
        layout = QVBoxLayout(new_tab)
        layout.addWidget(query_section)

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
