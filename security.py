# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:58:53 2021

@author: moham
"""

from models.user import UserModel
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_userid(user_id)