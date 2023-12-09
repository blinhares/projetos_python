
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from PySide6.QtGui import QIcon
from files.cods.variables import WINDOW_ICON_PATH

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None,*args, **kwargs ):
        super().__init__(parent, *args, **kwargs)
        ###### adicionando opcoes a janela #####
        self.menu_bar = self.menuBar()
        self.op_02 = self.menu_bar.addMenu('teste2')
        self.op_01 = self.menu_bar.addMenu('teste')
        ###### adicionando opcoes a janela #####

        #definindo msg da barra de status
        self.statusBar().showMessage('By: Bruno')
        #definindo titulo da janela
        self.setWindowTitle('Jogo de Dama')
        #definindo Icone da janela
        self.windows_icon = QIcon(str(WINDOW_ICON_PATH))
        self.setWindowIcon(self.windows_icon)
        #criando um layout
        self.v_layout = QVBoxLayout()
        #criando o widget central que recebe o layout
        self.central_widget = QWidget()
        #atribuindo o layout criado ao widget
        self.central_widget.setLayout(self.v_layout)
        #atribuindo o widget central ao widget da window
        self.setCentralWidget(self.central_widget)
        # estudar se ha a real nescessidade de criar um outro widgetecentral ou 
        # simplesmente usar self.setLayout(self.v_layout)


    def add_widget_to_vlayout(self,widget:QWidget):
        """Adiciona Widget no Layout da Pagina"""
        self.v_layout.addWidget(widget)


################ ver / excluir #####################
    def make_msg_box(self):
        return QMessageBox(self)

