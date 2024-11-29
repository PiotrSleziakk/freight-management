from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash  # Haszowanie haseł
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)  # Akceptacja żądań z dowolnego źródła
#CORS(app, resources={r"/*": {"origins": "http://192.168.0.213:8080"}}, supports_credentials=True)  # Tylko frontend

@app.before_request
def handle_preflight():
    if request.method == 'OPTIONS':
        # Ręczna obsługa preflight request
        response = app.make_response('')
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        return response


# Konfiguracja połączenia z PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/freight_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Ustal tajny klucz dla JWT
db = SQLAlchemy(app)
jwt = JWTManager(app)  # Inicjalizacja JWT


# Model użytkownika
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Endpoint główny
@app.route('/', methods=['GET'])
def home():
    return jsonify({"msg": "Witaj w aplikacji Freight Management!"}), 200

# Endpoint do logowania (generowanie tokenu JWT)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):  # Sprawdzanie hasła
        token = create_access_token(identity=user.id)  # Tworzenie tokenu JWT
        return jsonify(access_token=token), 200
    else:
        return jsonify({"msg": "Invalid credentials"}), 401  # Błąd logowania


# Endpoint do rejestracji użytkownika
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"msg": "Brak danych w żądaniu!"}), 400

    print("Odebrane dane:", data)  # Debugowanie danych
    username = data.get('username', '')
    email = data.get('email', '')
    password = data.get('password', '')
    confirm_password = data.get('confirm_password', '')

    # Sprawdzenie, czy hasła się zgadzają
    if password != confirm_password:
        return jsonify({"msg": "Hasła muszą być takie same!"}), 400

    # Sprawdzenie, czy użytkownik już istnieje
    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Użytkownik o tej nazwie już istnieje!"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "Użytkownik o tym emailu już istnieje!"}), 400

    # Haszowanie hasła przed zapisaniem w bazie danych
    hashed_password = generate_password_hash(password)

    print(f"Dane otrzymane: {data}")  # Debugowanie
    print(f"Hashed password: {hashed_password}")

    # Tworzenie nowego użytkownika
    new_user = User(username=username, email=email, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        print(f"Użytkownik {new_user.username} został utworzony.")
        return jsonify({"msg": "User registered successfully"}), 201
    except Exception as e:
        db.session.rollback()
        print(f"Błąd podczas zapisu do bazy: {e}")  # Szczegółowy log błędu
        return jsonify({"msg": "Błąd serwera. Spróbuj ponownie później."}), 500


# Endpoint do pobierania użytkowników (wymaga tokenu)
@app.route('/users', methods=['GET'])
@jwt_required()  # Wymaga autentykacji JWT
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])


# Główna funkcja do uruchamiania aplikacji i inicjalizacji bazy danych
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Tworzenie tabel w bazie danych
        print("Tabele w bazie danych zostały utworzone.")
    app.run(debug=True)
