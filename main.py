import qrcode
url=qrcode.QRCode(version=1, box_size=40,border=3)
url.add_data(" paste your url here")
url.make(fit=True)
generate_image = url.make_image(fill_color="black", back_clolor="white")
generate_image.save("image.png")