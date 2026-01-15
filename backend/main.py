from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os
import shutil

from backend.models.tryon_job import TryOnJob
from backend.services.tryon_router import decide_pipeline

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Armazenamento temporário de jobs (MVP)
JOBS = {}


@app.get("/")
def home():
    return {"status": "API do Provador Virtual rodando"}


@app.post("/try-on")
async def create_tryon_job(
    user_image: UploadFile = File(...),
    product_image: UploadFile = File(...),
    category: str = Form(...)
):
    """
    Cria um job de provador virtual e decide o pipeline automaticamente.
    """

    user_path = os.path.join(UPLOAD_DIR, f"user_{user_image.filename}")
    product_path = os.path.join(UPLOAD_DIR, f"product_{product_image.filename}")

    with open(user_path, "wb") as buffer:
        shutil.copyfileobj(user_image.file, buffer)

    with open(product_path, "wb") as buffer:
        shutil.copyfileobj(product_image.file, buffer)

    pipeline = decide_pipeline(product_path, category)

    job = TryOnJob(
        user_image_path=user_path,
        product_image_path=product_path,
        product_category=category,
        pipeline=pipeline
    )

    JOBS[job.id] = job

    return JSONResponse(
        content={
            "job_id": job.id,
            "pipeline": job.pipeline,
            "status": job.status
        }
    )


