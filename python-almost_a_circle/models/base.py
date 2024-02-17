#!/usr/bin/python3
# Jahaziel Adans Serrano
""" Defines a base model class"""


class Base:
    """Base Model

        Base for the other classes
        
        Attributes:
            __nb_objects (int): The number of instantiated Bases
    """
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        """ Initialize a new Base

            Args:
                id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nnb_objects += 1
            self.id = Base.__nb_objects