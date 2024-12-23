import argparse

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    parser = argparse.ArgumentParser(description="Simple Calculator")
    parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'], help="Operation to perform")
    parser.add_argument('num1', type=float, help="First number")
    parser.add_argument('num2', type=float, help="Second number")
    
    args = parser.parse_args()

    if args.operation == 'add':
        print(f"{args.num1} + {args.num2} = {add(args.num1, args.num2)}")
    elif args.operation == 'subtract':
        print(f"{args.num1} - {args.num2} = {subtract(args.num1, args.num2)}")
    elif args.operation == 'multiply':
        print(f"{args.num1} * {args.num2} = {multiply(args.num1, args.num2)}")
    elif args.operation == 'divide':
        print(f"{args.num1} / {args.num2} = {divide(args.num1, args.num2)}")

if __name__ == "__main__":
    calculator()
