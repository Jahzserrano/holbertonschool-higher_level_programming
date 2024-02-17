#!/usr/bin/python3
# Jahaizel Adans Serrano
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    
    def test_rect_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)
        
    def test_none_args(self):
        with self.assertRaises(TypeError)
    
    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)
    
    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)