import os
from random import randint
import time
"""
o jogo é uma simulacao aleatoria simplismente obedecendo os movimentos da peças.

Por implementar:
Logica na qual o jogo termina em caso do Rei ser capturado
No caso do rei adversario estar dentro dos movimentos possiveis, capitura-lo
No caso do rei em CHeck, a jogada do jogador oposto deve ser com o rei para fugir

"""
class Tabuleiro():
    def __init__(self) -> None:
        self._rows = [1,2,3,4,5,6,7,8]
        self._columns= ['a','b','c','d','e','f','g','h']
        self.field = {}
        self._empty_slot = '[ ]'
        self.create_field()

        self._dict_pecas_brancas = {'Pw':['a2','b2','c2','d2','e2','f2','g2','h2'],
                           'Hw':['b1','g1'],
                           'Tw':['a1','h1'],
                           'Bw':['c1','f1'],
                           'Kw':['d1'],
                           'Qw':['e1']}
        self.put_all_pices(self._dict_pecas_brancas)                 
        self._dict_pecas_pretas = {'Pb':['a7','b7','c7','d7','e7','f7','g7','h7'],
                           'Hb':['b8','g8'],
                           'Tb':['a8','h8'],
                           'Bb':['c8','f8'],
                           'Kb':['e8'],
                           'Qb':['d8']}
        self.put_all_pices(self._dict_pecas_pretas)                 
        
        

    def create_field(self):
        for row in self._rows:
            #CONVERTER EM UM DICT COMPREETION
            for column in self._columns:
                key = column + str(row)
                self.field[key] = self._empty_slot
    
    def show_field(self,list_to_highlight:list = []):
        """
        Mostrar campo de batalha.
        list = [] - Argumento para destacar as celulas indicadas
        """
        # os.system('cls')
        list = list_to_highlight
        #imprime na tela as colunas
        print_columns = lambda :[print(f'{column :^4}', end='') for column in self._columns ]
        print_columns()
        print()

        num_columns = len(self._columns)
        cont = 0
        cont2 = 0 #conta quantas linhas
        
        for key in self.field.keys():
            cont += 1
            if key in list:
                print(f'\033[0;30;42m{self.field[key] :^4}\033[m', end='')
            else:
                print(f'{self.field[key] :^4}', end='')
            if not cont % num_columns:
                cont = 0
                cont2 += 1
                print(cont2)
        print_columns()
        print()

    def is_empty(self,position:str):
        if self.field[position] == self._empty_slot:
            return True
        return False

       # remover peca
    def get_out(self,place:str):
        self.field[place] = self._empty_slot

    #mover peca
    def move(self, start:str, end:str, verbose=False):
        possibles_moviments = self.possible_moviments(start)
        if end in possibles_moviments:
            content = self.field[start] #pega conteudo
            self.field[end] = f'{content :^4}'
            self.get_out(start)
            if verbose:
                print(f'Movimento de {start} -> {end} realizado...')
        else:
            if verbose:
                print('Movimento Impossivel!')

    def put_all_pices(self,incial_pos:dict):
        for piece in incial_pos.keys():
            for pos in incial_pos[piece]:
                 self.field[pos] = piece

    def possible_moviments(self,position:str):
        possibles_moviments = []
        
        #pegar a peca da posicao
        piece = self.field[position].strip()
        colum, row = self.convert_pos_to_cord(position)
        #movimento do piao
        if 'P' in piece:
            #movimentos 1 em direcao ao adversario + 1 em cada diagonal, se ouver pecas para comer
            #pecando cordenadas
            
            if 'w' in piece:
                colum2, rown2 = colum, (row+1)
                #possibilita o movimento pra frente, se estiver livre
                if self.is_in(colum2, rown2) and self.is_empty(pos:=(self.convert_cord_to_pos(colum2, rown2))):
                    possibles_moviments.append(pos)
                colum2 = (colum-1)
                if self.is_in(colum2, rown2): #garantir que os numeros estejam dentro do tabuleiro
                    if not 'w' in self.field[pos:=(self.convert_cord_to_pos(colum2,rown2))] and not self.is_empty(pos):
                            possibles_moviments.append(pos)
                
                colum2= (colum+1)  
                if self.is_in(colum2, rown2): #garantir que os numeros estejam dentro do tabuleiro
                    if not 'w' in self.field[pos:=(self.convert_cord_to_pos(colum2,rown2))] and not self.is_empty(pos):
                            possibles_moviments.append(pos)
                #possibilita mover duas casas no inicio do jogo
                
                if row == 2 and self.is_empty(pos:=(self.convert_cord_to_pos(colum,(row+2)))) and self.is_empty(pos:=(self.convert_cord_to_pos(colum,(row+1)))):
                    possibles_moviments.append(self.convert_cord_to_pos(colum,(row+2)))
           
            else:

                colum2, rown2 = colum, (row-1)
                #possibilita o movimento pra frente, se estiver livre
                
                if self.is_in(colum2, rown2) and self.is_empty(pos:=(self.convert_cord_to_pos(colum2, rown2))):
                    possibles_moviments.append(pos)
                colum2 = (colum-1)
                if self.is_in(colum2, rown2): #garantir que os numeros estejam dentro do tabuleiro
                    if not 'b' in self.field[pos:=(self.convert_cord_to_pos(colum2,rown2))] and not self.is_empty(pos):
                            possibles_moviments.append(pos)
                colum2= (colum+1)  
                if self.is_in(colum2, rown2): #garantir que os numeros estejam dentro do tabuleiro
                    if not 'b' in self.field[pos:=(self.convert_cord_to_pos(colum2,rown2))] and not self.is_empty(pos):
                            possibles_moviments.append(pos)
                #possibilita mover duas casas no inicio do jogo
                
                if row == 7 and self.is_empty(pos:=(self.convert_cord_to_pos(colum,(row-2)))) and self.is_empty(pos:=(self.convert_cord_to_pos(colum,(row-1)))):
                    possibles_moviments.append(self.convert_cord_to_pos(colum,(row-2)))
           
            
        #movimento do rei
        if 'K' in piece:
            colum2, rown2 = colum, row
            for tup in [(1,1),(1,-1),(-1,1),(-1,-1),
                        (1,0),(-1,0),(0,-1),(0,1)]:
                colum2 += tup[0]
                rown2 += tup[1]
        
                if self.is_in(colum2, rown2) and piece[-1:] not in self.field[(pos := self.convert_cord_to_pos(colum2, rown2))]:
                    possibles_moviments.append(pos)
                    colum2, rown2 = colum, row
                else:
                    colum2, rown2 = colum, row  
                
        #movimento do bispo
        if 'B' in piece:
            piece = piece[-1]
            colum2, rown2 = colum, row
            for tup in [(1,-1),(-1,1),(1,1),(-1,-1)]:
                while(self.is_in(colum2, rown2)):
                    colum2 += tup[0]
                    rown2 += tup[1]
                    if self.is_in(colum2, rown2) and piece not in self.field[(pos := self.convert_cord_to_pos(colum2, rown2))]:
                        possibles_moviments.append(pos)
                        if not self.is_empty(pos):
                            colum2, rown2 = colum, row
                            break
                    else:
                        colum2, rown2 = colum, row
                        break
            
        if 'T' in piece:
            colum2, rown2 = colum, row
            piece = piece[-1]
            for tup in [(1,0),(-1,0),(0,1),(0,-1)]:

                while(self.is_in(colum2, rown2)):
                    colum2 += tup[0]
                    rown2 += tup[1]
                    if self.is_in(colum2, rown2) and piece not in self.field[(pos := self.convert_cord_to_pos(colum2, rown2))]:
                        possibles_moviments.append(pos)
                        if not self.is_empty(pos):
                            colum2, rown2 = colum, row
                            break
                    else:
                        colum2, rown2 = colum, row
                        break

        if 'Q' in piece:
            colum2, rown2 = colum, row
            piece = piece[-1]

            for tup in [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1)]:
                while(self.is_in(colum2, rown2)):
                    colum2 += tup[0]
                    rown2 += tup[1]
                    if self.is_in(colum2, rown2) and piece not in self.field[(pos := self.convert_cord_to_pos(colum2, rown2))]:
                        possibles_moviments.append(pos)
                        if not self.is_empty(pos):
                            colum2, rown2 = colum, row
                            break
                    else:
                        colum2, rown2 = colum, row
                        break
        
        if 'H' in piece:
            colum2, rown2 = colum, row
            piece = piece[-1]
            for tup in [(2,1),(2,-1),(-2,1),(-2,-1),
                        (1,2),(-1,2),(1,-2),(-1,-2)]:
                colum2 += tup[0]
                rown2 += tup[1]
    
                if self.is_in(colum2, rown2) :
                    pos = self.convert_cord_to_pos(colum2, rown2)
                    if piece not in self.field[pos]:        
                        possibles_moviments.append(pos)
                    colum2, rown2 = colum, row
                else:
                    colum2, rown2 = colum, row
               
        
        # possibles_moviments.append(position)
        # self.show_field(possibles_moviments)
        return possibles_moviments


    def convert_pos_to_cord(self,pos:str):
        cord_column =  self._columns.index(pos[0]) + 1
        cord_row = int(pos[1])
        return cord_column, cord_row
    
    def convert_cord_to_pos(self,cord_column:int, cord_row:int):
        pos = str(self._columns[cord_column-1]) + str(cord_row)
        return pos
    
    def is_in(self,colum:int, row:int):
        """
        Verifica se as cordenadas estao dentro do tabuleiro
        """
        return (colum <= len(self._columns) and colum > 0 and row <= len(self._rows) and row > 0)


    def get_freepieces(self,is_white:bool= True):
        """
        Pega as pecas livres de uma cor ou de outra
        """
        list_of_pieces = []
        for piece in self.field.keys():
            content = self.field[piece]
            possible_moviments = self.possible_moviments(piece)
            if len(possible_moviments) > 0:
                if is_white :
                    if 'w' in content:
                        list_of_pieces.append(piece)
                elif 'b' in content:
                    list_of_pieces.append(piece)
                    
        return list_of_pieces

    def cont_pieces(self,is_white:bool= True):
        n_pieces = 0
        for piece in self.field.keys():
            content = self.field[piece]
            n_pieces = n_pieces + 1 if is_white and 'w' in content else n_pieces
            n_pieces = n_pieces + 1 if not is_white and 'b' in content else n_pieces
        return n_pieces
                    
    def where_is_king(self,is_white:bool= True):
        '''
        Retorna em que local do tabuleiro esta o rei
        '''
        king = 'Kw' if is_white else 'Kb'
        
        for casa in self.field.keys():
            if king in self.field[casa]:
                return str(casa).strip()


    def is_the_king_safe(self,is_white:bool= True):
        '''
        Verifica se o rei em questao esta dentro dos movimentos possiveis do adversario.
        Retorna, se o rei esta a salvo(true) ou nao (false) e os possiveis movimentos para tiralo do sufoco
        '''
        king = 'Kw' if is_white else 'Kb'
        
        king_location = self.where_is_king(is_white=is_white)
        king_danger = False
        
        #pega lista das pecas adversarias
        pecas_adversarias = self.get_freepieces(is_white=(not is_white))
        #armazena em variavel todas os possiveis movimentos dessas pecas 

        ### problema: o piao nao come pecas pela frente, porem a funcao inclui esta casa

        alcance_adversario = set()
        for peca in pecas_adversarias:
            [alcance_adversario.add(str(casa).strip()) for casa in self.possible_moviments(peca)]
            
        #MOVIMENTOS POSSIVEIS DO REI DESCONSIDERA AMECAS         
        king_option_scape = set(self.possible_moviments(king_location))
        

        #TESTAR CADA POSICAO DO REI 
        for pos in king_option_scape:
            #mover o rei
            self.move(king_location, pos)
            #ADICIONA AO ALCANCE DO ADVERSARIO AS POSICOES DE PERIGO
            for peca in pecas_adversarias:
                [alcance_adversario.add(str(casa).strip()) for casa in self.possible_moviments(peca)]
            #mover o kei para pos inicial
            self.move(pos, king_location)
            

        # retira das opcoes de movimento do rei Do alcance das adversarias.
        # RETORNA O QUE HA ME_KING OPTIN E NAO TEM EM ALCANCE ADVERSARIO
        king_option_scape = king_option_scape - alcance_adversario

        
        if king_location in alcance_adversario:
            king_danger = True
            print('*' *40)
            print(f'O rei {king} esta em {king_location} perigo!!!')
            print(f'Poder correr para {king_option_scape}')
            print('*' *40)
            self.show_field(list(alcance_adversario))
            input()

        

        return king_danger


if __name__=="__main__":
    
    os.system('cls')
    tabuleiro = Tabuleiro()
    is_white = True
    cont = 0

    while True:
        

        cont += 1
        #escolher peca a mover
        pecas_livres = tabuleiro.get_freepieces(is_white=is_white)
        # se as pecas nao possuem mais moviemntos o jogo para
        if len(pecas_livres)== 0:
            if is_white:
                print('Pecas Negras Venceram!')
            else:
                print('Pecas Brancas Venceram!')
            tabuleiro.show_field()
            break
        peca_escolhida = pecas_livres[randint(0, len(pecas_livres)-1)]
        #pegar posicoes possivel de movimento da peca escolhida
        mov_possi = tabuleiro.possible_moviments(peca_escolhida)
        desti_final = mov_possi[randint(0, len(mov_possi)-1)]
        # os.system('cls')
        
        print(f'Mov. N {cont} - {tabuleiro.field[peca_escolhida]} : {peca_escolhida} -> {desti_final} . N Pieces : {tabuleiro.cont_pieces(is_white)} ')
        tabuleiro.move(peca_escolhida, desti_final)

        tabuleiro.is_the_king_safe(True)
        tabuleiro.is_the_king_safe(False)
        


        tabuleiro.show_field()
        is_white = not is_white #inverte o bolean
        # time.sleep(.5)



        




