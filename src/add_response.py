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

n = int(input(f"No of matches: "))
try:    
    for i in range (n):
        match_id = input(f"Enter the Match Number: ")
        rob = input(f"Enter Robin's response: ")
        tan = input(f"Enter Tanya's response: ")
        nev = input(f"Enter Nevin's response: ")
        niy = input(f"Enter Niya's response: ")
        cursor.execute(
            """
            insert into Match_Result values 
            (%d, %s, %s, %s)""", (match_id, rob, tan, nev, niy)
        )
    conn.commit()
    print(f"Responses added successfully. ")
except mysql.connector.Error as err:
    conn.rollback()
    print(f"Database error: {err}")
finally:
    cursor.close()
    conn.close()