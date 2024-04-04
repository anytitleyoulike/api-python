from abc import abstractmethod, ABC

from fastapi import UploadFile

from src.core.domain.Person import Person


class FileUseCase(ABC):
    @abstractmethod
    def extract(self, file_path: str, chunksize: int) -> list[Person]:
        pass

    @abstractmethod
    def upload_file(self, files: list[UploadFile]):
        pass