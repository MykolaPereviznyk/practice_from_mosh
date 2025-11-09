import qrcode

input_user = str(input("Enter the text or URL: ")).strip()
input_name = str(input("Enter the filename: ")).strip()


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2,
)

qr.add_data(input_user)
qr.make(fit=True)

img = qr.make_image(fill_color="purple", back_color="black")

img.save(input_name + '.png')

print(f"QR code saved as {input_name}" + ".png")
