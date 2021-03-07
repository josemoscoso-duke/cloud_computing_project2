import os
import io
#import magic
import urllib.request
from app import app
from flask import Flask, Response, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from app_utils import parse_xml, draw_bounding_box

ALLOWED_EXTENSIONS = set(['xml', 'png', 'jpg', 'jpeg'])
ALLOWED_IMG_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
ALLOWED_XML_EXTENSION = set(['xml'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].\
                                        lower() in ALLOWED_EXTENSIONS

def allowed_img_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].\
                                        lower() in ALLOWED_IMG_EXTENSIONS

def allowed_xml_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].\
                                        lower() in ALLOWED_XML_EXTENSION


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
    # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if file.filename.rsplit('.', 1)[1].lower() in ['xml']:
                file.save(os.path.join(app.config['UPLOAD_XML_FOLDER'],
                                                                    filename))
            else:
                file.save(os.path.join(app.config['UPLOAD_IMG_FOLDER'],
                                                                    filename))
            flash('File successfully uploaded')
            return redirect('/')
        else:
            flash('Allowed file types are xml, png, jpg, jpeg')
            return redirect(request.url)


@app.route('/parse_xml')
def upload_xml_form():
    return render_template('parse_xml.html')


@app.route('/parse_xml', methods=['POST'])
def parse_file():
    if request.method == 'POST':
    # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for parsing')
            return redirect(request.url)
        if file and allowed_xml_file(file.filename):
            filename = secure_filename(file.filename)
            parse_xml(os.path.join(app.config['UPLOAD_XML_FOLDER'], filename))
            return redirect(request.url)
        else:
            flash('Allowed file type is xml')
            return redirect(request.url)


@app.route('/plot_png')
def upload_plot_form():
    return render_template('plot_png.html')

@app.route('/plot_png', methods=['GET','POST'])
def plot_file():
    if request.method == 'POST':
    # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for plotting')
            return redirect(request.url)
        if file and allowed_img_file(file.filename):
            filename = secure_filename(file.filename)
            txt_name = filename.rsplit('.', 1)[0] + '.txt'
            xml_name = filename.rsplit('.', 1)[0] + '.xml'
            
            img_path = os.path.join(app.config['UPLOAD_IMG_FOLDER'], filename)
            txt_path = os.path.join(app.config['UPLOAD_TXT_FOLDER'], txt_name)
            xml_path = os.path.join(app.config['UPLOAD_XML_FOLDER'], xml_name)
            
            fig = draw_bounding_box(img_path, txt_path, xml_path)
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            return Response(output.getvalue(), mimetype = 'image/png')
            #return redirect(request.url)
        else:
            flash('Allowed file types are jpg, jpeg and png')
            return redirect(request.url)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8085, debug = True)