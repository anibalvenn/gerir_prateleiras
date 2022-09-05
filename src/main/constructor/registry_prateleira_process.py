from src.views.registry_prateleira_view import RegistryPrateleiraViews
from src.controllers.registry_prateleira_controller import RegistryPrateleiraController

def registry_prateleira_process() -> None:
    registry_prateleira_view = RegistryPrateleiraViews()
    registry_prateleira_controller = RegistryPrateleiraController()

    new_prateleira = registry_prateleira_controller.registry()

    if new_prateleira is not None: registry_prateleira_view.registry_prateleira_success(new_prateleira)
    else: registry_prateleira_view.registry_prateleira_fail()

