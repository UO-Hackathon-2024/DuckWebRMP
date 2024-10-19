from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


# Initialize the app
app = Flask(__name__)

# Define a route
@app.route('/')
@app.route('/<userName>')
def home(userName="Guest"):
    return render_template('home.html', name=userName)

courses = ['CS 102', 'CS 110', 'CS 111', 'CS 122', 'CS 210', 'CS 212', 'CS 314', 'CS 322', 'CS 332', 'CS 402', 'CS 407', 'CS 410', 
           'CS 415', 'CS 420', 'CS 422', 'CS 425', 'CS 431', 'CS 432', 'CS 443', 'CS 451', 'CS 471', 'CS 507', 'CS 510', 'CS 520', 
           'CS 522', 'CS 531', 'CS 532', 'CS 543', 'CS 551', 'CS 571', 'CS 607', 'CS 610', 'CS 640', 'CS 633']

names = [
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
     

# Run the app
@app.route('/subject_selection', methods=['POST'])
def submit_selection():
    selected_subject = request.form['subject']
    return f'You Picked: {selected_subject}'
if __name__ == '__main__':
    app.run(debug=True)

    