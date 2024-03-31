from flask import Blueprint, request, send_file
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet
import os, io
from flask_login import login_required, current_user
from . import db 
from .models import User, MedicalImage

views = Blueprint('views', __name__)

def encrypt_file(file_data, key):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(file_data)

def decrypt_file(encrypted_data, key):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_data)

@views.route('/', methods=['GET'])
def home():
    return "home"

@views.route('/upload', methods=['POST'])
@login_required
def upload_file():
    from main import app
    file = request.files['file']
    user_id = current_user.id
    key = current_user.password.encode()
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file_data = file.read()
        # Encrypt the file content
        encrypted_data = encrypt_file(file_data, key)
        
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)        
        medical_images = MedicalImage(file_path=file_path, user_id=user_id)
        db.session.add(medical_images)
        db.session.commit()
        
        return 'File uploaded successfully'
    else:
        return 'No file uploaded'

@views.route('/view/<file_id>', methods=['GET'])
@login_required
def download_file(file_id):
    medical_image = MedicalImage.query.filter_by(id=file_id).first()
    if medical_image.user_id != current_user.id:
        return "No access"
    file_path = medical_image.file_path
    key = current_user.password.encode() 
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Decrypt the file content
    decrypted_data = decrypt_file(file_data, key)
    
    return send_file(io.BytesIO(decrypted_data), as_attachment=True, attachment_filename=file_path.split("/")[-1])

