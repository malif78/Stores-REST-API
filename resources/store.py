# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 23:07:31 2021

@author: moham
"""

from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
     
    
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.myjson()
        else:
            return {'message':"Store not found"}, 404
    
    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message':'Store with the given name already exists'}
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'An error occired while creating the store'},500
        return store.myjson(), 201
    
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message':'store deleted'}
    
class Store_list(Resource):
    def get(self):
        return {'stores':[store.myjson() for store in StoreModel.query.all()]}



