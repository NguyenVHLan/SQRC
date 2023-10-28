import qrcode
import os

def generate_qr_code(data,id):
    # Tạo ảnh từ mã QR code
    qr = qrcode.QRCode(version=40, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    # Kiểm tra thư mục nếu ko có thì tạo
    image_name = f"qrcode_{id}.png"
    if not os.path.exists(f"uploads/{id}"):
        os.makedirs(f"uploads/{id}")
    # Lưu ảnh
    qr_image.save(f"uploads/{id}/{image_name}")
