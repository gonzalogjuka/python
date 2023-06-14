from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QAction, QFileDialog, QLabel, QWidget, QVBoxLayout, QFrame, QTextEdit
from PyQt5 import Qsci
import sys,ast,sqlalchemy
from database import DatabaseManager
from pymysql import Connection


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

    def show_result(self, result):
        self.result_text.setText(result)

    def clear_result(self):
        self.result_text.clear()  


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


class QuerySection(QWidget):
    def __init__(self):
        self.connection_config = None
        self.engine = None
        self.connection = None

    def set_connection_config(self, host, database, username, password):
        self.connection_config = {
            'host': host,
            'database': database,
            'username': username,
            'password': password
        }

    def connect(self):
        if self.connection_config:
            # Crear el objeto Engine y establecer la conexión a la base de datos
            connection_string = f"mysql+pymysql://{self.connection_config['username']}:{self.connection_config['password']}@{self.connection_config['host']}/{self.connection_config['database']}"
            self.engine = sqlalchemy.create_engine(connection_string)
            self.connection = self.engine.connect()
            print('Conexión exitosa')
        else:
            print('Configuración de conexión no establecida')

    def is_valid_syntax(self, code):
        try:
            ast.parse(code)
            return True
        except SyntaxError as e:
            error_message = str(e)
            return error_message

    def execute_query(self, query):
        if not query:
            # No se ingresó ninguna consulta
            print("Error: No se ingresó ninguna consulta.")
            return

        # Verificar la sintaxis de la consulta
        syntax_error = self.is_valid_syntax(query)
        if syntax_error:
            # Mostrar el mensaje de error de sintaxis en la aplicación
            print(f"Error de sintaxis: {syntax_error}")
            return

        try:
            # Lógica para ejecutar la consulta y obtener el resultado
            result = self.execute_query_python(query)

            if result is not None:
                # Mostrar el resultado
                print(result)

        except Exception as e:
            # Manejo de errores durante la ejecución de la consulta
            print(f"Error: {str(e)}")

    def execute_query_python(self, query):
        if isinstance(self.connection, Connection):
            try:
                # Crear un cursor para ejecutar consultas
                cursor = self.connection.cursor()

                # Ejecutar la consulta
                cursor.execute(query)

                # Obtener el resultado de la consulta
                result = cursor.fetchall()

                # Cerrar el cursor
                cursor.close()

                return result

            except Exception as e:
            # Manejar cualquier error durante la ejecución de la consulta
                raise Exception(f"Error en la consulta: {str(e)}")
        else:
            print('No hay una conexión establecida a la base de datos')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# SI FALLA QUE no se tilde el sistema y de el codigo de error por la salida
# Poner un boton para elegir el lenguaje
# conectar a la base de datos por medio de ese boton