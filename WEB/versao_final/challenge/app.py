import os
import sqlite3
from base64 import b64encode
from hashlib import md5
from flask import Flask, g, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'L137tCDwqvT3OdliaOxoW73EMWc70XzP'
app.config['MAX_CONTENT_LENGTH'] = 1000

DATABASE = 'db.sqlite'
UPLOAD_FOLDER = './TEMP/'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def secure_filename(filename):
    filename = filename.replace('/', '')
    filename = filename.split('.')
    if len(filename) == 2:
        return filename[0]+'.'+filename[1]
    return False

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        if 'file' not in request.files:
            flash('No file')
            return redirect(url_for('upload'))

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('upload'))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if filename is False:
                flash('Filename not allowed')
                return redirect(url_for('upload'))

            ip = md5(request.remote_addr.encode()).hexdigest()
            if os.path.isdir(UPLOAD_FOLDER+ip):
                file.save(os.path.join(UPLOAD_FOLDER+ip, filename))
            else:
                os.mkdir(UPLOAD_FOLDER+ip)
                file.save(os.path.join(UPLOAD_FOLDER+ip, filename))

            with sqlite3.connect(DATABASE) as conn:
                conn.execute("INSERT INTO images (ip, name) VALUES ('" + ip + "', '" + filename + "');")
                conn.commit()

            return redirect(url_for('upload'))

        flash('Extension not allowed')
        return redirect(url_for('upload'))

@app.route('/preview/<folder>/<image_name>', methods=['GET'])
def preview(folder, image_name):
    if os.path.exists(UPLOAD_FOLDER+folder+'/'+image_name):
        file = b64encode(open(UPLOAD_FOLDER+folder+'/'+image_name, 'rb').read()).decode()
        return render_template('preview.html', content=file)
    return render_template('index.html')

@app.route('/list', methods=['GET'])
def list():
    ip = md5(request.remote_addr.encode()).hexdigest()

    with sqlite3.connect(DATABASE) as conn:
        results = conn.execute("SELECT name FROM images WHERE ip='" + ip + "'").fetchall()
    
    if results:
        images_name = [name[0] for name in results]
        return render_template('list.html', content=images_name, ip=ip)

    return render_template('index.html')

        
if __name__ == "__main__":
    app.run()
