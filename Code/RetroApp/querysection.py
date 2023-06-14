from PyQt5.QtWidgets import QWidget, QVBoxLayout,QPushButton
from resultviewer import ResultViewer
from queryeditor import QueryEditor
from sqlalchemy import create_engine
from pymysql import Connection
import ast


class QuerySection(QWidget):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.connection_config = None
        self.engine = None
        self.connection = None
        self.main_window = main_window
        self.main_layout = QVBoxLayout(self)
        self.query_editor = QueryEditor(self)
        self.execute_button = QPushButton("Ejecutar")
        self.result_viewer = ResultViewer(self)
        self.main_layout.addWidget(self.query_editor)
        self.main_layout.addWidget(self.execute_button)
        self.main_layout.addWidget(self.result_viewer)
        self.execute_button.clicked.connect(self.execute_query)

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
            self.engine = create_engine(connection_string)
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
        query = self.query_editor.get_query()
        
        if not query:
            # No se ingresó ninguna consulta
            print("Error: No se ingresó ninguna consulta.")
            return

        # Verificar la sintaxis de la consulta
        syntax_error = self.is_valid_syntax(query)
        if syntax_error:
            # Mostrar el mensaje de error de sintaxis en la aplicación
            self.main_window.show_error_message(syntax_error)
            #print(f"Error de sintaxis: {syntax_error}")
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
