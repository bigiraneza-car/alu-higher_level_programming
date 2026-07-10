#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for item in my_list:
            print("{} is in the list".format(item), end="")
            x += 1
        print(x)
    except:
        print("Ooops! There is no item in the list")
