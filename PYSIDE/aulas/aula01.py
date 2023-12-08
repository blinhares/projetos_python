from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication()

botao = QPushButton('Texto Botao')
botao.setStyleSheet('font-size: 40px; color: red') # altera estilo do texto (tamanho e cor)
botao.show() #adiciona o botao na hierarquia da janela

app.exec() #executa o looping da aplicacao 