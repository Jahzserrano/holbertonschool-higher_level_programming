#!/usr/bin/python3
# 8-simple_delete.py
# Jahaziel Adans Serrano


def simple_delete(a_dictionary, key=""):
    """Delete a specific element"""
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
