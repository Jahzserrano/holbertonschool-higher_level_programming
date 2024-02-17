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
        
        @property
        def width(self):
            """Get the value of width"""
            return self.__width
        
        @width.setter
        def width(self, value):
            """Set the value of width"""
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        
        @property
        def height(self):
            """Get the value height"""
            return self.__height
        
        @height.setter
        def height(self, value):
            """Set the value of height"""
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value
            
        
        @property
        def x(self):
            """Get the value x"""
            return self.__x
        
        @x.setter
        def x(self, value):
            """Set the value of x"""
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be > 0")
            self.__x = value
            
        @property
        def y(self):
            """Get the value __y"""
            return self.__x
        
        @y.setter
        def y(self, value):
            """Set the value of y"""
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be > 0")
            self.__y = value
        
        def area(self):
            """Return the area of the rectangle"""
            return self.width * self.height
        
        def display(self):
            """Print a representation of a Rectangle"""
            if self.width == 0 or self.height == 0:
                print("")
                return 
            [print("") for y in range(self.y)]
            for h in range(self.height):
                [print(" ", end="") for x in range(self.x)]
                [print("#", end="") for w in range(self.width)]
                print("")
            
        def update(self, *args, **kwargs):
            """Update Rectangle"""
            if args and len(args) != 0:
                a = 0
                for arg in args:
                    if a == 0:
                        if arg is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id = arg
                    elif a == 1:
                        self.width = arg
                    elif a == 2:
                        self.height = arg
                    elif a == 3:
                        self.x = arg
                    elif a == 4:
                        self.y = arg
                    a += 1

    
        
        def __str__(self):
            """Return string representation of a Rectangle"""
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
        