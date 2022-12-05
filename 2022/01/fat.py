#!/usr/bin/env python3

max = 0
current = 0

f = open("input.txt", "r")
lines = f.readlines()

for line in lines:
    l = line.strip()
    if l != "":
        current += int(l)
        if current > max:
            max = current
    else:
        current = 0
print(max)
f.close()


max
