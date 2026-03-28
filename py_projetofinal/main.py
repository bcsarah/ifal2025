from funções import título
from ver_livro import ver
from cadastrar_livros import cadastrar
from editar_livros import editar
from remover_livro import remover


# ------ #
#  MAIN  #
# ------ #
def main():
    while True:
        match título('BIBLIOTECA', 'O que deseja fazer?', ['Ver livros', 'Cadastrar livros', 'Editar livros', 'Remover livros', 'Sair']):
            case 1:
                ver()
            case 2:
                cadastrar()
            case 3:
                editar()
            case 4:
                remover()
            case 5:
                break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass