#Create Sample Python File
from flask import Flask

app = Flask(__name__)

@app.route("/Home")
def hello():
    return "Hello World"

app.run(debug=True, port=8000)
