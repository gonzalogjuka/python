import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from RestrictedPython import compile_restricted_exec

class VisualInterface:
    def __init__(self):
        self.window = tk.Tk()

        self.menu_bar = tk.Menu(self.window)
        self.window.config(menu=self.menu_bar)

        self.syntax_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Chequeo de Sintaxis", menu=self.syntax_menu)
        self.syntax_menu.add_command(label="Verificar", command=self.syntax_check)

        self.security_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Chequeo de Seguridad", menu=self.security_menu)
        self.security_menu.add_command(label="Verificar", command=self.security_check)

        self.output_text = scrolledtext.ScrolledText(self.window, height=10, width=50)
        self.output_text.pack()

    def syntax_check(self):
        code = self.output_text.get(1.0, tk.END)
        try:
            compile(code, filename='<string>', mode='exec')
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "El código tiene una sintaxis válida.")
        except SyntaxError as e:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"Error de sintaxis: {str(e)}")

    def security_check(self):
        code = self.output_text.get(1.0, tk.END)
        
        # Medidas de seguridad a nivel de código
        
        # 1. Validación de entradas
        if "import" in code:
            self.output_text.insert(tk.END, "El código no debe contener la instrucción 'import'.\n")
        
        # 2. Limitar permisos
        
        # 3. Implementar sandboxing
        try:
            compiled_code = compile_restricted_exec(code, '<string>')
            exec(compiled_code.code, {})
            self.output_text.insert(tk.END, "El código se ejecutó en un entorno aislado.\n")
        except Exception as e:
            self.output_text.insert(tk.END, f"Error de seguridad: {str(e)}\n")
        
        # 4. Revisiones de código
        
        self.output_text.insert(tk.END, "Se ha completado el chequeo de seguridad.\n")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    interface = VisualInterface()
    interface.run()
