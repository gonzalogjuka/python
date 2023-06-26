from tkinter import Tk, filedialog
from pylint.lint import PyLinter
from pylint.reporters.text import TextReporter

def solicitar_archivo():
    root = Tk()
    root.withdraw()

    # Mostrar el cuadro de diálogo para seleccionar el archivo
    archivo = filedialog.askopenfilename(title="Seleccione el archivo a verificar")

    return archivo

class MinutaReporter(TextReporter):
    def __init__(self, output_file):
        super().__init__(output_file)
        self.llamativos = 0
        self.enlaces = []

    def handle_message(self, msg):
        super().handle_message(msg)

        # Verificar si el mensaje es de categoría "error"
        if msg.category == "error":
            # Incrementar el contador de objetos llamativos
            self.llamativos += 1

            # Obtener las sugerencias asociadas al mensaje
            suggestions = getattr(msg, 'suggestions', [])

            if suggestions:
                # Agregar las sugerencias al informe
                self.out.write(f"\nSugerencias para {msg.symbol}:\n")
                for suggestion in suggestions:
                    self.out.write(f" - {suggestion}\n")

            # Agregar explicación detallada para cada error
            self.out.write(f"\nExplicación para {msg.msg_id}:\n")
            self.out.write(f" - Categoría: {msg.category}\n")
            self.out.write(f" - Descripción: {msg.msg}\n")
            self.out.write(f" - Archivo: {msg.path}\n")
            self.out.write(f" - Línea: {msg.line}\n")
            self.out.write(f" - Columna: {msg.column}\n")

    def display_messages(self):
        super().display_messages(None)

        # No agregar los enlaces aquí

def verificar_codigo():
    # Solicitar al usuario la ruta del archivo a verificar utilizando el cuadro de diálogo
    archivo = solicitar_archivo()

    # Realizar verificación del código utilizando Pylint
    linter = PyLinter()
    linter.load_default_plugins()
    linter.check([archivo])

    # Generar archivo de salida en formato de minuta con los errores de categoría "error"
    with open("verificacion_minuta.txt", "w") as archivo_salida:
        reporter = MinutaReporter(archivo_salida)
        linter.set_reporter(reporter)
        linter.check([archivo])

        # Agregar enlaces al final del reporte
        reporter.out.write("\nRecursos adicionales:")
        reporter.out.write("\n- Documentación oficial de Python: https://docs.python.org/es/")
        reporter.out.write("\n- Stack Overflow: https://es.stackoverflow.com/")
        reporter.out.write("\n- Tutorial de Python: https://www.learnpython.org/es/")

    # Mostrar la cantidad de objetos llamativos encontrados
    print(f"Se encontraron {reporter.llamativos} objetos llamativos en el código.")

# Llamar a la función principal
verificar_codigo()
