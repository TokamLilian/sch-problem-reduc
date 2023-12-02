import os
import json
import threading

import webbrowser

from flask import Flask, jsonify, render_template

FLASK_ADDRESS = '127.0.0.1'  # Sever address
FLASK_PORT = 5001            # server port

import subprocess

current_dir = os.path.join(os.path.dirname(__file__), 'static')
session_file = os.path.join(current_dir, 'session.json')
color_file = os.path.join(current_dir, 'color_picker.json')

app = Flask(__name__, template_folder='static')

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

@app.route('/api/get_colorPicker', methods=['GET'])
def get_colorPicker():
    try:
        with open(color_file, "r", encoding='utf-8') as json_file:
            colors_data = json.load(json_file)
            return jsonify(colors_data)
        
    except Exception as e:
        print("Couldn't load data from session file.", str(e))


@app.route("/")
def serve_index():
    return render_template('index.html')

def run_PyQt5_app():
    try:
        subprocess.run(['py', 'PyQt5_app.py'], check=True)
        return 'PyQt5 app opened successfully.'
    except Exception as e:
        print('Error running program', str(e))

# def open_browser():
#     webbrowser.open_new_tab("http://127.0.0.1:5001/")


if __name__ == '__main__':
    # Start Flask app in a separate thread
    # app_thread = threading.Thread(target=app.run, kwargs={'debug': True})
    # app_thread.start()

    PyQt5_timer = threading.Timer(1, run_PyQt5_app)
    PyQt5_timer.start()

    # webbrowser_timer = threading.Timer(1, open_browser)
    # webbrowser_timer.start()

    app.run(debug=False, host=FLASK_ADDRESS, port=FLASK_PORT)

##---Execute get_semester() ---##
## curl http://127.0.0.1:5001/api/get_semester ##


##---Execute run_program() from seperate terminal ---##
## curl http://127.0.0.1:5001/api/run_program ##