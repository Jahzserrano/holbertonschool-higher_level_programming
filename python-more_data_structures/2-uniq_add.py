#!/usr/bin/python3
# 2-uniq_add.py
# Jahaziel Adans Serrano

def uniq_add(my_list=[]):
    """Add unique integers in a list"""
    result = 0
    for x in set(my_list):
        result += x
    return (result)
