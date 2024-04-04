import os.path

from fastapi import FastAPI, UploadFile, HTTPException
from fastapi_pagination import Page, add_pagination, paginate
from starlette.responses import HTMLResponse

from src.core.domain.Person import Person
from src.core.services.FileManipulator import FileManipulator

app = FastAPI()
add_pagination(app)

file_manipulator = FileManipulator()


@app.get("/read", response_model=Page[Person])
def read_file():
    try:
        result = file_manipulator.extract()
        return paginate(result)
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/upload")
async def create_upload_files(files: list[UploadFile]):
    filename = files[0].filename
    file_extension = os.path.splitext(filename)[1]

    if file_extension != ".csv":
        raise HTTPException(status_code=400, detail="Only csv files are supported")

    file_manipulator.upload_file(files)

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
