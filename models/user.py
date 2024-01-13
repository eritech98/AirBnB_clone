#!/usr/bin/python3

"""
Has the class UseR
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class USERser that inherits from BaseModel.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
