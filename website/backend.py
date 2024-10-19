from flask import Flask

# Initialize the app
app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    return "Hello, Flask!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)