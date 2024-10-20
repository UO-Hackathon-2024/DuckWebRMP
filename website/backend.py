from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


# Initialize the app
app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/subject_selection', methods=['POST'])
def submit_selection():
    selected_subject = request.form['subject']
    return f'You Picked: {selected_subject}'
if __name__ == '__main__':
    app.run(debug=True)

    