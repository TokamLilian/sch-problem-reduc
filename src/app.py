import os
import json

from flask import Flask, jsonify

import subprocess

current_dir = os.path.join(os.path.dirname(__file__), 'frontend')
session_file = os.path.join(current_dir, 'session.json')

app = Flask(__name__)

@app.route('/api/run_program', methods=['GET'])
def run_program():
    try:
        subprocess.run(['py', 'main.py'], check=True)
    except Exception as e:
        print('Error running program', str(e))

    return jsonify(None)

@app.route('/api/get_semester', methods=['GET'])
def get_semester():
    try:
        with open(session_file, "r", encoding='utf-8') as json_file:
            semester_data = json.load(json_file)
            return semester_data
        
    except Exception as e:
        print("Couldn't load data from session file.", str(e))

if __name__ == '__main__':
    app.run(debug=True, port=5001)

##---Execute get_semester() ---##
## curl http://127.0.0.1:5001/api/_get_semester ##


##---Execute run_program() ---##
## curl http://127.0.0.1:5001/api/run_program ##