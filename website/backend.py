from flask import Flask
from flask import render_template

# Initialize the app
app = Flask(__name__)

# Define a route
@app.route('/')
@app.route('/<userName>')
def home(userName="Guest"):
    return render_template('home.html', name=userName)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

    