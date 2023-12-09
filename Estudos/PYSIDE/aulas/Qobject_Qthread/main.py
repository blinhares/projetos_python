''' manual https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/ '''


#importando bibliotecas nescessarias
from PySide6.QtCore import QRunnable , Slot , QThreadPool

############

from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QWidget, QApplication
from workerui_ui import Ui_mywidget
import sys, time

############## criando o worker Thread #############

class Worker1(QRunnable):
    '''
    Worker thread
    '''

    @Slot()
    def run(self):
        value = '0'
        for i in range(5):
            value = str(i)
            print(value)
            time.sleep(1)

    

############## fim o worker Thread #############

class MyWidget(QWidget,Ui_mywidget):
    def __init__(self, parent= None ):
        super().__init__(parent)
        self.setupUi(self)
        self.button1.clicked.connect(self.hard_work1)
        self.button_2.clicked.connect(self.hard_work2)
        ########### inicializando multitask ######
        self.threadpool = QThreadPool()
        print(f"Multithreading with maximum {self.threadpool.maxThreadCount()} threads")
        ########### inicializando multitask ######


    def hard_work1(self):
        worker = Worker1() # instancia o objeto QRunnable que vai ser responsavel pela thread
        #aqui a threadpool recebe o objeto o qual vai executar
        # executa a funcao run()  por padrao
        self.threadpool.start(worker) 
        


    def hard_work2(self):
        print('bot 2 pression')
        self.label_2.setText('2 Iniciado')
        time.sleep(5)
        self.label_2.setText('2 Terminado')



if __name__=='__main__':
    app = QApplication(sys.argv)
    mywidget = MyWidget()
    mywidget.show()

    app.exec()