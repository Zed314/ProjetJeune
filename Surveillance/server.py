from flask import Flask
import os
import datetime
from flask import abort
from flask import send_file
from flask import render_template
app = Flask(__name__)

from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(2)

@app.route('/')
def take_pic():
    camera.capture(str(datetime.datetime.now())+".jpg")
    return "OK"

@app.route('/getPic/<picName>')
def gp(picName):
    return send_file(picName)
@app.route('/getPics')
def dir_listing():
    BASE_DIR = '.'
   # Joining the base and the requested path
   # abs_path = os.path.join(BASE_DIR, req_path)
    # Return 404 if path doesn't exist
   # if not os.path.exists(abs_path):
    #    return abort(404)
    #if os.path.isfile(abs_path):
     #   return send_file(abs_path)
    # Show directory contents
    listFiles = []
    for file in os.listdir("."):
        if file.endswith(".jpg"):
            listFiles.append("getPic/"+file)
    return render_template('files.html', files=listFiles)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
