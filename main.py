from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ml.ml_model import create_component
from ml.db import connectDataBase

connectDataBase()

app = FastAPI(
    title="LangChain Server",
    version="1.0"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ComponentRequest(BaseModel):
    description: str

@app.post("/api/v1/generate-component")
async def generate_component(request: ComponentRequest):
    component = create_component(request.description)
    return component


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
