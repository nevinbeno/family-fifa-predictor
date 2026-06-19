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

print(f"==  Add Fixtures ==")

n = int(input("No. of matches: "))
try:
    for i in range(n):
        print(f"Match {i + 1}:")
        team1 = input("Team 1: ")
        team2 = input("Team 2: ")
        cursor.callproc("add_match", [team1, team2])

    conn.commit()
    print(f"{n} matches added successfully.")

except mysql.connector.Error as err:
    conn.rollback()
    print("Database error:", err)

finally:
    cursor.close()
    conn.close()

print(f"{n} Matches added.")