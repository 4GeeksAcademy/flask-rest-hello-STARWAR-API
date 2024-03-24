"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Favorites, Planet, People
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Mostrar lista de users
@app.route("/user", methods=['GET'])
def get_all_user():
    people =User.query.all()
    return jsonify(people), 200

# Mostrar todos lo favoritos
@app.route("/user/favorites", methods=["GET"])
def get_all_favorites():
    favorites = Favorites.query.all()
    return jsonify (favorites), 200

# Mostrar lista de personajes
@app.route("/people", methods=['GET'])
def get_all_people():
    people =People.query.all()
    return jsonify(people), 200

# Mostrar lista de planetas
@app.route("/planet", methods=['GET'])
def get_all_planet():
    planet =People.query.all()
    return jsonify(planet), 200
    
# Muestra personaje segun su UID
@app.route("/people/<int:people_id>")
def find_people_by_id(people_id):
    people = People.query.filter_by(id = people_id).one_or_none()
    find_people = [people.serialize() for character in people]

    if find_people:
        return jsonify(find_people), 200
    else:
        return jsonify({"Error": "character not found"}), 404

# Muestra planeta segun su UID
@app.route("/planet/<int:planet_id>")
def find_planet_by_id(planet_id):
    planet = Planet.query.filter_by(id = planet_id).first()
    if planet:
        return jsonify(planet), 200
    else:
        return jsonify({"Error": "planet not found"}), 404

# Crear Usuario
@app.route("/create/user", methods = ['POST'])
def new_user():
    body = request.json
    email = body.get('email')
    password = body.get('password')
    is_active = True 

    new_user = User(email = email, password = password, is_active = is_active)

    db.session.add(new_user)
    try: 
        db.session.commit()
        return 'User created', 200
    except Exception as error:
        db.session.rollback()
        return 'error had ocurred', 400
    

# Crear un planeta
@app.route('/create/planet', methods = ['POST'])
def new_planet():
    body = request.json
    name = body.get('name')
    src = body.get('src')
    description = body.get('descripton')

    new_planet = Planet(name = name, src=src, description=description)

    db.session.add(new_planet)
    try:
        db.session.commit()
        return 'planet created', 200
    except Exception as error:
        db.session.rollback()
        return 'error had ocurred', 500
    
# Crear un personaje  
@app.route('/create/people', methods = ['POST'])
def new_people():
    body = request.json
    name = body.get('name')
    src = body.get('src')
    description = body.get('description')

    new_people = People(name = name, src = src, description = description)

    db.session.add(new_people)
    try:
        db.session.commit()
        return 'Character created', 200
    except Exception as error:
        db.session.rollback()
        return 'error had occured', 500

# Agregar personaje a favorito
@app.route('/favorites/people/<int:people_id>', methods = ['POST'])
def add_favorite_people(people_id):
    body = request.json
    user_id = body.get('user_id')

    if user_id is None:
        return jsonify({'Error': 'user id and people id is required'})
    
    new_favorite_people = Favorites(user_id = user_id, people_id = people_id)

    db.session.add(new_favorite_people)
    try:
        db.session.commit()
        return 'A character was added to your favorites', 200
    except Exception as error:
        db.session.rollback()
        return 'there was an error', 500
    
# Agregar un planeta a favoritos
@app.route('/favorites/planet/<int:planet_id>', methods = ['POST'])
def add_favorites_planet(planet_id):
    body =  request.json
    user_id = body.get(user_id)

    if user_id is None:
        return jsonify({'Error': 'user id and planet id are need it'})
    
    new_favorites_planet = Favorites(user_id = user_id, planet_id = planet_id)

    db.session.add(new_favorites_planet)
    try:
        db.session.commit()
        return 'A planet was add to yours favorites', 200
    
    except Exception as error:
        db.session.rollback()
        return 'there was an error', 500
    

# Eliminar un planeta de los favoritos
@app.route('/favorite/planet/<int:planet_id>')
def delete_favorite_planet(planet_id):
    favorite_filter = Favorites.query.filter_by(id = planet_id).one_or_none()

    if favorite_filter is None:
        return jsonify({'error': 'favorite not found'}), 404
    
    db.session.delete(favorite_filter)
    try:
        db.session.commit()
        return jsonify({'response': 'favorite was delete'}), 200
    except Exception as error:
        return jsonify({'error': 'there was an error'}), 500



    


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
