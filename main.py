from Repository.repository import Repository
from Service.service import Service
from UI.console import UI
from Teste.test import TestService

if __name__ == '__main__':
    tester = TestService()
    file_name = "/Users/vladsoporan/Desktop/FMI/An1/sem_2/structuri_date/lab/de_la_mine/lab_1_sd__me/cars.txt"
    repo = Repository(file_name)
    service = Service(repo)
    ui = UI(service)

    ui.run_meniu()
