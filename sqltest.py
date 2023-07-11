import json
import os
import pyodbc
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

#Azure SQL Database connection
AZURE_DB_SERVER = os.environ.get("AZURE_DB_SERVER")
AZURE_DB_NAME = os.environ.get("AZURE_DB_NAME")
AZURE_DB_USERNAME = os.environ.get("AZURE_DB_USERNAME")
AZURE_DB_PASSWORD = os.environ.get("AZURE_DB_PASSWORD")
AZURE_DB_DRIVER = '{ODBC Driver 18 for SQL Server}'

""" with pyodbc.connect('DRIVER='+AZURE_DB_DRIVER+';SERVER=tcp:'+AZURE_DB_SERVER+';PORT=1433;DATABASE='+AZURE_DB_NAME+';UID='+AZURE_DB_USERNAME+';PWD='+ AZURE_DB_PASSWORD) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone() """

conn = pyodbc.connect('DRIVER='+AZURE_DB_DRIVER+';SERVER=tcp:'+AZURE_DB_SERVER+';PORT=1433;DATABASE='+AZURE_DB_NAME+';UID='+AZURE_DB_USERNAME+';PWD='+ AZURE_DB_PASSWORD)
c = conn.cursor()

ip_address = "1.2.3.4"
user_input = "I asked this requestion"
bot_response = "I got this response"
now = datetime.now()
print(now)


log_record = f'IP Address: {ip_address}, User input: {user_input}, Bot response: {bot_response}'

c.execute("INSERT INTO chat_log (timestamp, ip_address, user_input, bot_response) VALUES (?, ?, ?, ?)", (now, ip_address, user_input, bot_response))
conn.commit()
