import sys

def add(a, b):
    return int(a) + int(b)

def main():
    if len(sys.argv) != 3:
        print("Usage: addition <a> <b>")
        sys.exit(1)
    a = sys.argv[1]
    b = sys.argv[2]
    result = add(a, b)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
