from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from qdarktheme import load_stylesheet

app = QApplication()

loder =QUiLoader()
window = loder.load('login.ui')
window.show()
app.setStyleSheet(load_stylesheet('light'))
app.exec()