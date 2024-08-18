from flask import Blueprint, render_template, jsonify
from app.database import db
from app.models import Test

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/test_db')
def test_db():
    try:
        # Testa se a conexão ao banco de dados está funcionando
        db.create_all()  # Cria as tabelas se não existirem
        test_entry = Test(name="Test")
        db.session.add(test_entry)
        db.session.commit()
        return jsonify({'message': 'Database connection is working!'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500