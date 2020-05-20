from flask import Flask,render_template , request,send_file
from qr import getdata,qrfunc
import io
from tempfile import NamedTemporaryFile


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/display',methods=['POST','GET'])
def display():
    link = request.form['n']
    return render_template('display.html', link=link )

@app.route('/download/<path:link>',methods=['POST','GET'])
def download(link):
    link=link
    qrimage=qrfunc(link)
    filename='image.png'
    with NamedTemporaryFile(delete=True) as tmp:
        qrimage.save(tmp.name)
        str_io = io.BytesIO(tmp.read())
    return send_file(str_io,
                 attachment_filename=filename,
                 mimetype='image/png',
                 as_attachment=True)


if __name__=='__main__':
    app.run(debug=True)