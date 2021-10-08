import qrcode
# example of data
data = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# name of the final file
filename = "QR code.png"
# generating QR code
img = qrcode.make(data)
# save img into the file
img.save(filename)
