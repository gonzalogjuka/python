from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QAction, QFileDialog, QVBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5 import Qsci
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame, QTextEdit
import sys
import ast

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

        # Establecer corrector de Python
        python_lexer = Qsci.QsciLexerPython()
        self.editor.setLexer(python_lexer)
        # Establecer corrector de SQL
        sql_lexer = Qsci.QsciLexerSQL()
        self.editor.setLexer(sql_lexer)

        self.editor.setMarginWidth(0, "000")  # Números de línea a la izquierda
        self.editor.setMarginLineNumbers(0, True)
        self.editor.setFolding(Qsci.QsciScintilla.BoxedFoldStyle)
        self.editor.setBraceMatching(Qsci.QsciScintilla.SloppyBraceMatch)
        self.main_layout.addWidget(self.editor)
        self.setFixedHeight(130)  # Establecer la altura deseada

    def get_query(self):
        return self.editor.text()
    
class ResultViewer(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.Box)
        self.setLineWidth(1)
        layout = QVBoxLayout(self)
        self.result_label = QLabel("Resultado")
        self.result_text = QTextEdit()
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_text)

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
        query = self.query_editor.get_query()

        if not query:
            # No se ingresó ninguna consulta
            self.result_viewer.show_error("Error: No se ingresó ninguna consulta.")
            return

        try:
            # Lógica para ejecutar la consulta y obtener el resultado
            result = execute_query_python(query)

            if result is not None:
                # Mostrar el resultado en la ventana de Resultado
                self.result_viewer.show_result(result)

        except Exception as e:
            # Manejo de errores durante la ejecución de la consulta
            self.result_viewer.show_error(f"Error: {str(e)}")

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

def is_python_code(code):
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False
    
    # SI FALLA QUE no se tilde el sistema y de el codigo de error por la salida

def execute_query_python(code):
    try:
        # Ejecutar el código de Python
        result = eval(code)
        return result

    except Exception as e:
        # Manejar cualquier error durante la ejecución del código
        raise e

# Poner un boton para elegir el lenguaje y conectar a la base de datos por medio de ese boton

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
