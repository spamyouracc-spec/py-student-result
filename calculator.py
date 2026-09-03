import sys

def main(args):
    a = float(args[1]) if len(args) > 1 else 0
    b = float(args[2]) if len(args) > 2 else 0
    operation = args[0] if len(args) > 0 else 'add'

    if operation == 'add':
        print("Result:", add(a, b))
    elif operation == 'subtract':
        print("Result:", subtract(a, b))
    elif operation == 'multiply':
        print("Result:", multiply(a, b))
    elif operation == 'divide':
        print("Result:", divide(a, b))
    else:
        print("Invalid operation.")



if name == "main":
    main(sys.argv[1:]) # Pass arguments for operation and numbers
