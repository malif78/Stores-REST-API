# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 21:52:21 2021

@author: moham
"""

from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot left blank"
    )
    parser.add_argument('store_id',
            type=int,
            required=True,
            help="Store id is mandatory"
    ) 
       
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.myjson(),200
        return {"message":"item not found"},404
                        
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message':'item already exists'},400   
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])    
        try:
            item.save_to_db()
        except: 
            return {"message", "an error occured while inserting the iterm"},500
        return item.myjson(),201
                   
            
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)        
        if item:   
            item.price = data['price']
            item.store_id = data['store_id']
        else:
            item = ItemModel(name, data['price'], data['store_id']) 
        
        item.save_to_db()
        
        return item.myjson()
    

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            try:
                item.delete_from_db(name)
            except:
                return {"message", "an error occured while updating the iterm"},500
            return {"message":"item deleted"},201
        else:
            return {'message':'item does not exist'}



class Item_list(Resource):
    def get(self):
        return {'items':[item.myjson() for item in ItemModel.query.all()]}
          
       
      
