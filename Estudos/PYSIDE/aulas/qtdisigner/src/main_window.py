from typing import cast
from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QKeyEvent
import sys
from window_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication
# criar um classe herdando a classe do arquivo criado e qmainwindows
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None ):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_send.clicked.connect(self._change_label_result)

        #filtrando eventos de um widget
        self.line_name.installEventFilter(self)

    def _change_label_result(self):
        text = self.line_name.text()
        self.labelresult.setText(text)

    #para filtrar eventos em qualquer widget usase a func abaixo
    def eventFilter(self, watched: QObject, event: QEvent) :
        # print(event.type())#imprime o evento capturado

        #filtrando por evento especifico
        if event.type() == QEvent.Type.KeyPress:
            # trocar tipo da variavel event
            event = cast(QKeyEvent, event)
            print(event.text())

        return super().eventFilter(watched, event)


if __name__=='__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    app.exec()