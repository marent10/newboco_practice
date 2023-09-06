#!/usr/bin/python3
names = ["fred","Jerry", "Ron", "Conner"]
i = len(names)
print(i)
names.reverse()
while i != 0:
    print(f"Hello, {names[i-1]}, you have been greeted")
    i -= 1

