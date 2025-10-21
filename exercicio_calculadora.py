'''
​1- Criar uma calculadora utilizando funções onde o usuário terá que inserir dois valores e o operador aritmético.​

'''

def calculadora():
    
    while True:
        try:
            num1 = int(input('Digite o 1º número: '))
            operador = input("Digite o operador (+, -, *, /): ")
            num2 = int(input('Digite o 2º número: '))
        except ValueError:
            print('Entre com algum valor interior e/ou use somente os operadores apropriados.')
   

        # Realiza o cálculo baseado no operador
        if operador == '+':
            resultado = num1 + num2
            return resultado
        elif operador == '-':
            resultado = num1 - num2
            return resultado
        elif operador == '*':
            resultado = num1 * num2
            return resultado
        elif operador == '/':

        # Tratamento para evitar divisão por zero
            if num2 == 0:
                print("Erro: Não é possível dividir por zero.")
            else:
                resultado = num1 / num2
                return resultado
            else:
                print('Operação não reconhecida.')

print('O resultado é:')
print(calculadora())
