#!/bin/env python3

import flask
import time
TPL = flask.render_template

app = flask.Flask(__name__, template_folder='.')


# Main page
@app.route('/')
def info():
    data = """\
    Benoit benoit benoit benoit
    """
    return TPL("default.html", data=data)

# Example of parameter in a URL
@app.route('/paramurl/<int:number>')
def paramurl(number):
    print("Number :")
    print(number)
    data = """\
    You put {} in the URL.
    """.format(number)
    return TPL("default.html", data=data)


# Starts the server on port 5000
if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.secret_key = 'test'
    app.run(host='0.0.0.0', port=5000)
