#!/usr/bin/python3
"""Base mudole"""
import uuid
import json
import datetime


class BaseModel:
    """define Base class"""

    def __init__(self):
        """initailize instances"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """print class information"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        base_dict = dict(self.__dict__)
        base_dict['__class__'] = type(self).__name__
        base_dict['created_at'] = base_dict['created_at'].isoformat()
        base_dict['updated_at'] = base_dict['updated_at'].isoformat()
        return base_dict
