# PROBLEM----make a qr code to any given web link
import qrcode as qr
# make qr for given website
image = qr.make("https://www.youtube.com/c/wscubetechjodhpur")
# save the png image to given path
image.save("wscube_youtube.png")
