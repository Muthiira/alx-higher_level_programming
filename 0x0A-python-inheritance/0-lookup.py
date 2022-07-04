#!/usr/bin/python3
def lookup(obj):
    """function that returns list of available attributes of an object"""
    return list(dir(obj))
