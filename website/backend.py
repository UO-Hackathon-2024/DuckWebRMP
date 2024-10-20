from flask import Flask
from flask import render_template, request, session, jsonify
import mysql.connector
import ast



# Initialize the app
app = Flask(__name__)
app.secret_key = "test"

db_config = {
    'host': 'localhost',
    'user': 'kai',
    'password': 'hack_24',
    'database': 'professor_table'
}







# Define a route
@app.route('/', methods=['GET', 'POST'])
def home():
    courses = ['CS 102', 'CS 110', 'CS 111', 'CS 122', 'CS 210', 'CS 212', 'CS 314', 'CS 322', 'CS 332', 'CS 402', 'CS 407', 'CS 410', 
           'CS 415', 'CS 420', 'CS 422', 'CS 425', 'CS 431', 'CS 432', 'CS 443', 'CS 451', 'CS 471', 'CS 507', 'CS 510', 'CS 520', 
           'CS 522', 'CS 531', 'CS 532', 'CS 543', 'CS 551', 'CS 571', 'CS 607', 'CS 610', 'CS 640', 'CS 633']
    profs = [
    "Carrere D", "Flores J", "Kutnyi D", "Balivada N", "Soh Y", 
    "Thuzar A", "Subedi S", "Hall J", "Nepal A", "Mathai M", 
    "Young M", "Cross Z", "Shabanzadeh S", "Ponraj R", "Lei Y", 
    "Colbert P", "Majumder M", "Mclewe G", "Lowd D", "Nelson J", 
    "Wills E", "Teske A", "Norris B", "Lisan A", "Freeman Hennessy K", 
    "Wang Y", "Malony A", "Srinivasan S", "Ndemeye B", "Wilson C", 
    "Ariola Z", "Yapucuoglu M", "Choi J", "Rejaie R", "Hornof A", 
    "Gupta S", "Nguyen T", "Wang Y", "Wilson C", "Choi J", 
    "Rejaie R", "Hornof A", "Gupta S", "Nguyen T", "Hou T", 
    "Li J"
    ] 

    return render_template('home.html',courses=courses, profs= profs) #the list courses is being passed to the html as a variable



     

# Run the app
@app.route('/courses', methods=['POST'])
def get_courses():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    
    selected_course = request.form.get('courses') 
    selected_prof = request.form.get('prof')

    if selected_course == "None" and selected_prof == "None": 
        cursor.execute(f"SELECT * FROM duckwebscraper")
        courses = cursor.fetchall()
        cursor.execute(f"SELECT * FROM reviews")
        reviews = cursor.fetchall()


    if selected_course != "None" and selected_prof == "None": 
        selected_course = selected_course.replace(" ", "")

        alternate_course = ""
        if selected_course.startswith("CS"): 
            alternate_course = "CIS" + selected_course[2:]

        cursor.execute(f"SELECT * FROM duckwebscraper WHERE (course = '{selected_course}') OR (course = '{alternate_course}')")
        courses = cursor.fetchall()
        cursor.execute(f"SELECT * FROM reviews WHERE (class = '{selected_course}') OR (class = '{alternate_course}')")
        reviews = cursor.fetchall()

    if selected_course == "None" and selected_prof != "None": 
        cursor.execute(f"SELECT * FROM duckwebscraper WHERE (Professor = '{selected_prof}')")
        courses = cursor.fetchall()
        cursor.execute(f"SELECT * FROM reviews WHERE (professor_name = '{selected_prof}')")
        reviews = cursor.fetchall()

    if selected_course != "None" and selected_prof != "None": 
        selected_course = selected_course.replace(" ", "")

        alternate_course = ""
        if selected_course.startswith("CS"): 
            alternate_course = "CIS" + selected_course[2:]
        cursor.execute(f"""SELECT * FROM duckwebscraper WHERE (course = '{selected_course}' OR course = '{alternate_course}')
                       AND (Professor = '{selected_prof}')""")
        courses = cursor.fetchall()
        cursor.execute(f"""SELECT * FROM reviews WHERE (class = '{selected_course}' OR class = '{alternate_course}')
                       AND (professor_name = '{selected_prof}')""")
        reviews = cursor.fetchall()



    cursor.close()
    connection.close()

    return render_template('courses.html', courses=courses, reviews=reviews)


        
@app.route('/mycourses', methods=['POST'])
def get_my_courses(): 
    course_response = request.form.get('my_course')
    course = course_response[1]
    action = course_response[0]
    if action = "ADD" and course:
        course = ast.literal_eval(course)
        if 'my_courses' not in session:
            session['my_courses'] = []
        session['my_courses'].append(course)
        session.modified = True
    else: 
        session['my_courses'].pop(course)
    my_courses = session.get('my_courses', [])
    return render_template('mycourses.html', my_courses=my_courses)







if __name__ == '__main__':
    app.run(debug=True)

    
