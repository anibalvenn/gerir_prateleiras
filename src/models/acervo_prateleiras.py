class __RegistroPrateleiras:
    def __init__(self) -> None:
        self.prateleiras = []
        self.books = []

    def count_prateleiras(self) -> int:
        return len(self.prateleiras)
    
    def count_books(self) -> int:
        return len(self.books)

    def registry_prateleira(self, prateleira: any) -> None:
        self.prateleiras.append(prateleira)

    def registry_book(self, book: any) -> None:
        self.books.append(book)
    
    def get_book(self, book_name: str) -> any:
        for registry in self.books:
            if registry.name == book_name:
                return registry

        return None

    def get_books_by_prateleira_id(self, prateleira_id: str):
        books = []
        for registry in self.books:
            if registry.prateleira_id == prateleira_id:
                books.append(registry)
        
        return books


registro_prateleiras = __RegistroPrateleiras()
