#!/usr/bin/python3
print("{}".format(''.join(
    chr(97 + i) for i in range(26) if i not in [4, 16])), end='')
