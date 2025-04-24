## Description 
This is a simple example of FastAPI framework with authentication and asyncio library making requests to get stock data simultaneously <br/>

## HOW TO SECTION:

Installing Application <br/>

Step 1. Navigate to directory where you want to clone application <br/>
   
Step 2. Clone repository using url https://github.com/Svajunas900/FastAPI_Stocks.git <br/>
````
git clone https://github.com/Svajunas900/FastAPI_Stocks.git
````
Step 3. Install all the dependencies
````
pip install -r requirements.txt
````

    
 ## Guide for starting this app locally
   
Step 1. Use this command 
````
fastapi dev main.py
````

## Guide for starting this app from docker <br/>

Step 1. Run this command in cmd:
````
docker build . -t appname
````
Step 2. Run:
````
docker run -p 8000:8000 appname 
````
![Untitled](https://github.com/user-attachments/assets/6b8968d8-bec8-41fd-acf6-8115caa823ff)
