import os
from flask import Flask

BASE_PATH = os.getcwd()

UPLOAD_IMG_FOLDER = os.path.join(BASE_PATH, 'img_files')
UPLOAD_XML_FOLDER = os.path.join(BASE_PATH, 'xml_files')
UPLOAD_TXT_FOLDER = os.path.join(BASE_PATH, 'txt_files')


app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_IMG_FOLDER'] = UPLOAD_IMG_FOLDER
app.config['UPLOAD_XML_FOLDER'] = UPLOAD_XML_FOLDER
app.config['UPLOAD_TXT_FOLDER'] = UPLOAD_TXT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 0.2 * 1024 * 1024