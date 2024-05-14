import qrcode
import base64
from io import BytesIO

def generate_qr(data):
    qr = qrcode.QRcode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=4,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()

    img.save(BytesIO(), format='PNG')
    img_str = base64.b64encode(BytesIO().getvalue()).decode('uft-8')
    print(img_str)
    retrun img_str

print(generate_qr("1234456789"))