def introduction_page():
    message = '''
        Sistema de Cadastro de Livros

        * Cadastrar Prateleira - 1
        * Cadastrar Livro - 2
        * Buscar Prateleira - 3       
        * Sair - 4
    '''

    print(message)
    command = input('Comando: ')

    return command
