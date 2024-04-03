from abc import abstractmethod, ABC


class FileExtractor(ABC):
    @abstractmethod
    def extract(self, file_path: str, chunksize: int):
        pass
