import json
from abc import ABC, abstractmethod
import os
from config import ROOT_DIR


class FileWork(ABC):

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass

    @abstractmethod
    def del_file(self):
        pass


class WorkWithJson(FileWork):

    def read_file(self):
        """
        читает файл с вакансиями

        """
        FILEPATH = os.path.join(ROOT_DIR, 'data', 'vacancies.json')
        with open(FILEPATH, "r", encoding="utf-8") as datafile:
            return json.load(datafile)


    def save_file(self, data):
        """
        сохраняет файл с вакансиями
        """
        FILEPATH = os.path.join(ROOT_DIR, 'data', 'vacancies.json')
        with open(FILEPATH, "w", encoding="utf-8") as datafile:
            json.dump(data, datafile,  ensure_ascii=False, indent=4)

    def del_file(self):
        """
        очищает файл с вакансиями
        :return:
        """
        FILEPATH = os.path.join(ROOT_DIR, 'data', 'vacancies.json')
        with open(FILEPATH, "w", encoding="utf-8") as datafile:
            pass

    @staticmethod
    def get_data(criterion, currency_choice):
        """
        Метод получения данных из файла по указанным критериям
        """
        criterion_vac = []
        empty_list = []
        FILEPATH = os.path.join(ROOT_DIR, 'data', 'vacancies.json')
        with open(FILEPATH, "r", encoding="utf8") as datafile:
            vacancies = json.load(datafile)
            for vac in vacancies:
                if criterion in vac.keys() and vac['salary'] != None:
                    if currency_choice == vac['salary']['currency']:
                        criterion_vac.append(vac)
                else:
                    empty_list.append(vac)
                    continue

            #print(len(criterion_vac),len(empty_list))
        return criterion_vac
        #datafile.write(criterion_vac)







# Vacancy = WorkWithJson()
# Vacancy.get_data('name', 'RUR')
# print(Vacancy)