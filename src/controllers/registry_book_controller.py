from typing import Dict
from src.models.acervo_prateleiras import registro_prateleiras
from src.models.entities.book import Book

class RegistryBookController:

    def registry(self, book_informations: Dict):
        try:
            new_book_id = self.__get_new_book_id()

            new_book = Book(
                new_book_id,
                book_informations["name"],
                book_informations["prateleira_id"]
            )
            registro_prateleiras.registry_book(new_book)
            
            return { "success": True, "book_registry": new_book }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __get_prateleira(self, prateleira_id: str) -> any:
        prateleira_registry = registro_prateleiras.get_books_by_prateleira_id(prateleira_id)
        if prateleira_registry is None: raise Exception('Falha ao cadastrar. Turma nao encontrada!')

        return prateleira_registry

    def __get_new_book_id(self) -> str:
        books_count = registro_prateleiras.count_books()
        new_book_id = str(books_count + 1)
        return new_book_id
