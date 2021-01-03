import qrcode

def qrfunc(link):
    qr=qrcode.QRCode(version=20,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=15, border=10  )
    qr.add_data(link)
    qr.make(fit=True)
    img=qr.make_image(fill="black",back_color="white")
    print(type(img))
    return img





    

    

