""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash



## INPUTTED WORKOUT CLASS


class Colleges(db.Model):
    __tablename__ = 'Colleges'

    # Define the workout schema
    id = db.Column(db.Integer, primary_key=True)
    _uid = db.Column(db.String(255), unique=True, nullable=False)
    _college = db.Column(db.Text, unique=False, nullable=False)
    _city = db.Column(db.Integer, unique=False, nullable=False)
    _rate = db.Column(db.Integer, unique=False, nullable=False)

    

    # Constructor of a Inputworkout object, initializes of instance variables within object
    def __init__(self, id, uid, college, city, rate):
        self.userID = id
        self._uid = uid
        self.college = college
        self.city = city
        self.rate= rate


    @property
    def uid(self):
        return self._uid
    
    
    @uid.setter
    def uid(self, uid):
        self._uid = uid
        
    def is_uid(self, uid):
        return self._uid == uid


    @property
    def college(self):
        return self._college
    
    # a setter function, allows exercise name to be updated after initial object creation
    @college.setter
    def college(self, college):
        self._exerciseType = college


    @property
    def city(self):
        return self._city
    
    @city.setter
    def sets(self, city):
        self._city = city


    @property
    def rate(self):
        return self._rate
    
    
    @rate.setter
    def reps(self, rate):
        self._rate = rate

    
    # CRUD create, adds a new record to the Collegesp table
    def create(self):
        try:
            # creates a workout object from College(db.Model) 
            db.session.add(self)  
            db.session.commit()  
            return self
        except IntegrityError:
            db.session.remove()
            return None

  
    def read(self):
        
        return {
            "id": self.id,
            "uid": self.uid,
            "college": self.college,
            "city": self.city,
            "rate": self.rate
        }
    
    def update(self,sets=""):
        """only updates values with length"""
        if len(sets) > 0:
            self.sets = sets
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
    

def initColleges():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        i1 = Colleges(college='USCD', id='ucsd', uid='ucsd1', city='San Diego', rate='34%')
        i2 = Colleges(college='UCSC', id='ucsc', uid='ucsc1', city='Santa Cruz', rate='52%')
        i3 = Colleges(college='UCLA', id='ucla', uid='ucla1', city='Los Angeles', rate='12%')
        i4 = Colleges(college='UC Davis', id='ucdavis', uid='ucdavis1', city='LA', rate='46%')
        
        colleges = [i1, i2, i3, i4]

       # """Builds sample college/note(s) data"""
        for college in colleges:
            try:
                '''add a few 1 to 4 notes per user'''
                for num in range(randrange(1, 4)):
                #  note = "#### " + user.college + " note " + str(num) + ". \n Generated by test data."
                    '''add inputted workout data to table'''
                college.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"ERROR {Colleges.id}")
