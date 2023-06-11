from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QAction
import sys


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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tab_widget = CloseableTabWidget()
        self.setCentralWidget(self.tab_widget)
        self.create_menu()
        self.setGeometry(100, 100, 800, 600)

    def create_menu(self):
        new_action = QAction("Nueva Pestaña", self)
        new_action.triggered.connect(self.create_new_tab)

        file_menu = self.menuBar().addMenu("Archivo")
        file_menu.addAction(new_action)

    def create_new_tab(self):
        new_tab = QWidget()
        layout = QVBoxLayout(new_tab)
        self.tab_widget.addTab(new_tab, f'Pestaña {self.tab_widget.count()}')

    def close_current_tab(self):
        current_index = self.tab_widget.currentIndex()
        if current_index != -1:
            self.tab_widget.close_tab(current_index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
