FROM python:slim

WORKDIR /fastapi_stock

COPY . .

RUN pip install -r requirements.txt

RUN pip install "fastapi[standard]"

CMD [ "fastapi", "run", "main.py", "--port", "8000" ]

EXPOSE 8000