# monitora_funcionarios_prefeitura_caucaia
Realiza a comparação entre dois meses quaisquer das listas de funcionários da prefeitura. Sendo possível constatar as contratações e desligamentos do período. 
O scrypt se utiliza de 3 bibliotecas não nativas:
requests
from openpyxl import load_workbook
from xls2xlsx import XLS2XLSX
Todas disponiveis via "Pip"
Os dados sao obtidos por meio da API disponibilizada por meio do requests. O arquivo tem formato original do .XLS que não é lido pelo OPENPYXL (manipulador de arquivos excel) e por isso teve de ser convertido para .XLSX atraves da biblioteca xls2xlsx.
O Restante do código é logica simples de programação...
