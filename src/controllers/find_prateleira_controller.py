from typing import Dict
from src.models.acervo_prateleiras import registro_prateleiras

class FindPrateleiraController:

    def find(self, book_prateleira_id: str):
        try:
            books_registries = self.__search_books_registries_by_prateleira_id(book_prateleira_id)
            registries = self.__format_registries_info(books_registries)
            return { "success": True, "registries": registries }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __search_books_registries_by_prateleira_id(self, prateleira_id: str) -> any:
        books_registries = registro_prateleiras.get_books_by_prateleira_id(prateleira_id)
        if books_registries == []: raise Exception('Prateleira vazia')

        return books_registries

    def __format_registries_info(self, books_registries: any):
        
        prateleira_id = books_registries[0].prateleira_id

        registries = []
        for book in books_registries:
            registries.append({
                "id": book.id,
                "name": book.name,
            })
        
        return {
            "prateleira_id": prateleira_id,          
            "registries": registries
        }
