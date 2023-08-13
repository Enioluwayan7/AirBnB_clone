#!/bin/usr/python3
'''class inherit from BaseModel'''
from models.base_model import BaseModel

class Review(BaseModel):
    '''class Review'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initialize Review"""
        super().__init__(*args, **kwargs)
