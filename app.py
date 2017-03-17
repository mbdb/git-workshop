#!/usr/bin/env python3

#Et voila une petite modif gratuite

def greetings():
    """Salute RESIF people"""
    print("Hello RESIF people!")

def repeat(x, callback):
    """Call x times callback"""
    for _ in range(x):
        callback()

if __name__ == "__main__":
    repeat(3, greetings)
