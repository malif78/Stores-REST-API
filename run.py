# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 16:15:40 2021

@author: moham
"""


from app import app
from db import db

db.init_app(app)