from pandas import pandas

from src.web.fastapi.domain.Person import Person
from src.web.fastapi.FileExtractor import FileExtractor


class CsvExtractor(FileExtractor):

    def extract(self, file_path: str, chunksize=5000) -> list:
        person_data = []

        for chunk in pandas.read_csv(file_path, chunksize=chunksize):
            for row in chunk.itertuples(index=False):
                person = Person(name=row[0],
                                governmentId=str(row[1]),
                                email=row[2],
                                debtAmount=float(row[3]),
                                debtDueDate=row[4],
                                debtId=row[5]
                                )
                person_data.append(person)

        return person_data
