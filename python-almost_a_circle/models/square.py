#!/usr/bin/python3
# Jahaziel Adans Serrano
"""Define a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square
    
    Args:
        size (int): The size fo the Square
        x (int): The coordinate x
        y (int): The coordinate y
        id (int): The id of the object
    """
    
    def __init__(self, size, x=0, y=0, id=None):
        super.__init__(size, size, x, y, id)
        
    @property
    def size(self):
        """Get the size"""
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    
    
    