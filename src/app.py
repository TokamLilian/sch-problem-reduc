import os
import json
import threading

import webbrowser

from flask import Flask, jsonify, render_template

import subprocess

current_dir = os.path.join(os.path.dirname(__file__), 'frontend')
session_file = os.path.join(current_dir, 'session.json')

app = Flask(__name__, template_folder='frontend')

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
            return jsonify(semester_data)
        
    except Exception as e:
        print("Couldn't load data from session file.", str(e))

@app.route("/")
def serve_index():
    return render_template('index.html')


def open_browser():
    webbrowser.open_new_tab("http://127.0.0.1:5001/")


if __name__ == '__main__':
    # Start Flask app in a separate thread
    # app_thread = threading.Thread(target=app.run, kwargs={'debug': True})
    # app_thread.start()

    webbrowser_timer = threading.Timer(1, open_browser)
    webbrowser_timer.start()

    app.run(debug=False, port=5001)

##---Execute get_semester() ---##
## curl http://127.0.0.1:5001/api/get_semester ##


##---Execute run_program() from seperate terminal ---##
## curl http://127.0.0.1:5001/api/run_program ##