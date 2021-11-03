from flask import Flask, jsonify, request, render_template, redirect, url_for,send_file 
from flask_api import FlaskAPI, status, exceptions
import os, json, requests
from werkzeug.utils import secure_filename
from requests import get
import SoilFilter
UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# api_endpoint=f""+os.getenv('api_endpoint')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/') 
def index(): 
	return "Flask server"

################################################### SOIL FILTER API#################################################    

@app.route('/getSoilNet', methods = ['GET','POST']) 
def filter():
    
    img_data = request.files['image']
    if img_data.filename == '':
        return jsonify({'msg':"Image not found"})
    f=0
    result=""
    Error="None"
    if img_data and allowed_file(img_data.filename):
        filename = secure_filename(img_data.filename)
        img_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # print(img_path)
        img_data.save(img_path)
        try:
            result= SoilFilter.inference(img_path)
        except Exception as error:
            Error="Error in the model Inference File"
            try:
                f=1
                os.remove(img_path)
            except Exception as error2:
                Error="Error removing or closing downloaded file handle and buggy inference file"
                app.logger.error("Error removing or closing downloaded file handle", error2)
            app.logger.error("Error in the model Inference File", error)
        if f==0:
            try:
                os.remove(img_path)
            except Exception as error:
                Error="Error removing or closing downloaded file handle"
                app.logger.error("Error removing or closing downloaded file handle", error)
    return jsonify({'msg': 'success','result':result,'error':Error}) 


if __name__ == "__main__": 
	app.run(threaded=True, port = int(os.environ.get('PORT', 5000)))