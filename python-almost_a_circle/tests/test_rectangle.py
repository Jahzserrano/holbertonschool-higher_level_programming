#!/usr/bin/python3
# Jahaizel Adans Serrano
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    
    def test_rect_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)
        
    def test_none_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
    
    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)
            
    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)
        
    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)
            
    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)
    
    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)
    