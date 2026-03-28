import json
from os import system


# --------- #
#  FUNÇÕES  #
# --------- #
def título(cabeçalho, descrição, conteúdo=[]):
    while True:
        system('cls')
        print(f'\u001b[91m#  {cabeçalho.upper()}  #')
        for line in descrição.splitlines():
            print(f"  {line.capitalize()}")
        print()
        if len(conteúdo) > 0:
            for i, opção in enumerate(conteúdo, start=1):
                print(f'  {i} - {opção}')
            try:
                input_usuário = int(input(">> "))
                if 1 <= input_usuário <= len(conteúdo):
                    print()
                    return input_usuário
                else:
                    raise ValueError
            except ValueError:
                input('\nDigite uma entrada válida.\nPressione ENTER para continuar.')
        else:
            break

def validar_nome(entrada):
    while True:
        entrada_usuário = input(entrada)
        if entrada_usuário == '':
            input('\nDigite uma entrada válida.\nPressione ENTER para continuar.')
            print("\033[A\033[K"*4, end="\r")
        else:
            return entrada_usuário

def validar_novo(entrada, atual):
    entrada_usuário = input(entrada)
    if entrada_usuário == '':
        return atual
    else:
        return entrada_usuário
    
def ler_arquivo():
    with open('data.json', 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def salvar_arquivo(dados):
    with open('data.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)