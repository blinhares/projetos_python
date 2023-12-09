"""
Definindo estruturas
tarefa {'Titulo':'', 'Status':''}
status = {1:'a fazer',2:'andamento',3:'concluido'}
lista_tarefas [tarefa]

# Funções:
[ok] - opcao : menu interativo para validacaod e opcoes
[ok] - visualizar : Ter visibilidade das tarafas separadas por status
inserir tarefa : adicionar uma tarefa
editar tarefa : Editar status da tarefa;
                Editar titulo da mesma
"""
lista_status = {'1':'a fazer','2':'andamento','3':'concluido'}

lista_tarefas = [{'Titulo':'Passear', 'Status':'a fazer'},
                 {'Titulo':'Estudar', 'Status':'andamento'},
                 {'Titulo':'Comer', 'Status':'concluido'},
                 {'Titulo':'rezar', 'Status':'concluido'}
]

def mostra_tarefas_by_status(lista_tarefas:list, lista_status:dict):
    for key in lista_status:
        print(f'{lista_status[key] :-^50} \n')
        [print(f'- {task['Titulo']} ') for task in lista_tarefas if task['Status'] in lista_status[key]]
        print(f'{ '-' * 50 :^}')

def mostra_tarefas(lista_tarefas:list):
    for i in range(0,len(lista_tarefas)):
        print(f'{i+1} - {lista_tarefas[i]['Titulo']} - Status : {lista_tarefas[i]['Status']}')
    print()

def opcao(texto:str, options:list):
    options = [str(op) for op in options] #converte as opcoes para string
    print(texto)
    option = input('Escolha uma opção: ')
    while option not in options:
        print(texto)
        option = input('Opção digitada é invalida! Digite novamente: ')
    return option

def add_task(lista_tarefas:list ,lista_status:dict):
    title = input('Digite um titulo para a tarefas:')
    texto = 'Digite uma das opções abaixo \n' + str(lista_status)
    options = list(lista_status.keys())
    status = opcao(texto=texto,options=options)
    status = lista_status[status]
    lista_tarefas.append({'Titulo':title, 'Status':status})

def rm_task(lista_tarefas:list):
    mostra_tarefas(lista_tarefas)
    texto = 'Digite um numero a ser excluido. (digite 0 para cancelar)'
    options = [str(i+1) for i in range(0, len(lista_tarefas))]
    options.append('0')
    print(options)
    option = opcao(texto,options)
    if option != 0:
        lista_tarefas.pop(int(option)-1)

def rm_finish_task(lista_tarefas:list):
    list_conclu = []
    for i in range(0, len(lista_tarefas)):
        if lista_tarefas[i]['Status'] in 'concluido':
            list_conclu.append(i)
    list_conclu.sort(reverse=True)
    for index in list_conclu:
        lista_tarefas.pop(index)
    
def status_change():
    print('falta implementar')  


menu = '''
[1] - Adicionar Tarefa
[2] - Mudar Status da Tarefa
[3] - Remover Tarefa
[4] - Remover todas as Concluidas
[5] - Exibir tarefa por Status
[0] - SAIR
'''  
while True:
    mostra_tarefas(lista_tarefas)
    option = opcao(menu,[1,2,3,4,5,0])
    if option == '1':
        add_task(lista_tarefas ,lista_status)
    if option == '2':
        status_change()
    if option == '3':
        rm_task(lista_tarefas)
    if option == '4':
        rm_finish_task(lista_tarefas)
    if option == '5':
        mostra_tarefas_by_status(lista_tarefas, lista_status)
    if option == '0':
        break
# mostra_tarefas(lista_tarefas=lista_tarefas)
