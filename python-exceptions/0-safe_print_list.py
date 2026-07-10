#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
    try:
            print(my_list[i], end="")
            count += 1
    except IndexError:
        print("Ooops! There are no other element in the list")
        break
    print()
    return count
