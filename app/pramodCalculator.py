import sys

def add(a, b):
    return int(a) + int(b)

def sub(a, b):
    return int(a) - int(b)

def mul(a, b):
    return int(a) * int(b)

def div(a, b):
    if int(b) == 0:
        raise ValueError("Division by zero is not allowed")
    return int(a) / int(b)

def main():
    if len(sys.argv) != 4:
        print("Usage: pramodCalculator <operation> <a> <b>")
        print("Operations: add, sub, mul, div")
        sys.exit(1)
    
    operation = sys.argv[1]
    a = sys.argv[2]
    b = sys.argv[3]

    if operation == 'add':
        result = add(a, b)
    elif operation == 'sub':
        result = sub(a, b)
    elif operation == 'mul':
        result = mul(a, b)
    elif operation == 'div':
        result = div(a, b)
    else:
        print(f"Unknown operation: {operation}")
        sys.exit(1)
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
