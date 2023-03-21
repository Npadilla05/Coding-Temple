from math import pi 

def print_name(name: str):
    return f"Hello Mr/Ms {name}... we've been waiting for you."

# * Has a function to calculate the square footage of a house
# * Has a function to calculate the circumference of a circle
# * Has a function to change feet to inches

# Length * Width
def sq_ft(l, w):
    return l * w

# cirumfrence = 2pi R
def circle(r):
    return 2 * pi * r

# 1 foot = 12 inches
def inches(f):
    return f * 12