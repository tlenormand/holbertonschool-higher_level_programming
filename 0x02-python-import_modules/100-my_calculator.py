#!/usr/bin/python3
"""imports all functions and handles basic operations"""

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operators = ["+", "-", "*", "/"]
    functions = [add(a, b), sub(a, b), mul(a, b), div(a, b)]

    if any(sys.argv[2] in s for s in operators):
        print(functions[operators.index(sys.argv[2])])
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
