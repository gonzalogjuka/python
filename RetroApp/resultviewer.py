from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QTextEdit


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
