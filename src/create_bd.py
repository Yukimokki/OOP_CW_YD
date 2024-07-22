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
    def __init__(self):
        self.filepath = os.path.join(ROOT_DIR, 'data', 'vacancies.json')

    # def print_filepath(self):
    #     filepath = self.filepath
    #     print(filepath)

    def read_file(self):
        """
        читает файл с вакансиями

        """
        FILEPATH = self.filepath
        with open(FILEPATH, "r", encoding="utf-8") as datafile:
            return json.load(datafile)


    def save_file(self, data):
        """
        сохраняет файл с вакансиями
        """
        FILEPATH = self.filepath
        with open(FILEPATH, "w", encoding="utf-8") as datafile:
            json.dump(data, datafile,  ensure_ascii=False, indent=4)

    def del_file(self):
        """
        очищает файл с вакансиями
        :return:
        """
        FILEPATH = self.filepath
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
                requirements = vac['snippet']['requirement'].lower() if vac['snippet']['requirement'] else ''
                responsibility = vac['snippet']['responsibility'].lower() if vac['snippet']['responsibility'] else ''
                if criterion.lower() in requirements or criterion in responsibility and vac['salary'] != None:
                    if vac['salary'] and currency_choice.lower() == vac['salary'].get('currency').lower():
                        criterion_vac.append(vac)
                else:
                    empty_list.append(vac)
                    continue

            #print(len(criterion_vac),len(empty_list))
        return criterion_vac
