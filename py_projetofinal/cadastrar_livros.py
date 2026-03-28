from funções import título, validar_nome, ler_arquivo, salvar_arquivo


# ----------------- #
#  CADASTRAR LIVRO  #
# ----------------- #
def cadastrar_livro():
    livros = ler_arquivo()
    while True:
        título('CADASTRO DE LIVROS', 'Digite corretamente para cadastrar um livro.')
        try:
            nome = validar_nome('  Nome: ').strip().title()
            autor = validar_nome('  Autor: ').strip().title()
            genero = validar_nome('  Gênero: ').strip().title()
            quantidade = int(input('  Quantidade: '))
            link = input('  Link de acesso: ').strip()

            livro = {
                'Nome': nome,
                'Autor': autor,
                'Gênero': genero,
                'Quantidade': quantidade,
                'Link': link
            }
            break
        except ValueError:
            input('\nDigite uma entrada válida.\nPressione ENTER para continuar.')
    livros.append(livro)
    salvar_arquivo(livros)

def continuar():
    while True:       
        match input('\nVocê cadastrou um livro! Deseja continuar cadastrando? (s/n) ').strip().lower():
            case 's' | 'ss' | 'sim':
                return cadastrar()
            case 'n' | 'nn' | 'nao' | 'não':
                break
            case _:
                input('\nDigite uma entrada válida.\nPressione ENTER para continuar.')
                print("\033[A\033[K"*5, end="\r")

def cadastrar():
    cadastrar_livro()
    continuar()