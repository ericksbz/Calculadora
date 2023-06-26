# Calculadora com While

numero1 = 0
numero2 = 0

while True:
    numero_1 = input('digite um número: ')
    numero_2 = input('digite outro número: ')
    operador = input('digite o operador (+-/*): ')
    
    numeros_validos = None
    
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
    
    
    
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue
    
    sair = input('deseja sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
    