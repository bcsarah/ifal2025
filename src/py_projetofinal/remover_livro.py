from funções import título, ler_arquivo, salvar_arquivo


# --------------- #
#  REMOVER LIVRO  #
# --------------- #
def remover():
    while True:
        livros = ler_arquivo()
        opções = [f'[{livro['Quantidade']}] {livro['Nome']} ~ {livro['Autor']}  ({livro['Gênero']})' for livro in livros]
        opções.append('Voltar')

        remover = título('REMOÇÃO DE LIVRO',
                         'Remova o livro que desejar, com base no seu index.',
                         opções)
        if remover == len(opções):
            break
        removido = livros.pop(remover - 1)
        print(f'Livro "{removido["Nome"]}" removido com sucesso!')
        salvar_arquivo(livros)

        match input('Continuar removendo? (s/n) '):
            case 's' | 'sim':
                pass
            case 'n' | 'nao' | 'não':
                break