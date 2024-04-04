import os.path

from fastapi import FastAPI, UploadFile, HTTPException
from fastapi_pagination import Page, add_pagination, paginate
from starlette.responses import HTMLResponse

from src.core.domain.Person import Person
from src.core.services.CsvExtractorService import CsvExtractor

app = FastAPI()
add_pagination(app)

file_extractor_usecase = CsvExtractor()
@app.get("/read-file", response_model=Page[Person])
def get_csv_person():
    result = file_extractor_usecase.extract(file_path="src/files/input.csv", chunksize=5000)
    return paginate(result)


@app.post("/upload")
async def create_upload_files(files: list[UploadFile]):
    filename = files[0].filename
    file_extension = os.path.splitext(filename)[1]

    if file_extension != ".csv":
        raise HTTPException(status_code=400, detail="Only csv files are supported")

    file_extractor_usecase.upload_file(files)

    return {"response": True}


@app.get("/")
async def main():
    content = """
<body>
<form action="/upload" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
