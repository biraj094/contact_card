from flask import request
import qrcode
from flask import send_file
from PIL import Image

def getdata():
    name=request.form['n']
    return name

def qrfunc(data):
    qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=15, border=10  )
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill="black",back_color="white")

    #TODO: want to generate the image and be able to download it withour saving it anywhere
    #TODO: download can be done by pressing the button 
    #TODO: Be able to name the file 
    #TODO:  
    jpgfile = Image.open(img)
    filename='image.png'

    # img.save('/Users/apple/Desktop/Biraj/Contact card/static/images/YourContactCard.png')
    return send_file(jpgfile,
                 attachment_filename=filename,
                 mimetype='image/png',
                 as_attachment=True)

    

