print('Tabuada')
print('='*30)

numero = int(input('Digite um númeto inteiro: '))

def tabuada ():

    multiplicador = 0

    while True:
        if multiplicador < 10:
            multiplicador += 1
            print(f'{multiplicador} * {numero} = {multiplicador * numero}')
        else:
            break

tabuada()

