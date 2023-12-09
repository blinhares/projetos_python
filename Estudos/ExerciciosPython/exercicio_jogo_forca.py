"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os
palavra , letras_corretas , n_tentativas = 'abacate' , set() , 0

while True:
    letra_usuario = input('Digite uma letra: ').lower()
    n_tentativas += 1
    if letra_usuario in palavra:
        os.system('cls')
        letras_corretas.add(letra_usuario)
        print(f'A letra {letra_usuario} esta contida na palavra secreta...')
        for letra in palavra:
            print(letra, end='') if letra in letras_corretas else print(' _ ', end='')
        print()
    else:
        print('A letra n faz parte da palavra secreta. Tente Novamente...')
    if len(set(palavra)) == len(letras_corretas):
        print(f'Parabens vc encontrou a palavra secreta utilizando {n_tentativas} tentativas')
        break
