from funções import título, ler_arquivo
from os import system


# ------------ #
#  VER LIVROS  #
# ------------ #
def ver():
    while True:
        livros = ler_arquivo()
        título('VISUALIZAÇÃO',
            'Modo de Visualização de Livros.\nQuantidade, Nome, Autor, Gênero')
        if len(livros) > 0:
            for i, livro in enumerate(livros, start=1):
                print(f'  {i} ~ [{livro['Quantidade']}] {livro['Nome']} ~ {livro['Autor']}  ({livro['Gênero']})')

            match input('\nVocê deseja ler algum livro? (s/n) '):
                case 's' | 'sim':
                    ler_livro()
                case 'n' | 'nao' | 'não':
                    break
        else:
            input('Você não tem livros cadastrados. Pressione ENTER para continuar.')
            break
        
def ler_livro():
    livros = ler_arquivo()
    while True:
        try:
            ler = int(input('Digite o número do livro (index) para leitura: '))
            if 1 <= ler <= len(livros):
                system(f'firefox {livros[ler - 1]["Link"]} >/dev/null 2>&1 &')
                input('\u001b[91mLivro aberto! Pressione ENTER para continuar.')
                break
            else:
                raise ValueError
        except ValueError:
            input('Número inválido. Pressione ENTER.')