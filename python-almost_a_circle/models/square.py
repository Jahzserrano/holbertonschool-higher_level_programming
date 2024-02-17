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
    
    def update(self, *args, **kwargs):
        """Update Square"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
                
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
                    
    
    