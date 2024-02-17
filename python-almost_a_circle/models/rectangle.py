#!/usr/bin/python3
# Jahaziel Adans Serrano
"""Define a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """ A new Rectangle 
        
            Args:
                width (int): The width 
                height (int): The height
                x (int): The x coordinate
                y (int): the y coordinate
                id (int): The id
            Raises:
            TypeError: If width/height are not an int
            ValueError: If width/height are <=0
            TypeError: if x/y are not an int
            ValueError: If x/y are < 0   
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        