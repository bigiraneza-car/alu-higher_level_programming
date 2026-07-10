#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: ", end="")
        return result
    except ZeroDivisionError:
        return None
    finally:
        print("{}".format(result))
