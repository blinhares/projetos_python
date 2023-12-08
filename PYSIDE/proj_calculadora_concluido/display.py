from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from PySide6.QtCore import Qt , Signal
from utilis import is_empty, is_num_or_dot

class Display(QLineEdit):
    eq_pressed = Signal() #criar sinal
    del_pressed = Signal() #criar sinal
    clear_pressed = Signal() #criar sinal
    input_pressed = Signal(str) #neste caso a que passar o argumento de 
    #signal uma vez que ele vai disparar um sinal com um dado str
    operator_pressed = Signal(str)

    def __init__(self, *args, **kwargs ):
        super().__init__( *args, **kwargs)
        self.configstyle()   

    def configstyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE*1.5)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])
        # essa list compreentioin gera os 4 dados nescessarios 
        # pa crias as margens
        self.setPlaceholderText('Digite algo...')
        # self.setReadOnly(True)
        

    def keyPressEvent(self, event: QKeyEvent) -> None: #monitora pressionar das teclas
        text = event.text().strip()#pega texto do evento e retira espacos
        key = event.key()
        KEYS = Qt.Key
        is_enter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        is_delet = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        is_esc = key in [KEYS.Key_Escape]

        if is_enter or text == '=': #emite signal caso a tecla enter seja pressionada
            self.eq_pressed.emit()
            return event.ignore()
        
        if is_delet: #emite signal caso a tecla enter seja pressionada
            self.del_pressed.emit()
            return event.ignore()
        
        if is_esc  or text.lower() == 'c': #emite signal caso a tecla enter seja pressionada
            self.clear_pressed.emit()
            return event.ignore()
        #
        if is_empty(text):
            return event.ignore()
        
        if is_num_or_dot(text):
            self.input_pressed.emit(text)
            return event.ignore()
        
        if text in '+-/*^':
            self.operator_pressed.emit(text)
            return event.ignore()


if __name__ == '__main__':
    from main import main
    main()
