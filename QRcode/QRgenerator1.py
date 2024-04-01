import qrcode
""" Python Imaging Library (PIL) is a library used for opening, manipulating, and saving many different image file formats. 
It provides functionalities for tasks such as resizing, cropping, rotating, filtering, and blending images."""
from PIL import Image
qr = qrcode.QRCode(version=1,      # QRCode function--- change the given qrcode ---like change border -color-size
                   # for removing error---(only remove high level error)high level error--H
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4,)
# given website -- for make qr
qr.add_data("https://www.wscubetech.com/")
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="pink")
img.save("wscube_web.png")
