#!/usr/bin/python3
print(("{:c}" * 24).format(*[(ord('a') + i) for i in range(26) if ord('a') +i not in (ord('q'), ord('e'))]), end="")
