#!/usr/bin/env python3

max = []
current = 0

f = open("input.txt", "r")
lines = f.readlines()

for line in lines:
    l = line.strip()
    if l != "":
        current += int(l)
    else:
        current = 0
    if current != 0:
        max.append(current)
print(sum(sorted(max, reverse=True)[:3]))
f.close()
