# encoding: utf-8


def main(x):
    """
    你好
    :param x:
    :return:
    """
    if x == 2:
        print "hello, world"
    else:
        print "F**k you, world"


def calculator(x, op, y):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "x":
        return x * y
    elif op == "/":
        return x / y
    else:
        raise Exception("OMG!")

import math

r = 7
h = 9
z = (math.pi * r**2) * h
print z

a = 0
while a < 1:
    a = a + 1
    print a

print calculator(8888, "+", 99)

if __name__ == "__main__":
    main(6)
