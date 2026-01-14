from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
import shutil

app = FastAPI()

UPLOAD_DIR = "uploads"

# Garante que a pasta de upload existe
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def home():
    return {"status": "API do Provador Virtual rodando"}


@app.post("/upload")
async def upload_imagem(file: UploadFile = File(...)):
    """
    Recebe uma imagem enviada pelo navegador e salva na pasta uploads/
    """

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return JSONResponse(
        content={
            "status": "ok",
            "filename": file.filename,
            "saved_at": file_path
        }
    )

