#!/usr/bin/python3
print(("{:c}" * 26).format(*[(ord('a') + i) for i in range(26)]), end="")