#!/usr/bin/python3
# 11-mutiply_list_map.py
# Jahaziel Adans Serrano

def mutiply_list_map(my_list=[], number=0):
    """Multiply a list by a selected  number"""
    return (list(map(lambda x: x*number, my_list)))
