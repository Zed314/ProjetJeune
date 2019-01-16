#!/bin/env python3

import flask
import RPi.GPIO as GPIO
import time
TPL = flask.render_template

app = flask.Flask(__name__, template_folder='.')


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


@app.route('/')
def info():
    print "LED on"
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print "LED off"
    GPIO.output(18,GPIO.LOW)
    data = """\
    Benoit benoit benoit benoit
    """
    return TPL("default.html", title='Home', data=data)

@app.route('/paramurl/<int:number>')
def paramurl(number):
    print("Number")
    print(number)
    data = """\
    You put {} in the URL.
    """.format(number)
    return TPL("default.html", title='ParamUrl', data=data)



@app.route('/forbidden')
def forbidden():
    flask.abort(403)

print("PATH =====>", app.instance_path)
if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.secret_key = 'test'
    app.run(host='0.0.0.0', port=5000)