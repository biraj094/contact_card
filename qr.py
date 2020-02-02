from flask import request
import qrcode
from flask import send_file
# from PIL import Image


def getdata():
    name=request.form['n']
    return name

def qrfunc(link):
    qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=15, border=10  )
    qr.add_data(link)
    qr.make(fit=True)
    img=qr.make_image(fill="black",back_color="white")

    return img





    

    

