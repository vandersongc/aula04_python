def calculadora():
    """
    Função de calculadora simples que realiza operações básicas.
    """
 
    num1 = int(input('Digite o 1º número: '))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = int(input('Digite o 2º número: '))
   

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
