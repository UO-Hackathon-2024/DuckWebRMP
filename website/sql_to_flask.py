import mysql.connector

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

def course_rating(professor:str):
    

# Close the cursor and connection
cursor.close()
connection.close()
