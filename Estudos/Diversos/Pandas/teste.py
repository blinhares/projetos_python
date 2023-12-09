import pandas as pd
import numpy as np

dados= pd.DataFrame( {'Vendas_Cafe' : [18, 20, 23, 23, 23, 23, 24, 25, 26, 26, 26, 26, 27, 28, 28,
29, 29, 30, 30, 31, 31, 33, 34, 35, 38, 39, 41, 44, 44, 46],
'Preco_Cafe' : [4.77, 4.67, 4.75, 4.74, 4.63, 4.56, 4.59, 4.75, 4.75, 4.49,
4.41, 4.32, 4.68, 4.66, 4.42, 4.71, 4.66, 4.46, 4.36, 4.47, 4.43,
4.4, 4.61, 4.09, 3.73, 3.89, 4.35, 3.84, 3.81, 3.79],
'Promocao' : ["Nao", "Nao", "Nao", "Nao", "Nao", "Nao", "Nao", "Nao", "Sim",
"Nao", "Sim", "Nao", "Nao", "Sim", "Sim", "Nao", "Sim", "Sim",
"Sim", "Nao", "Nao", "Sim", "Sim", "Sim", "Nao", "Sim", "Sim","Sim", "Sim", "Sim"],
'Preco_Leite' : [4.74, 4.81, 4.36, 4.29, 4.17, 4.66, 4.73, 4.11, 4.21, 4.25,
4.62, 4.53, 4.44, 4.19, 4.37, 4.29, 4.57, 4.21, 4.77, 4, 4.31,
4.34, 4.05, 4.73, 4.07, 4.75, 4, 4.15, 4.34, 4.15]
})
print(f'Descrevendo as estatisticas descritivas dos dados:\n {dados.describe()}')

print(dados['Promocao'].str.split('i'))




