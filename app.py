 # Problem 1
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Welcome to the Flask app!"

# @app.route('/greet/<username>')
# def greet(username):
#     return f"Hello, {username}!"

# @app.route('/farewell/<username>')
# def farewell(username):
#     return f"Goodbye, {username}!"


# if __name__ == '__main__':
#     app.run()

# Problem 2
from flask import Flask, render_template, request
# Import necessary modules

app = Flask(__name__)
# Create an instance of the Flask class

data = {}
# Create an empty dictionary to store data

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        data[key] = value
        # If the request method is POST, retrieve the key and value from the form data
        # and add them to the dictionary
    return render_template('create.html')
    # Render the create.html template, which contains the form for creating a new entry

@app.route('/read')
def read():
    return render_template('read.html', data=data)
    # Render the read.html template and pass the data dictionary to it
    # The template will display the current state of the dictionary

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        if key in data:
            data[key] = value
        # If the request method is POST, retrieve the key and value from the form data
        # and update the corresponding entry in the dictionary if it exists
    return render_template('update.html')
    # Render the update.html template, which contains the form for updating an existing entry

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            del data[key]
        # If the request method is POST, retrieve the key from the form data
        # and delete the corresponding entry from the dictionary if it exists
    return render_template('delete.html')
    # Render the delete.html template, which contains the form for deleting an existing entry

if __name__ == '__main__':
    app.run()
