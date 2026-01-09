from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


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


async def current_user():
    pass


def search_user(username: str):
    if username in users_db:
        return UserDB(users_db[username])


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=400, detail="El usuario no es correcto")

    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=400, detail="La contraseña no es correcta")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
