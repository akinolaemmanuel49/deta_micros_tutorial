import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from deta import Deta
from dotenv import load_dotenv
from json import dump

from schemas import UserSchema

DOTENV_PATH = os.path.join(os.path.dirname(__file__), ".env")

load_dotenv(dotenv_path=DOTENV_PATH)

deta = Deta(os.environ.get("PROJECT_KEY"))
db = deta.Base("users")
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/users", response_model=UserSchema)
async def create_user(user: UserSchema):
    new_user = db.put(user.dict())
    return new_user


@app.get("/users/{key}", response_model=UserSchema)
async def get_user(key: str):
    user = db.get(key)
    return user


@app.put("/users/{key}", response_model=UserSchema)
async def update_user(key: str, user: UserSchema):
    updated_user = db.update(user.dict(), key)
    return updated_user


@app.delete("/users/{key}")
async def delete_user(key: str):
    db.delete(key)
    return {"message": "User deleted"}
