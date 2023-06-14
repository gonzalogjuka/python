from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QAction, QFileDialog, QVBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5 import Qsci
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame, QTextEdit,QMessageBox
import sys
import ast
from database import DatabaseManager

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
            # Verificar la sintaxis del código
            ast.parse(query)

            # Lógica para ejecutar la consulta y obtener el resultado
            #result = is_valid_syntax(query)

            #if result is not None:
                # Mostrar el resultado en la ventana de Resultado
             #   self.result_viewer.show_result(result)

        except SyntaxError as e:
            # Error de sintaxis en el código
            self.show_error_message(f"Error de sintaxis en el código:\n{str(e)}")

        except Exception as e:
            # Manejo de otros errores durante la ejecución de la consulta
            self.show_error_message(f"Error durante la ejecución del código:\n{str(e)}")

    def show_error_message(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.exec_()

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

        opcion_connect_db = QAction("Conectar Base de datos", self)
        opcion_connect_db.triggered.connect(self.funcion_opcion_connect_db)

        fila_2.addAction(ventana_script)
        file_menu.addAction(ventana_archivo)
        file_menu.addAction(opcion_connect_db)
    
    def funcion_opcion_connect_db(self):
        print("Trigger Ok") # testear con la base y el otro script

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

    def connect_to_database(self):
        # Crear una instancia de la clase DatabaseManager
        db_manager = DatabaseManager()

        # Establecer la configuración de conexión a la base de datos
        db_manager.set_connection_config('localhost', 'mydatabase', 'username', 'password')

        # Conectar a la base de datos
        db_manager.connect()

# SI FALLA QUE no se tilde el sistema y de el codigo de error por la salida
# Poner un boton para elegir el lenguaje y conectar a la base de datos por medio de ese boton

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
