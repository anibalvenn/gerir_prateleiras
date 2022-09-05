import os


class RegistryPrateleiraViews:
    def registry_prateleira_page(self) -> str:
        self.__clear()

        print('Criação de Prateleira \n\n')
        id_prateleira = input('Determine o id da prateleira: ')

        return id_prateleira

    def registry_prateleira_success(self, new_prateleira: any) -> None:
        self.__clear()

        message = '''
            Prateleira cadastrada com sucesso!
            * Infos:
                Id da Prateleira: {}
                
        '''.format(new_prateleira.id)
        print(message)

    def registry_prateleira_fail(self) -> None:
        self.__clear()

        message = '''
            Ocorreu um erro ao cadastrar a Prateleira, confira os campos apresentados
        '''
        print(message)
    
    def __clear(self):
        os.system('cls||clear')