import os


#  FUNÇÕES MATEMÁTICAS  #
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        resultado = '?? (dividido por 0)'
    return resultado

def resto_divisão(a, b):
    try:
        resultado = a % b
    except ZeroDivisionError:
        resultado = '?? (dividido por 0)'
    return resultado

def ao_quadradado(a):
    return a ** 2

#  FUNÇÕES  #
def titulo(titulo):
    os.system('clear')
    print(f'#  {titulo}  #\n')

def validar_numero(numero):
    try:
        uinput = float(numero)
        return uinput
    except ValueError:
        return_main()

def return_main():
    print('\nDigite um número/operador válido.')
    input('Pressione ENTER para continuar...')
    return main()

#  MAIN  #
def main():
    while True:
        titulo('CALC.py')
        x = validar_numero(input('Digite o primeiro número: '))
        y = validar_numero(input('Digite o segundo número:  '))
        op = input('Digite o operador (+, -, *, /, %, **):  ')
        print()

        match op:
            case '+':
                print(f'{x} + {y} = {somar(x, y)}')
            case '-':
                print(f'{x} - {y} = {subtrair(x, y)}')
            case '*':
                print(f'{x} * {y} = {multiplicar(x, y)}')
            case '/':
                print(f'{x} / {y} = {dividir(x, y)}')
            case '%':
                print(f'{x} % {y} = {resto_divisão(x, y)}')
            case '**' | '^':
                print(f'{x} ** 2 = {ao_quadradado(x)}')
                print(f'{y} ** 2 = {ao_quadradado(y)}')
            case _:
                return_main()
            
        while True:
            continuar = input('\nVocê deseja continuar realizando operações? (s/n) ')
            match continuar.strip().lower():
                case 's' | 'sim':
                    break
                case 'n' | 'nao' | 'não':
                    exit()
                case _:
                    print('Digite "s" ou "n".')

main()