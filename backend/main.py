from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API do Provador Virtual rodando"}
