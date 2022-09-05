from src.models.acervo_prateleiras import registro_prateleiras
from src.models.entities.prateleira import Prateleira

class RegistryPrateleiraController:

    def registry(self):
        try:
            prateleira_count = registro_prateleiras.count_prateleiras()
            new_prateleira_id = str(prateleira_count + 1)

            new_prateleira = Prateleira(new_prateleira_id, [])
            registro_prateleiras.registry_prateleira(new_prateleira)

            return new_prateleira
        except:
            return None