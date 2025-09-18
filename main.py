from calculator import add, subtract, multiply, divide

def repl():
    print("Simple Calculator. Type 'quit' to exit.")
    while True:
        expr = input("Enter calculation (e.g., 2 + 2): ")
        if expr.lower() in ["quit", "exit"]:
            break
        try:
            tokens = expr.split()
            if len(tokens) != 3:
                print("Invalid format. Use: number operator number")
                continue
            a, op, b = tokens
            a, b = float(a), float(b)

            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                print("Unsupported operator.")
                continue

            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
