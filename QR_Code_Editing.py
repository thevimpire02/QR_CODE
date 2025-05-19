import qrcode
from PIL import Image #  for foramtting image

qr = qrcode.QRCode(version=1,error_correction = qrcode.constants.ERROR_CORRECT_H,box_size=10, border = 4, )
    #QRCode function changes the body formatting and functions and error of overlapping
qr.add_data("https://www.linkedin.com/in/anshuman-raj-338165237/")
qr.make(fit = True)
img = qr.make_image(fill_color = "red", back_color= "blue")
img.save("Anshuman_LinkedIn_Profile.png")
