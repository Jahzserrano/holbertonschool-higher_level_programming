#!/usr/bin/python3
# Jahaziel Adans Serrano 
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
