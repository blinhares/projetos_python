
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow
#para colocar tudo em uma unica janela, precisamos criar um widget central
app = QApplication()
def slot_exmpl(satausbar):
    status_bar.showMessage('O botao foi clicado')


#ccriando botoes
button_01 = QPushButton('Botao 01')
button_01.setStyleSheet('font-size: 80px; color: red')

button_02 = QPushButton('Botao 02')
button_02.setStyleSheet('font-size: 40px; color: red')

button_03 = QPushButton('Botao 03')
button_03.setStyleSheet('font-size: 600px; color: red')
#QmainWIndows recebe o Widget central

#criando o layout
layout = QGridLayout()
layout.addWidget(button_01,1,1)
layout.addWidget(button_02,2,2)

# criando widget central
widget_central = QWidget()
widget_central.setLayout(layout)

window = QMainWindow()# criando a janela centra
window.setCentralWidget(widget_central) # recebe um cenral widget
window.setWindowTitle('Teste em Pyside6') # definindo nome da janela
window.show() #jogar widget na hierarquia
# com a adiccao da janela central eu posso usar alguns recursos
#satus 
status_bar = window.statusBar()
status_bar.showMessage('Teste de menssagem na barra')
#menu bar
menu = window.menuBar()
menu_principal = menu.addMenu('Primeiro Menu')
primeira_acao = menu_principal.addAction('Primeira acao')
primeira_acao.triggered.connect( lambda sb:slot_exmpl(status_bar)) #executa acao quando botao é apertado

segunda =menu.addMenu('Segunda Menu').addAction('Teste')

app.exec()