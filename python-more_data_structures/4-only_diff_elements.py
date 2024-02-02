#!/usr/bin/python3
# 4-only_diff_elements.py
# Jahaziel Adans Serrano


def only_diff_elements(set_1, set_2):
    """Return a set of elements present in only one set."""
    return (set_1 ^ set_2)
