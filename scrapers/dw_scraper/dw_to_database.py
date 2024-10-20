

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
import json 

load_dotenv()


def main(): 
    with open("profs.json", "r") as file: 
        course_info = json.load(file)

    insert_info(course_info)





def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',         # Your MySQL server host
            user='kai',     # Your MySQL username
            password='hack_24',  # Your MySQL password
            database='professor_table' # The database you want to access)
        )

        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def insert_info(course_info: dict): 
    connection = create_connection()
    cursor = connection.cursor()

    try: 
        for prof_name in course_info: 
            prof_info = course_info[prof_name]
            

            sql = f"""INSERT INTO duckwebscraper (professor, day, time, course, room, crn) VALUES 
                  ('{prof_name}', '{prof_info["day"]}', '{prof_info["time"]}'
                   , '{prof_info["course_title"]}', '{prof_info["location"]}', '{prof_info["crn"]}') """

            connection.cursor().execute(sql)
            connection.commit()
    except Exception as e: 
        print("Could not execute sql", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == "__main__": 
    main()





    

