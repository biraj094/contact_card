from flask import Flask,render_template , request,send_file
from qr import qrfunc
import io
from tempfile import NamedTemporaryFile


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/display',methods=['POST','GET'])
def display():
    link = request.form['link']
    return render_template('display.html', link=link )

@app.route('/download/<path:link>',methods=['POST','GET'])
def download(link):
    link=link
    qrimage=qrfunc(link) 
    with NamedTemporaryFile(delete=True) as tmp:
        qrimage.save(tmp.name)
        str_io = io.BytesIO(tmp.read())
    filename="image.png"
    if request.method == "POST":
        filename = "image.png" 
        filename_byuser = request.form['filename'] + ".png"
        if len(filename_byuser)>4:
            filename = filename_byuser
    return send_file(str_io,
                 attachment_filename=filename,
                 mimetype='image/png',
                 as_attachment=True)


if __name__=='__main__':
    app.run(debug=True)