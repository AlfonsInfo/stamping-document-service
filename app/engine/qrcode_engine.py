import qrcode
from io import BytesIO
import base64

def generate_base64_qr(data):
    try:
        qr = qrcode.main.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=0,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Buat gambar QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Simpan gambar ke dalam buffer
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        # Konversi gambar ke base64
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    except Exception as e:
        print(e)
        raise
    return img_str