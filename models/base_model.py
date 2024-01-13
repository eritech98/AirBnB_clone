#!/usr/bin/python3
"""
Has the Base Classs
"""

import datetime
import uuid
from models import storage


class BaseModel():
    """
    Defines all the  common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if len(kwargs) == 0:
            storage.new(self)
        elif len(kwargs) > 0:
            for key_Erick, v in kwargs.items():
                if key_Erick == '__class__':
                    continue
                if key_Erick in ('created_at', 'updated_at'):
                    v = datetime.datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__[key_Erick] = v

    def __str__(self):
        """
        Called when a Base Object is caLLed.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instanCE attribute \
        updated_at with the CuRRent datetime.
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict_1(self):
        """
        Returns a dictionary containing all keys/values \
            of __dict__ of the instance.
        """
        new_dict_1 = self.__dict__.copy()
        new_dict_1['__class__'] = self.__class__.__name__
        new_dict_1['created_at'] = self.created_at.isoformat()
        new_dict_1['updated_at'] = self.updated_at.isoformat()
        return new_dict_1
