# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, redirect
import os
 
# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)


@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']

    #
    #
    # HERE you will write your user adding logic
    #
    #

    return redirect('/')


@app.route('/bye')
def goodbye_world():
    # ‘http://127.0.0.1:5000/bye’ URL is bound with goodbye_world() function.
    return 'Goodbye World'


# The route() function of the Flask class tells the application which URL should call the associated function.
@app.route('/')
def index():
    # ‘http://127.0.0.1:5000/’ URL is bound with index() function.
    return render_template('index.html')
 
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application on the local development server.
    app.run(port=5000)