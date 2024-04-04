import datetime
import os

from fastapi import UploadFile
from pandas import pandas

from src.core.domain.Person import Person
from src.core.usecase.FileUseCase import FileUseCase


class FileManipulator(FileUseCase):
    def __init__(self):
        self.person_data = []
        self.file_path = "src/files"
        self.current_file = ""

    def __check_path_exists(self, file_path: str) -> bool:
        return os.path.exists(file_path)
    
    def __format_file_path(self,file_name) -> str:
        current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{current_time}_{file_name}"
        return os.path.join(self.file_path, file_name)
    
    def __get_newest_file(self) -> str:
        files = os.listdir(self.file_path)
        return max(files)
    
    def upload_file(self, files: list[UploadFile]):
        if not self.__check_path_exists(self.file_path):
            os.mkdir(self.file_path) 
        
        file_path = self.__format_file_path(files[0].filename)

        with open(file_path, "wb") as f:
            f.write(files[0].file.read())

    def extract(self) -> list[Person]:
        try: 
            newest_file = self.__get_newest_file()
            if self.current_file != newest_file:
                self.current_file = newest_file
                file_path = os.path.join(self.file_path, newest_file)
                for chunk in pandas.read_csv(file_path, chunksize=5000):
                    for row in chunk.itertuples(index=False):
                        person = Person(name=row[0],
                                        governmentId=str(row[1]),
                                        email=row[2],
                                        debtAmount=float(row[3]),
                                        debtDueDate=row[4],
                                        debtId=row[5]
                                        )
                        self.person_data.append(person)

            return self.person_data
        except FileNotFoundError as e:
            raise FileNotFoundError("No file found. Please upload a .csv file")
