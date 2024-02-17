#!/usr/bin/python3
# Jahaziel Adans Serrano
"""Define a rectangle class"""
from models.base import Base

class Rectangle(Base):
    """Represent a rectangle"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """ A new Rectangle """