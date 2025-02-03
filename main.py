from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import requests
from dotenv import load_dotenv
import os
import asyncio


load_dotenv()

POLYGON_KEY = os.getenv("POLYGON_IO_KEY")
FASTFOREX_KEY = os.getenv("FASTFOREX_KEY")


async def fetch(url, header):
  return requests.get(url, headers=header).json()


async def async_function(stock_ticker, date):
    url_1 = f'https://eodhd.com/api/eod/{stock_ticker}.US?api_token={FASTFOREX_KEY}&fmt=json'
    url_2 = f"https://api.polygon.io/v1/open-close/{stock_ticker}/{date}?adjusted=true"
    
    headers_url1 = {
      'Authorization': f'Bearer  {FASTFOREX_KEY}'
    }

    headers_url2 = {
    'Authorization': f'Bearer {POLYGON_KEY}'
    }

    response1 = await fetch(url_1, headers_url1)
    response2 = await fetch(url_2, headers_url2)

    print("Response from URL 1:", response1)
    print("Response from URL 2:", response2)


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
def home():
  # asyncio.run(async_function("AAPL","2025-01-03"))
  return "Hello world"


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


def fake_hash_password(password: str):
    return "fakehashed" + password


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}