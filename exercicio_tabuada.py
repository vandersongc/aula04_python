'''
2- Crie um programa em Python que:​
Peça ao usuário um número inteiro.​
Gere e exiba na tela a tabuada desse número de 1 a 10.​
Utilize funções para deixar o código organizado.

'''

print('='*30)
numero = int(input('Digite um númeto inteiro: '))
print('='*30)

print('Tabuada')

def tabuada ():

    multiplicador = 0

    while True:
        if multiplicador < 10:
            multiplicador += 1
            print(f'{multiplicador} * {numero} = {multiplicador * numero}')
        else:
            break

tabuada()

