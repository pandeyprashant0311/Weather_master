import os
from flask import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)+" "+os.getcwd()

