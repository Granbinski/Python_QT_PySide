from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import (QApplication, QLabel,QPushButton, QWidget, QVBoxLayout, QMainWindow)
from qdarktheme import load_stylesheet



def callback():
  print('Clicado, clicadinho!!!')


class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    base = QWidget()
    layout = QVBoxLayout()

    font = QFont()
    font.setPixelSize(90)
   

    self.label = QLabel("Hellow world!!!!")
    self.label.setFont(font)
    self.label.setAlignment(Qt.AlignCenter)


    botao = QPushButton("Clique!")
    botao.setFont(font)
    
    botao.clicked.connect(self.muda_label)

    layout.addWidget(self.label)
    layout.addWidget(botao)

    base.setLayout(layout)
    self.setCentralWidget(base)

    menu = self.menuBar()
    arquivo_menu = menu.addMenu('Menu')
    action = QAction('Printado!!!')
    action.triggered.connect(callback)
    arquivo_menu.addAction(action)
  def muda_label(self):
    self.label.setText('Clicadão!!!!!')

app = QApplication()
app.setStyleSheet(load_stylesheet('light'))
janela = Window()
janela.show()
app.exec()