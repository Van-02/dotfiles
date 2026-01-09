from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "ivan": {
        "username": "van",
        "full_name": "Ivan Lalik",
        "email": "lalikivan02@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "ivan2": {
        "username": "van2",
        "full_name": "Ivan Martin Lalik",
        "email": "lalikivan2002@gmail.com",
        "disabled": True,
        "password": "654321"
    }
}


def search_user(username: str):
    if username in users_db:
        return UserDB(users_db[username])
