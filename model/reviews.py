""" database dependencies to support sqliteDB examples """
from random import randrange
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


# Define the Score class to manage actions in the 'score' table
class Review(db.Model):
    __tablename__ = 'reviews' 

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _school = db.Column(db.String(255), unique=False, nullable=False)
    _review = db.Column(db.Text, unique=True, nullable=False)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, school, review):
        self._school = school    # variables with self prefix become part of the object, 
        self._review = review

    # a name getter method, extracts name from object
    @property
    def school(self):
        return self._school
    
    # a setter function, allows name to be updated after initial object creation
    @school.setter
    def school(self, school):
        self._school = school
    
    @property
    def score(self):
        return self._review
    
    @score.setter
    def score(self, review):
        self._review = review
        
    def is_review(self, review):
        return self._review == review
    
    @property
    def __str__(self):
        return json.dumps(self.read())

    def create(self):
        try:
            # creates a person object from Score(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "school": self.school,
            "review": self.review
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, school="", review=""):
        """only updates values with length"""
        if len(review) > 0:
            self.review = review
        if len(review) > 0:
            self.review = review
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

"""Database Creation and Testing """

def initReviews():
    with app.app_context():
        """Create database and tables"""
        # db.init_app(app)
        db.create_all()
        """Tester data for table"""
        u1 = Review(school='UCSD', review='Socially dead :(')
        u2 = Review(school='UCSD', review='Great engineering program')
        u3 = Review(school='UCI', review='Go anteaters!!!!!!!!!')
        u4 = Review(school='UCM', review='Nothing fun to do at all around.')
        u5 = Review(school='UCSB', review='Party School!!!!')

        users = [u1, u2, u3, u4, u5]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                '''add a few 1 to 4 notes per user'''
                for num in range(randrange(1, 4)):
                    note = "#### " + user.school + " note " + str(num) + ". \n Generated by test data."
                '''add user/post data to table'''
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.review}")