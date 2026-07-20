#!/usr/bin/python3
"""Defines a class square with size validation, area, and printing."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Reinitialize the private instance attribute size."""
        self.size = size

    @property
    def size(self):
        """A getter that return the size value."""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter, that set the final value of the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the value of the square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the # character."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
~
