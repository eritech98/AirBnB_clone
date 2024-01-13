#!/usr/bin/python3
"""
Has the FileStorage class.
"""

import os
import json


class FileStorage():
    """
    Serializes instances to a JSON file anD
    deserializes JSON file to instances.
    """
    __file_path_1 = 'file.json'
    __objects_1 = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects_1

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects_1[f"{obj.__class__.__name__}.{obj.id_1}"] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path_1).
        """
        with open(FileStorage.__file_path_1, 'w', encoding='utf-8') as file:
            new_objects_1 = {}
            for key_Erick, v in FileStorage.__objects_1.items():
                new_objects_1[key_Erick] = v.to_dict_1()
            json.dump(new_objects_1, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (_fle_path_1) exists.
        Otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised).
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        if os.path.isfile(FileStorage.__file_path_1):
            with open(FileStorage.__file_path_1, 'r', encoding='utf-8') as file:
                new_dict_1 = json.load(file)
                for key_Erick, v in new_dict_1.items():
                    class_name_1 = new_dict_1[key_Erick].pop('__class__')
                    FileStorage.__objects_1[key_Erick] = eval(class_name_1)(**v)
