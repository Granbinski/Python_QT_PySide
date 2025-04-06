from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from qdarktheme import load_stylesheet



def callback():
  print('Clicado, clicadinho!!!')

app = QApplication()

loder =QUiLoader()
window = loder.load('login.ui')

window.pushButton.clicked.connect(callback)

window.show()
app.setStyleSheet(load_stylesheet('light'))
app.exec()