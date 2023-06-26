# Calculadora com While


while True:
    numero_1 = input('digite um número: ')
    numero_2 = input('digite outro número: ')
    operador = input('digite o operador (+-/*): ')
    
    numeros_validos = None
    
    num_1_float = 0
    num_2_float = 0
           
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos!')
        continue
    
    if len(operador) > 1:
        print('Digite somente 1 operador.')
        continue
    
    if operador == '+':
        soma = num_1_float + num_2_float
        print(f'A soma deles é: {soma:.2f}')
    elif operador == '-':
        sub = num_1_float - num_2_float
        print(f'a subtração é: {sub:.2f}')
    elif operador == '/':
        div = num_1_float / num_2_float
        print(f'a divisão é: {div}')     
    elif operador == '*':
        mult = num_1_float * num_2_float
        print(f'a multiplicação é: {mult}')
    else:
        print('Erro!')
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue
    
    sair = input('deseja sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
    