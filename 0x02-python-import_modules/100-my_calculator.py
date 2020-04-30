#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    if len(argv) - 1 is 3:
        num1 = int(argv[1])
        op = argv[2]
        num2 = int(argv[3])
        if op is '+':
            print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
        elif op is '-':
            print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
        elif op is '*':
            print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
        elif op is '/':
            print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
