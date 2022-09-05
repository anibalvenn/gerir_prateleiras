import os

class FindPrateleiraViews:
    def find_prateleira_view(self) -> str:
        self.__clear()

        print('Busca Livros da Prateleira \n\n')
        prateleira_id = input('Determine o id da prateleira para busca: ')

        return prateleira_id
    
    def find_prateleira_success(self, prateleira_registry: any) -> None:
        self.__clear()

        message = '''
            ID {} 
            * Infos:
        '''.format(
            prateleira_registry["prateleira_id"],
            
        )

        for registry in prateleira_registry["registries"]:
            message += '''\n
                Id do Livro: {}
                Nome do Livro: {}              
            '''.format(
                registry["id"],
                registry["name"]
            )

        print(message)
    
    def find_prateleira_fail(self, error: str) -> None:
        self.__clear()

        message = '''
            Ocorreu um erro ao buscar Prateleira.
            {}
        '''.format(error)
        print(message)

    def __clear(self):
        os.system('cls||clear')
