import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from buttons import  ButtonGrid
import qdarktheme

def main():
    app = QApplication(sys.argv)
    #definindo icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    app.setWindowIcon(icon) # nao funcinou (deveria criar um icone na bandeija)
    
    #aplicando tema
    #esta opcao nao funciona
    # setupTheme()
    app.setStyleSheet(qdarktheme.load_stylesheet())
    #criando janela
    window = MainWindow()


    #criando um info
    info = Info('')
    window.add_widget_to_vlayout(info)
    
    #criando um display
    display = Display()
    #adicionando display a janela
    window.add_widget_to_vlayout(display)

    #adicionando uma grid de botoes
    button_grid = ButtonGrid(display=display, info=info, window=window)

    window.vlayout.addLayout(button_grid)

    window.adjustfixedsize()
    
    window.show()


    app.exec()

if __name__ == '__main__':
    main()