import sqlalchemy

class DatabaseManager:
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
