import os
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


# class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == '/':
#             self.path = '/frontend/index.html'
#         return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Handler = MyRequestHandler
# server = socketserver.TCPServer(('127.0.0.1', 8080), Handler)

# server.serve_forever()

@app.route("/")
def lauch_html():
    # PORT = 8080
    # HOSTNAME = 'localhost'
    # handler = http.server.SimpleHTTPRequestHandler
    # with socketserver.TCPServer((HOSTNAME, PORT), handler) as httpd:
    #     print(f"serving at port {PORT}")
    #     httpd.serve_forever()

    return render_template('index.html')

def open_browser():
    webbrowser.open_new_tab("http://127.0.0.1:5001/")

if __name__ == '__main__':
    # Start Flask app in a separate thread
    app_thread = threading.Thread(target=app.run, kwargs={'debug': True})
    app_thread.start()

    webbrowser_timer = threading.Timer(1, open_browser)
    webbrowser_timer.start()

    app.run(debug=True, port=5001)

##---Execute get_semester() ---##
## curl http://127.0.0.1:5001/api/_get_semester ##


##---Execute run_program() ---##
## curl http://127.0.0.1:5001/api/run_program ##