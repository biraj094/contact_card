from flask import Flask,render_template
from qr import getdata,qrfunc

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/display',methods=['POST','GET'])
def display():
    n=getdata()
    qrimage=qrfunc(n)
    return render_template('display.html')


if __name__=='__main__':
    app.run(debug=True)