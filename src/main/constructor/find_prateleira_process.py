from src.views.find_prateleira_view import FindPrateleiraViews
from src.controllers.find_prateleira_controller import FindPrateleiraController

def find_prateleira_process() -> None:
    find_prateleira_views = FindPrateleiraViews()
    find_prateleira_controller = FindPrateleiraController()

    book_informations = find_prateleira_views.find_prateleira_view()
    response = find_prateleira_controller.find(book_informations)

    if response["success"]: find_prateleira_views.find_prateleira_success(response["registries"])
    else: find_prateleira_views.find_prateleira_fail(response["error"])

