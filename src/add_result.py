import mysql.connector
from dotenv import load_dotenv
import os


def add_result():
    load_dotenv()
    conn = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWD"),
        database=os.getenv("DB_NAME")
    )

    cursor = conn.cursor()
    print(f"==  Add Result ==")
    n = int(input("No of matches: "))

    try:
        for i in range(n):
            match_id = int(input("Match Number: "))
            result = input("Result: ")
            cursor.callproc("add_result", [match_id, result])
        conn.commit()
        print(f"Results have been added successfully..")
    except mysql.connector.Error as err:
        conn.rollback()
        print(f"Database Error: {err}")
    finally:
        cursor.close()
        conn.close()

if __name__=="__main__":
    add_result()