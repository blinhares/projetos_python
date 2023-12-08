"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def exercicio(lista_de_inteiros):
    # criar um dicionario, cujas chaves sao os valores da 
    # lista e os valores correspondentes sao o numero de ocorrencias
    print('-' * 20)
    print(lista_de_inteiros)
    dict_freq = {}
    for item in lista_de_inteiros:
        key_dict_freq = dict_freq.keys()
        if item in key_dict_freq:
            dict_freq[item] = dict_freq[item] + 1
        else:
            dict_freq[item] =  1
    
    #mostrar os valores duplicados...
    for valor in dict_freq:
        if dict_freq[valor] > 1:
            print(f'Valor {valor} duplicado.')

    # pegar valor cuja a ocorrencia acontece primeiro
    dict_ord_ocorr = {'Numero':None,'posi':len(lista_de_inteiros)}
    for valor in dict_freq:
        if dict_freq[valor]>1:
            prim_ocorrencia_valor = lista_de_inteiros.index(valor)
            seg_ocorrencia_valor = lista_de_inteiros.index(valor, prim_ocorrencia_valor+1)
            if seg_ocorrencia_valor < dict_ord_ocorr['posi']:
                dict_ord_ocorr['Numero'] = valor
                dict_ord_ocorr['posi'] = seg_ocorrencia_valor
    if dict_ord_ocorr['Numero'] != None:
        print(f'Retorna {dict_ord_ocorr['Numero']} ')
    else:
        print('-1')
    print('-' * 20)

def resolu2(lista_de_inteiros):
    primeira_recorrencia = -1
    n_poll = set()
    for num in lista_de_inteiros:
        if num in n_poll:
            primeira_recorrencia = num
            break
        n_poll.add(num)
    print(lista_de_inteiros, primeira_recorrencia)

for lista_de_inteiros in lista_de_listas_de_inteiros:
    # exercicio(lista_de_inteiros=lista_de_inteiros) 
    resolu2(lista_de_inteiros=lista_de_inteiros)