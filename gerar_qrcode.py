import qrcode
from PIL import Image

url = input("Enter URL: ").strip()
output = input("Output filename (without extension): ").strip() or "qrcode"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
img.save(f"{output}.jpg", "JPEG", quality=95)

print(f"QR code saved as {output}.jpg")
