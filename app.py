import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image, ImageFilter
from evaluate import ffwd_to_img


UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = set(['jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filename_out = 'out.jpg'
            ffwd_to_img(filename, filename_out, request.form['checkpoint'])
            return redirect(url_for('uploaded_file',
                                    filename=filename_out))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
          <select name="checkpoint">
              <option value="models/udnie.ckpt">Udnie</option>
              <option value="models/la_muse.ckpt">La Muse</option>
              <option value="models/rain_princess.ckpt">Rain Princess</option>
              <option value="models/scream.ckpt">Scream</option>
              <option value="models/wave.ckpt">Wave</option>
              <option value="models/wreck.ckpt">Wreck</option>
          </select> 
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == "__main__":
    app.run()
