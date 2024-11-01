from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, books, users
from . import database, models


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(books.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"Python API Development": "Comprehensive Course for Beginners"}
