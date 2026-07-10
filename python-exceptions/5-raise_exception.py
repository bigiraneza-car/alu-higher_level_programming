#!/usr/bin/python3
def raise_exception():
    try:
        number = input("Enter a number:")
        if number is not int:
            raise TypeError
    except TypeError:
        print("Exception raised")
