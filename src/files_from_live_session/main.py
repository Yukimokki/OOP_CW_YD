from src.files_from_live_session.api_from_live import HHVacanciesAPI

hh_api = HHVacanciesAPI()

vacancies = hh_api.get_vacancies('Python')
for vac in vacancies:
    print(vac['name'])