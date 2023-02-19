import os
import json
import csv
from typing import List
from xml.etree import ElementTree as ET

BASE_DIR = os.path.join(os.path.dirname(__file__))
PATH = BASE_DIR + '\data'
FILE_PATH_CSV = PATH + '\output.csv'
FILE_PATH_JSON = ""


class DataConverter:
    FIELDNAMES = ['first_name', 'last_name', 'age', 'city']

    @staticmethod
    def input_data(iter_number: int) -> List[dict]:
        persons = []
        count = 1
        while count <= iter_number:
            print(f"Person #{count}")
            person_dict = {'first_name': input("Enter first name: "),
                           'last_name': input("Enter last name: "),
                           'age': input("Enter age: "),
                           'city': input("Enter city: ")
            }
            count += 1
            persons.append(person_dict)
        return persons

    def to_csv(self, persons: List[dict], mode) -> None:
        with open(FILE_PATH_CSV, mode) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=self.FIELDNAMES
            )
            if mode == 'w':
                writer.writeheader()
                for person in persons:
                    writer.writerow(person)



class DataInterface:

    def __init__(self, iter_num=2, mode='w'):
        self.converter = DataConverter()
        self.iter_num = iter_num
        self.mode = mode

    def main(self):
        persons = self.converter.input_data(self.iter_num)
        self.converter.to_csv(persons, self.mode)




if __name__ == '__main__':
    data_int = DataInterface()
    data_int.main()





