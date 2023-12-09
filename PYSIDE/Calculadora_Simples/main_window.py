from typing import Optional
# import PySide6.QtCore
from PySide6.QtWidgets import  QMainWindow, \
    QVBoxLayout, QWidget, QMessageBox
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None,*args, **kwargs ) -> None:
        super().__init__(parent, *args, **kwargs)
        # #criando widget
        # self.label = QLabel('O meu texto')
        # self.label.setStyleSheet('font-size: 50px')
        self.statusBar().showMessage('By: Bruno')
        #criando layout
        self.vlayout = QVBoxLayout()
        # #adicionando label ao widget
        # self.vlayout.addWidget(self.label)
        #criando central widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.vlayout)
        #criando janela principal
        self.setWindowTitle('Calculadora by: B2L')
        self.setCentralWidget(self.central_widget)
        #definindo icone
        icon = QIcon(str(WINDOW_ICON_PATH))
        self.setWindowIcon(icon)
        
        
    def adjustfixedsize(self):
        """
        Esta funcao ajusta o tamanho da janela de acordo com seus componentes
        e o fixa para que o usuarioo nao a altere.
        """
        #configurando dimensoes da janela
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def add_widget_to_vlayout(self, widget:QWidget):
        self.vlayout.addWidget(widget)

    #adiciona recurso para enviar msg ao usuario  
    def make_msg_box(self):
        return QMessageBox(self)
