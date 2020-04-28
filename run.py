from flask import Flask,render_template
from qr import getdata,qrfunc
import io
from tempfile import NamedTemporaryFile
# import Image
from PIL import Image
from flask import send_file
from flask import Response

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/display',methods=['POST','GET'])
def display():
    link=getdata()
    qrimage=qrfunc(link)

    with NamedTemporaryFile(delete=True) as tmp:
        qrimage.save(tmp.name)
        str_io = io.BytesIO(tmp.read())
    # trial = qr
    # return Response(str_io.getvalue(), mimetype='image/png')
    # final= qrimage.show()
    # return render_template('display.html',qrimage=qrimage)
    return render_template('display.html', link=link ,qrimage=str_io )

@app.route('/download/<link>',methods=['POST','GET'])
def download(link):
    linkk=link
    qrimage=qrfunc(linkk)
    filename='image.png'
    with NamedTemporaryFile(delete=True) as tmp:
        qrimage.save(tmp.name)
        str_io = io.BytesIO(tmp.read())

    # img.save('/Users/apple/Desktop/Biraj/Contact card/static/images/YourContactCard.png')
    return send_file(str_io,
                 attachment_filename=filename,
                 mimetype='image/png',
                 as_attachment=True)

    # return render_template('display.html', qrimage=qrimage)


# @app.route('/download<qrimage>', methods=['GET'])
# def download(qrimage):
#     filename='image.png'


#     im = Image.open(qrimage,'r')
#     with NamedTemporaryFile(delete=True) as tmp:
#         im.save(tmp.name)
#         str_io = io.BytesIO(tmp.read())

#     # img.save('/Users/apple/Desktop/Biraj/Contact card/static/images/YourContactCard.png')
#     return send_file(str_io,
#                  attachment_filename=filename,
#                  mimetype='image/png',
#                  as_attachment=True)


if __name__=='__main__':
    app.run(debug=True)