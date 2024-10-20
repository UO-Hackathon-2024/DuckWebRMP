

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from review import Review


load_dotenv()


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',         # Your MySQL server host
            user='kai',     # Your MySQL username
            password='hack_24',  # Your MySQL password
            database='professor_table' # The database you want to access)
        )


    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def insert_review(review: Review): 
    connection = create_connection()
    cursor = connection.cursor()

    try: 
        sql = f"""INSERT INTO reviews (comment, professor_name, rating, difficulty_rating, class) VALUES 
              ('{review.get_comment()}', '{review.get_prof()}', {review.get_quality()}, {review.get_difficulty()}, '{review.get_course()}') """

        connection.cursor().execute(sql)
        connection.commit()
    except Exception as e: 
        print("Review already exists")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()








    

