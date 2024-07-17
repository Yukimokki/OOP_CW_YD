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


class WorkWithJson(FileWork):

    def read_file(self):
        FILEPATH = os.path.join(ROOT_DIR, 'data', 'file.json')
        with open(FILEPATH, "r", encoding="utf-8") as datafile:
            return json.load(datafile)

    def save_file(self, data):
        FILEPATH = os.path.join(ROOT_DIR, 'data', 'file.json')
        with open(FILEPATH, "w", encoding="utf-8") as datafile:
            json.dump(data, datafile,  ensure_ascii=False, indent=4)

    @staticmethod
    def get_data(criterion):
        """Метод получения данных из файла по указанным критериям"""
        criterion_vac = []
        FILEPATH = os.path.join(ROOT_DIR, 'data', 'file.json')
        with open(FILEPATH, "r", encoding="utf8") as datafile:
            vacancies = json.load(datafile)
            for vac in vacancies:
                if not vac["snippet"]["requirement"]:
                    continue
                else:
                    if criterion in vac["snippet"]["requirement"]:
                        criterion_vac.append(vac)
        return criterion_vac