from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    get_jwt,
    jwt_required,
)
from blocklist import BLOCKLIST
from flask_cors import CORS
from flask import request,send_file
import os,cv2
import numpy as np

from func.genqrcode import generate_qr_code
from func.aes import encrypt
from func.zip import compress_and_encode_data

blp = Blueprint("Images", "images", description="upload image")
CORS(blp)


@blp.route("/uploads/<int:id>", methods=["POST"])
def post(id):
    if "file" not in request.files:
        return {"message":"No file attached"}, 400

    file = request.files["file"]

    # Kiểm tra xem file có phải là file ảnh hay không
    if not file.filename.endswith((".jpg", ".jpeg", ".png", ".BMP", ".bmp",".JPG",".JPEG",".PNG")):
        return {"message":"Invalid file format. Only JPG, JPEG, BMP and PNG are supported."}, 400

    # Đọc file ảnh sử dụng OpenCV
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)

    # Tạo đối tượng SIFT
    sift = cv2.SIFT_create()

    # Trích xuất đặc trưng từ ảnh
    keypoints, descriptors = sift.detectAndCompute(image, None)
    # Nén và dữ liệu đặc trưng
    compressed_data = compress_and_encode_data(keypoints, descriptors)
    # Mã hóa dữ liệu bằng AES
    key = b'\xc2\xe2\xa8B\xf8#\x87\xe5\xe5\x9d\xee\xdc5\t\xf6\xe1/\x9af\x1c\xef\rP1\xce\xe1`\xa1\x89\x83C]'
    iv =b'1234567891234567'
    encrypted_user_id=encrypt(str(id).encode('utf-8'), key,iv)
    encrypted_compressed_data = encrypt(compressed_data, key,iv)
    qr_code_data = encrypted_user_id.decode() + '.' + encrypted_compressed_data.decode()

    print(qr_code_data)
    # Tạo qrcode
    generate_qr_code(qr_code_data,id)

    return {"message": "Create SQRC successfully"}, 201

@blp.route("/qrcode/<int:id>")   
def get_qrcode(id):
    path = f"uploads/{id}/qrcode_{id}.png"
    if not os.path.exists(path):
        return {"message": "File not found"}, 404
    return send_file(path)

        