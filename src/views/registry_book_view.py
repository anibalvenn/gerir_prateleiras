import os
from typing import Dict


class RegistryBookViews:
    def registry_book_view(self) -> Dict:
        self.__clear()

        print('Criação de Cadastro de Livro \n\n')
        book_name = input('Determine o nome do livro: ')
        prateleira_id = input('Determine a prateleira do livro: ')

        return {
            "name": book_name,
            "prateleira_id": prateleira_id
        }
    
    def registry_book_success(self, new_book: any) -> None:
        self.__clear()

        message = '''
            Livro cadastrado com sucesso!
            * Infos:
                Id do Livro: {}
                Nome do livro: {}
                Id da Prateleira: {}
        '''.format(new_book.id, new_book.name, new_book.prateleira_id)
        print(message)

    def registry_book_fail(self, error: str) -> None:
        self.__clear()

        message = '''
            Ocorreu um erro ao cadastrar o livro.
            {}
        '''.format(error)
        print(message)

    def __clear(self):
        os.system('cls||clear')
