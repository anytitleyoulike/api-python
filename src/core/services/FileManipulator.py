import os

from fastapi import UploadFile
from pandas import pandas

from src.core.domain.Person import Person
from src.core.usecase.FileUseCase import FileUseCase


class FileManipulator(FileUseCase):
    def __init__(self):
        self.person_data = []

    def upload_file(self, files: list[UploadFile]):

        file_path = os.path.join("src/files", files[0].filename)
        with open(file_path, "wb") as f:
            f.write(files[0].file.read())

    def extract(self, file_path: str, chunksize=5000) -> list[Person]:

        if not self.person_data:
            for chunk in pandas.read_csv(file_path, chunksize=chunksize):
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
