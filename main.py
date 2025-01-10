import requests
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

POLYGON_KEY = os.getenv("POLYGON_IO_KEY")
FASTFOREX_KEY = os.getenv("FASTFOREX_KEY")


def get_stock_prices_fastforex():
  url = f"https://api.fastforex.io/fetch-all?api_key={FASTFOREX_KEY}"
  response = requests.get(url)
  print(response)
  print(response.json())
  return response.json()


def get_stock_prices_polygon(stock_ticker, date):
  date = "2025-01-03"
  url = f"https://api.polygon.io/v1/open-close/{stock_ticker}/{date}?adjusted=true"
  headers = {
    'Authorization': f'Bearer {POLYGON_KEY}'
  }
  response = requests.get(url, headers=headers)
  print(response)
  print(response.json())
  return response.json()


get_stock_prices_polygon("AAPL","2025-01-03")
get_stock_prices_fastforex()


app = FastAPI()


@app.get("/")
def home():
  return "Hello world"