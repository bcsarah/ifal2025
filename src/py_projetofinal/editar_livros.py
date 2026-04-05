from funções import título, validar_novo, ler_arquivo, salvar_arquivo


# -------------- #
#  EDITAR LIVRO  #
# -------------- #
def editar():
    while True:
        livros = ler_arquivo()
        opções = [f'[{livro['Quantidade']}] {livro['Nome']} ~ {livro['Autor']}  ({livro['Gênero']})' for livro in livros]
        opções.append('Voltar')

        editar = título('REMOÇÃO DE LIVRO',
                         'Remova o livro que desejar, com base no seu index.',
                         opções)
        if editar == len(opções):
            break
        else:
            while True:
                try:
                    livro = livros[editar - 1]
                    título(f'Editando "{livro["Nome"]}" ~ {livro["Autor"]}',
                        'Continue editando seu livro.\nDeixe em branco para não alterar certa instância.')

                    nome = validar_novo(f'  Novo nome ({livro["Nome"]}): ', livro["Nome"]).strip().title()
                    autor = validar_novo(f'  Novo autor ({livro["Autor"]}): ', livro["Autor"]).strip().title()
                    genero = validar_novo(f'  Novo gênero ({livro["Gênero"]}): ', livro["Gênero"]).strip().title()
                    quantidade = int(validar_novo(f'  Quantidade ({livro["Quantidade"]}): ', livro["Quantidade"]))
                    link = validar_novo('  Link de acesso: ', livro["Link"]).strip()

                    livros[editar - 1] = {
                        'Nome': nome,
                        'Autor': autor,
                        'Gênero': genero,
                        'Quantidade': quantidade,
                        'Link': link
                    }
                    salvar_arquivo(livros)
                    input('\nLivro editado com sucesso! Pressione\nPressione ENTER para continuar.')
                    return
                except ValueError:
                    input('\nDigite uma entrada válida.\nPressione ENTER para continuar.')