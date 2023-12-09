import sys
from PySide6.QtWidgets import QApplication #, QMainWindow, QVBoxLayout, QWidget
from files.cods.main_windows import MainWindow



def main():
    app = QApplication(sys.argv)

    #instanciando nova janela
    main_window = MainWindow()    
    main_window.show()  


    app.exec()
    

if __name__ == '__main__':
    main()