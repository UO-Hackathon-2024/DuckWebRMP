import mysql.connector
import ast

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',         # Your MySQL server host
    user='kai',     # Your MySQL username
    password='hack_24',  # Your MySQL password
    database='professor_table' # The database you want to access
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Execute a query to select all records from the comment table
cursor.execute("SELECT * FROM comment")

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)


def overall_rating(name:str):
    total_rating = 0
    divisor = 0
    for row in rows:
        if row[1] == name:
            total_rating += ast.literal_eval(str(row[2]))
            divisor += 1
    return round(total_rating/divisor,2)

def difficulty_rating(name:str):
    total_rating = 0
    divisor = 0
    for row in rows:
        if row[1] == name:
            total_rating += ast.literal_eval(str(row[3]))
            divisor += 1
    return round(total_rating/divisor,2)

def course_rating(name:str,course:str):
    total_rating = 0
    divisor = 0
    for row in rows:
        if row[1] == name and row[4] == course:
            total_rating += ast.literal_eval(str(row[2]))
            divisor += 1
    return round(total_rating/divisor,2)


s='John Doe'   
c = 'Math 101'  
print(course_rating(s,c))  
            


# Close the cursor and connection
cursor.close()
connection.close()
