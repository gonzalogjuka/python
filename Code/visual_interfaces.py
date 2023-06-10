import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import ast

class VisualInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Interfaz Visual")
        self.syntax_checked = False  # Indicador de chequeo de sintaxis realizado
        self.check_syntax_button = tk.Button(self.window, text="Chequeo de Sintaxis", command=self.syntax_check)
        self.check_syntax_button.pack()
        self.check_security_button = tk.Button(self.window, text="Chequeo de Seguridad", command=self.security_check)
        self.check_security_button.pack()
        self.run_checks_button = tk.Button(self.window, text="Ejecutar Chequeos", command=self.run_checks)
        self.run_checks_button.pack()
        self.output_text = tk.Text(self.window, height=10, width=50)
        self.output_text.pack()

    def syntax_check(self):
        code = self.get_code_text()

        if self.syntax_checked:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "El código ya ha sido chequeado.")
        else:
            try:
                compile(code, "<string>", "exec")
                result = "El código tiene una sintaxis válida."
            except SyntaxError as e:
                result = f"Error de sintaxis: {str(e)}"

            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Resultado del chequeo de sintaxis" + "\n")
            self.output_text.insert(tk.END, result + "\n")
            self.syntax_checked = True

    def security_check(self):
        code = self.get_code_text()

        # Medidas de seguridad a nivel de código

        # 1. Validación de entradas
        if "import" in code:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "El código no debe contener la instrucción 'import'.")
            return

        # 2. Análisis del código utilizando la biblioteca 'ast'
        try:
            compile(code, "<string>", "exec")
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "El código tiene una sintaxis válida.")
        except SyntaxError as e:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"Error de sintaxis: {str(e)}")

        # 3. Implementar otras restricciones de seguridad

        result = "Resultado del chequeo de seguridad"
        self.output_text.insert(tk.END, result + "\n")

    def run_checks(self):
        self.syntax_check()
        self.security_check()

    def run(self):
        self.window.mainloop()

    def get_code_text(self):
        return self.output_text.get(1.0, tk.END).strip()

interface = VisualInterface()
interface.run()
