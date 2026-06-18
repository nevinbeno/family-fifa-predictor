import mysql.connector
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()
print(f"==  Add a Match ==")
team1 = input("Team 1: ")
team2 = input("Team 2: ")

cursor.callproc("add_match", [team1, team2])
conn.commit()

print("Match added.")