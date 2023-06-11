import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import re

class VisualInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Interfaz Visual")
        self.syntax_result = None  # Resultado del chequeo de sintaxis
        self.security_result = None  # Resultado del chequeo de seguridad
        self.check_syntax_button = tk.Button(self.window, text="Chequeo de Sintaxis", command=self.syntax_check)
        self.check_syntax_button.pack()
        self.check_security_button = tk.Button(self.window, text="Chequeo de Seguridad", command=self.security_check)
        self.check_security_button.pack()
        self.output_text = tk.Text(self.window, height=10, width=50)
        self.output_text.pack()

    def syntax_check(self):
        if self.syntax_result is not None:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "El código ya ha sido chequeado.")
            self.output_text.insert(tk.END, self.syntax_result + "\n")
            return

        code = self.get_code_text()

        pattern = r"import\s+"
        if re.search(pattern, code):
            self.syntax_result = "Error de sintaxis: El código no debe contener la instrucción 'import'."
        else:
            self.syntax_result = "El código tiene una sintaxis válida."

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Resultado del chequeo de sintaxis" + "\n")
        self.output_text.insert(tk.END, self.syntax_result + "\n")

    def security_check(self):
        if self.security_result is not None:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "El código ya ha sido chequeado.")
            self.output_text.insert(tk.END, self.security_result + "\n")
            return

        code = self.get_code_text()

        # Medidas de seguridad a nivel de código

        # 1. Validación de entradas
        if "import" in code:
            self.security_result = "El código no debe contener la instrucción 'import'."
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, self.security_result + "\n")
            return

        # 2. Análisis del código utilizando la biblioteca 'ast'
        pattern = r"\bexec\b"
        if re.search(pattern, code):
            self.security_result = "Error de sintaxis: El código no debe contener la instrucción 'exec'."
        else:
            try:
                exec(code)
                self.security_result = "El código tiene una sintaxis válida."
            except SyntaxError as e:
                self.security_result = f"Error de sintaxis: {str(e)}"

        # 3. Implementar otras restricciones de seguridad

        result = "Resultado del chequeo de seguridad"
        self.output_text.insert(tk.END, result + "\n")
        self.output_text.insert(tk.END, self.security_result + "\n")

    def run_checks(self):
        self.syntax_check()
        self.security_check()

    def run(self):
        self.window.mainloop()

    def get_code_text(self):
        return self.output_text.get(1.0, tk.END).strip()

interface = VisualInterface()
interface.run()
