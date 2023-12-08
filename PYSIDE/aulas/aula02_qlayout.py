from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout
#para colocar tudo em uma unica janela, precisamos criar um widget central
app = QApplication()

#ccriando botoes
button_01 = QPushButton('Botao 01')
button_01.setStyleSheet('font-size: 40px; color: red')

button_02 = QPushButton('Botao 02')
button_02.setStyleSheet('font-size: 40px; color: red')

#criando o layout
layout = QGridLayout()
layout.addWidget(button_01,1,1)
layout.addWidget(button_02,2,2)

# criando widget central
widget_central = QWidget()
widget_central.setLayout(layout)
widget_central.show() #pjogar widget na hierarquia
app.exec()