from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
import re

from config import bcrypt, db

class Location(db.Model, SerializerMixin):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String, nullable=False)
    # image = db.Column(db.String)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String)
    country = db.Column(db.String, nullable=False)

    routes = db.relationship('Route', backref='location')
    serialize_rules = ('-routes',)

    @validates('place')
    def validate_place(self, key, value):
        if not value:
            raise ValueError('Place must be provided')
        return value
    @validates('city')
    def validate_city(self, key, value):
        if not value:
            raise ValueError('City must be provided')
        return value
    @validates('country')
    def validate_country(self, key, value):
        if not value:
            raise ValueError('Country must be provided')
        return value


class Route(db.Model, SerializerMixin):
    __tablename__ = 'routes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    style = db.Column(db.String, nullable=False)
    grade = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    
    #reviews = db.relationship('Review', backref='route', primaryjoin='Review.route_id == Route.id')
    reviews = db.relationship('Review', backref='route')
    climbers = association_proxy('reviews', 'climber')
    serialize_rules = ('-reviews', 'location')
    

    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError('Route name must be provided')
        return value
    @validates('style')
    def validate_style(self, key, value):
        if not value:
            raise ValueError('Style must be provided')
        return value
    @validates('grade')
    def validate_grade(self, key, value):
        if not value:
            raise ValueError('Grade must be provided')
        return value

    # def to_dict(self):
    #     return SerializerMixin.to_dict(self)

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    star_rating = db.Column(db.Integer, nullable=False)
    safety_rating = db.Column(db.Integer, nullable=False)
    quality_rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    climber_id = db.Column(db.Integer, db.ForeignKey('climbers.id'))
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id'))

    serialize_rules = ('-climber', '-route', '-created_at', '-updated_at')


    @validates('star_rating')
    def validate_star_rating(self, key, value):
        if not value:
            raise ValueError('Star rating must be provided')
        return value
    @validates('safety_rating')
    def validate_safety_rating(self, key, value):
        if not value:
            raise ValueError('Safety rating must be provided')
        return value
    @validates('quality_rating')
    def validate_quality_rating(self, key, value):
        if not value:
            raise ValueError('Quality rating must be provided')
        return value


class Climber(db.Model, SerializerMixin):
    __tablename__ = 'climbers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    admin = db.Column(db.String, default=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)

    reviews = db.relationship('Review', backref='climber')
    routes = association_proxy('reviews', 'route')
    serialize_rules = ('-reviews',)

    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    @validates('username')
    def validate_username(self, key, username):
        climbers = Climber.query.all()
        usernames = [climber.username for climber in climbers]
        if not username:
            raise ValueError('Username must be provided')
        elif username in usernames:
            raise ValueError('Username already exists')
        elif len(username) < 3:
            raise ValueError('Username must be at least 3 characters long.')
        return username
    @validates('email')
    def validate_email(self, key, email):
        climbers = Climber.query.all()
        emails = [climber.email for climber in climbers]
        if not email:
            raise ValueError('Email must be provided')
        elif email in emails:
            raise ValueError('Email already exists')
        elif not re.search('@', email):
            raise ValueError('Must be a valid email')
        return email

    @validates('password')
    def validate_password(self, key, password):
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        elif not re.search('[!@#$%^&*]', password):
            raise ValueError('Password must contain at least one special character.')
        return password
        
    @validates('first_name')
    def validate_first_name(self, key, value):
        if not value:
            raise ValueError('First name must be provided')
        return value
    
    def __repr__(self):
        return f'CLIMBER: ID: {self.id}, Name {self.first_name}, Username: {self.username}, Admin: {self.admin}'
    


