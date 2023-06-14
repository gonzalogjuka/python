from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QAction, QFileDialog, QLabel, QWidget, QVBoxLayout, QFrame, QTextEdit, QStatusBar
from database import DatabaseManager
from querysection import QuerySection
from closeabletabwidget import CloseableTabWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tab_widget = CloseableTabWidget()
        self.setCentralWidget(self.tab_widget)
        self.create_menu()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Report-App")
        self.statusBar = self.statusBar()
        
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
        self.statusBar.showMessage("Conexión exitosa")

    def create_new_tab(self):
        new_tab = QWidget()
        self.tab_widget.addTab(new_tab, f'Pestaña {self.tab_widget.count()}')
        query_section = QuerySection(self)
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

    def show_error_message(self, message):
        self.statusBar.showMessage(f"Error: {message}")