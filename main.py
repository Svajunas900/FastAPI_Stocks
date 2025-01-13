import requests
from fastapi import FastAPI
from dotenv import load_dotenv
import os
import asyncio


load_dotenv()

POLYGON_KEY = os.getenv("POLYGON_IO_KEY")
FASTFOREX_KEY = os.getenv("FASTFOREX_KEY")


async def fetch(url, header):
  return requests.get(url, headers=header).json()


async def main(stock_ticker, date):
    # url_1 = f'https://eodhd.com/api/eod/{stock_ticker}.US?api_token=67851ece540be1.07274292&fmt=json'
    url_2 = f"https://api.polygon.io/v1/open-close/{stock_ticker}/{date}?adjusted=true"
    
    # headers_url1 = {
    #   'Authorization': f'Bearer  67851ece540be1.07274292'
    # }

    headers_url2 = {
    'Authorization': f'Bearer {POLYGON_KEY}'
    }

    # response1 = await fetch(url_1, headers_url1)
    response2 = await fetch(url_2, headers_url2)

    # print("Response from URL 1:", response1)
    print("Response from URL 2:", response2)

asyncio.run(main("AAPL","2025-01-03"))


# def get_stock_prices_fastforex():
#   url = f'https://eodhd.com/api/intraday/AAPL.US?api_token=67851ece540be1.07274292&fmt=json'
#   response = requests.get(url)
#   print(response)
#   print(response.json())
#   return response.json()


# async def get_stock_prices_polygon(stock_ticker, date):
#   date = "2025-01-03"
#   url = f"https://api.polygon.io/v1/open-close/{stock_ticker}/{date}?adjusted=true"
#   headers = {
#     'Authorization': f'Bearer {POLYGON_KEY}'
#   }
#   response = requests.get(url, headers=headers)
#   print(response)
#   print(response.json())
#   return response.json()


# asyncio.run(get_stock_prices_polygon("AAPL","2025-01-03"))
# get_stock_prices_fastforex()


# app = FastAPI()


# @app.get("/")
# def home():
#   return "Hello world"