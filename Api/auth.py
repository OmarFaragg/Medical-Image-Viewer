from flask import Blueprint, request, jsonify
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.json.get('email')
        password = request.json.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return jsonify({"status": "success"})
        return jsonify({"status": "error", "message":"Wrong email or password"})
    return

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return

@auth.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        name = request.json.get('name')
        password = request.json.get('password')
        email = request.json.get('email')
        new_user = User(name=name, password=generate_password_hash(password, method='pbkdf2'), email=email)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        return {"status": "success"}
    return