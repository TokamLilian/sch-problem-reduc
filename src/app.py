import os
import sys
import json
import threading

import http.server
import socketserver
import webbrowser

from flask import Flask, jsonify, render_template
from collections import OrderedDict

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
            semester_data = json.load(json_file, object_pairs_hook=OrderedDict)
            return jsonify(semester_data, sort_keys=False)
        
    except Exception as e:
        print("Couldn't load data from session file.", str(e))


@app.route("/")
def serve_index():
    return render_template('index.html')

def run_tkinter_app():
    try:
        subprocess.run(['py', 'tkinter_app.py'], check=True)
        return 'Tkinter app opened successfully.'
    except Exception as e:
        print('Error running program', str(e))


# def open_browser():
#     webbrowser.open_new_tab("http://127.0.0.1:5001/")

if __name__ == '__main__':
    # Start Flask app in a separate thread
    # app_thread = threading.Thread(target=app.run, kwargs={'debug': True})
    # app_thread.start()

    tkinter_timer = threading.Timer(1, run_tkinter_app)
    tkinter_timer.start()

    # webbrowser_timer = threading.Timer(1, open_browser)
    # webbrowser_timer.start()

    app.run(debug=False, port=5001)

##---Execute get_semester() ---##
## curl http://127.0.0.1:5001/api/get_semester ##


##---Execute run_program() ---##
## curl http://127.0.0.1:5001/api/run_program ##