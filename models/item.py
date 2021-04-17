# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 15:55:33 2021

@author: moham
"""


#import sqlite3
from db import db

class ItemModel(db.Model):   
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))   
    
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
        
    def myjson(self):
        return {'name':self.name, 'price':self.price, 'store':self.store_id}
    

    @classmethod 
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
 
    def save_to_db(self):        
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self,name):            
        db.session.delete(self)
        db.session.commit()