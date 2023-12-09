from random import randint
#dois milhoes de numeros
contador = 2 * 1000 * 1000 * 1000
 
with  open('rand.txt', mode='x') as file:
   
    for i in range(contador):
        print(f'Numero da intera: {i}')
        value = randint(0,10)
        if value != 5:
            # print(value, end=' ')
            file.write(str(value))
        else:
            # print(value)
            file.write('\n')

file.close()