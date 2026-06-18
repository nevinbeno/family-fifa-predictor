import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()
print(f"==  Add a Result ==")
match_id = input("Match Number: ")
result = input("Result: ")

cursor.callproc("add_result", [match_id, result])
conn.commit()

print("Result added.")