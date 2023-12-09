from typing import Optional
import math
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE, BUTTON_SIZE
from utilis import is_num_or_dot, is_empty, is_valid_number

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from display import Display
    from main_window import MainWindow
    from info import Info

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()

    
    def config_style(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(BUTTON_SIZE,BUTTON_SIZE)

class ButtonGrid(QGridLayout):
    def __init__(self, display:'Display',info:'Info', window:'MainWindow', *args, **kwargs):
        super().__init__( *args, **kwargs)
        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equation_inicial_value = 'Bem-Vindo'
        self.equation = self._equation_inicial_value
        self._right = None #armazena o numero da esquerda
        self._left = None #armazenda o numero da direita
        self._op = None #armazena o operador

        self.make_grid()
    #getter e setter
    @property
    def equation(self):
        return self._equation
    #essa funcao faz com que sempre que o calor de equation mude o texto do display tambem mude
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)
        
    def make_grid(self):
        # self.display.eq_request.connect(lambda: print(123)) #conectando o signal criado em display
        self.display.eq_pressed.connect(self._eq) #conectando o signal criado em display
        self.display.del_pressed.connect(self._back_space) #conectando o signal criado em display
        self.display.clear_pressed.connect(self._clear) #conectando o signal criado em display
        self.display.input_pressed.connect(self._insert_but_text_to_display)
        self.display.operator_pressed.connect(self._operator_clicked)

        for row_number,row in enumerate(self._grid_mask):
            for column_numb, button_text in enumerate(row):
                #criando botao
                button = Button(button_text)
                #criando slot
                slot = self._make_slot(
                self._insert_but_text_to_display, button_text
                )
                self._connect_button_clicked(button, slot)
                #definindo botoes epeciais
                self._config_especial_button(button)

                if is_num_or_dot(button_text) :
                    self.addWidget(button,row_number, column_numb)
                
                else:
                    self.addWidget(button,row_number, column_numb)

    def _make_slot(self, func, *args, **kwargs):
        @Slot()
        def real_slot():
            func(*args, **kwargs)
        return real_slot

    @Slot()
    def _back_space(self):
        self.display.backspace()
        self.display.setFocus()#volta o foco para o qlabel


    @Slot()
    def _insert_but_text_to_display(self,button_text):
        new_display_value = self.display.text() + button_text
        #somente mostra nos display se o numero for valido
        if not is_valid_number(new_display_value):
            return
        self.display.insert(button_text)
        self.display.setFocus()#volta o foco para o qlabel
        # self.equation = new_display_value
        
    def _connect_button_clicked(self,button, slot ):
        button.clicked.connect(slot)

    def _config_especial_button(self, button):
        text = button.text()
        if text == 'C':
            self._connect_button_clicked(button, self._clear)

        if text in '+-/*^':
            self._connect_button_clicked(
                button, 
                self._make_slot(self._operator_clicked, button.text()))
        if text == '=':
            self._connect_button_clicked(button, self._eq)
        
        if text == '◀':
            self._connect_button_clicked(button, self._back_space)

        if text == 'N':
            self._connect_button_clicked(button, self._invert_number)
        
        
    @Slot()
    def _clear(self):
        self._right = None #armazena o numero da esquerda
        self._left = None #armazenda o numero da direita
        self._op = None #armazena o operador
        self.display.clear() #limpa display
        self.equation = self._equation_inicial_value #reinicia o valor do texto
        self.display.setFocus()#volta o foco para o qlabel
    
    @Slot()
    def _operator_clicked(self, button_text):
        
        display_text = self.display.text() #armazena o valor do display
        self.display.clear() #limpa display
        #verifica se ha um numero valido apos pressionar o operador
        if not is_valid_number(display_text) and self._left is None:
            self._show_error('Valor em branco! Digite um valor e tente novamente.')
            return
        if self._left is None:
            self._left = float(display_text)

        self._op = button_text #armazena operador

        self.equation = f'{self._left} {self._op} ??' #mudar o texto do label
        self.display.setFocus()#volta o foco para o qlabel

    @Slot()
    def _eq(self):
        display_text = self.display.text() #armazena o valor do display
        if not is_valid_number(display_text) or self._left is None or self._op is None:
            self._show_error('Nao há numero para presseguir com o calculo.')
            return
        self._right = float(display_text)
        self.equation = f'{self._left} {self._op} {self._right}' #mudar o texto do label
        try:
            if '^' in self.equation and isinstance(self._left,float):
                result = math.pow(self._left, self._right)
                # eval(self.equation.replace('^','**'))
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._show_error('Nao é possivel fazer divisao por zero.')
            self._clear()
            return
        except OverflowError:
            self._show_error('Numero muito grande.')
            self._clear()
            return

        self.info.setText( f'{self._left} {self._op} {self._right} = {result}')
        self.display.setText(str(result))
        self._left = result
        self._right, self._op = None, None
        self.display.setFocus()
        

    @Slot()
    def _invert_number(self):
        dislpay_text = self.display.text()
        if is_empty(dislpay_text):
            return
        if not is_num_or_dot(dislpay_text):
            return
       
        dislpay_text = float(dislpay_text)
        dislpay_text *= -1

        if dislpay_text.is_integer():
            dislpay_text = int(dislpay_text)

        self.display.setText(str(dislpay_text))
        self.display.setFocus()



    def _show_error(self, text):
        msgbox = self.window.make_msg_box()
        msgbox.setText(text)
        msgbox.setIcon(msgbox.Icon.Warning)
        #muda o botao padrao da caixa e menssagem
        msgbox.setStandardButtons(
            msgbox.StandardButton.Abort | msgbox.StandardButton.Ok #add segundo botao
        )
        msgbox.button(msgbox.StandardButton.Abort).setText('Sair')
        msgbox.exec() # é possivel ser qual botao foi clicado armazenando a saida da func exec em uma variavel
        self.display.setFocus()#volta o foco para o qlabel

    def _show_info(self, text):
        msgbox = self.window.make_msg_box()
        msgbox.setText(text)
        msgbox.setIcon(msgbox.Icon.Information)
        #muda o botao padrao da caixa e menssagem
        msgbox.setStandardButtons(
            msgbox.StandardButton.Abort | msgbox.StandardButton.Ok #add segundo botao
        )
        msgbox.button(msgbox.StandardButton.Abort).setText('Sair')
        msgbox.exec() 
        self.display.setFocus()#volta o foco para o qlabel


if __name__ == '__main__':
    from main import main
    main()