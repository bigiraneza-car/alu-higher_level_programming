#!/usr/bin/python3
"""Defines an empty class square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Reinitialize the private instance attribute size."""
        self.__size = size
    if size not int:
        try:
            pass
        except TypeError:
            print("size must be an integer")
    if size < 0:
        try:
            pass
        except ValueError:
            print("size must be >=0")
