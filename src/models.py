from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorites')

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "favorites": self.favorites
            # do not serialize the password, its a security breach
        }
    

class Favorites(db.Model):
    # Parent
    __tablename__ = "favorites"
    fav_id= db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable = False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable = False)


    def serialize(self):
        return{
            "fav_id":self.fav_id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "people_id": self.people_id
            
        }

class Planet(db.Model):
    __tablename__ = "planet"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    src = db.Column(db.String(500), nullable = False)
    description = db.Column(db.String(500), nullable = False)
    favorites = db.relationship("Favorites")
    

    def serialize(self):
        return{
            "id":self.id,
            "name": self.name,
            "src": self.src,
            "description": self.description,
            "favorites": self.favorites
        }


class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    src = db.Column(db.String(300), nullable = False)
    description = db.Column(db.String(500), nullable = False)
    favorites = db.relationship("Favorites")

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "src": self.src,
            "description": self.description,
            "favorites": self.favorites
        }


