# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, jsonify
import threading

# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

# Initial sentence
current_message = "Welcome to the main screen!"

# Lock for thread safety
lock = threading.Lock()


# This function gets a string and present it on the website for all users to see
def set_homescreen_message(message):
    global current_message
    with lock:
        current_message = message


# Get data from someone
@app.route('/api', methods=['POST'])
def api():
    data = request.form['message']

    # do something

    return jsonify({'status': 'success', 'message': data})


# The route() function of the Flask class tells the application which URL should call the associated function.
@app.route('/')
def main_screen():
    # ‘http://127.0.0.1:5050/’ URL is bound with main_screen() function.
    return render_template('index.html', sentence=current_message)

 
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application on the local development server.
    app.run(port=5050)

