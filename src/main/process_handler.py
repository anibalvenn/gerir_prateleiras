from .constructor.introduction_process import introduction_process
from .constructor.registry_prateleira_process import registry_prateleira_process
from .constructor.registry_book_process import registry_book_process
from .constructor.find_prateleira_process import find_prateleira_process


def start() -> None:
    while True:
        command = introduction_process()

        if command == '1': registry_prateleira_process()
        elif command == '2': registry_book_process()
        elif command == '3': find_prateleira_process()
        elif command == '4': exit()
        else: print('\nComando nao encontrado, tente novamente!\n\n')
