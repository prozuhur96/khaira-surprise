import qrcode

card_url = "https://prozuhur96.github.io/khaira-surprise/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(card_url)
qr.make(fit=True)

img = qr.make_image(fill_color="#d81b60", back_color="#ffffff")

img.save("khaira_1month.png")

print("QR Code generated successfully!")