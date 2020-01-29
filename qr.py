from flask import request
import qrcode

def getdata():
    name=request.form['n']
    return name

def qrfunc(data):
    qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=15, border=10  )
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill="black",back_color="white")
    img.save('/Users/apple/Desktop/Biraj/Contact card/static/images/YourContactCard.png')
    return True
    

