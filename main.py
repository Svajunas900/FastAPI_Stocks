import requests
from fastapi import FastAPI

response = requests.get("https://polygon.io/")

app = FastAPI()

@app.get("/")
def home():
  return "Hello world"