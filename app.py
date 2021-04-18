# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 00:04:57 2021

@author: moham
"""
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Item_list
from resources.store import Store, Store_list
#from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Mohammed"
api = Api(app)

#@app.before_first_request
#def create_tables():
#    db.create_all()

jwt = JWT(app, authenticate, identity)

  
    
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Item_list, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Store_list, '/stores')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)