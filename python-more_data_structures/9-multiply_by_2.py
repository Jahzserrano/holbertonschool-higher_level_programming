#!/usr/bin/python3
# 9-multiple_by_2.py
# Jahaziel Adans Serrano


def multiply_by_2(a_dictionary):
    """Return a new dictionary where each element is multipled by 2"""
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
