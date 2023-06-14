from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5 import Qsci


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
