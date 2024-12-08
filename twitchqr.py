# Importing library
import qrcode

# Data to encode
data = "https://twitch.tv/giggleoutloudband"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version=1,
                   box_size=80,
                   border=5)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color='#663399',
                    back_color='white')

img.save('gol_twitch.png')
