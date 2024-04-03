from fastapi import FastAPI, UploadFile
from fastapi_pagination import Page, add_pagination, paginate
from starlette.responses import HTMLResponse

from src.web.fastapi.CsvExtractorService import CsvExtractor
from src.web.fastapi.domain.Person import Person

app = FastAPI()
add_pagination(app)


@app.get("/")
def main_endpoint() -> str:
    return f"Hello World"


@app.get("/person", response_model=Person)
def get_person():
    return Person(name="Marcello", age=33)


@app.get("/person-csv", response_model=Page[Person])
def get_csv_person():
    result = CsvExtractor().extract("input.csv")
    return paginate(result)


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):

    return {"filenames": files[0].filename}


@app.get("/upload")
async def main():
    content = """
<body>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
