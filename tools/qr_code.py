import qrcode

link = "https://www.google.com/maps/search/?api=1&query=Monk%27s+Nirvanaa+Hotel+%26+Resort%2C+Indore%2C+Madhya+Pradesh"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qr_code.png")

print("Vanshika & Naman Wedding Invitation QR Code generated successfully!")
