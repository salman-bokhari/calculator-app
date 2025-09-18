from calculator import add, subtract, multiply, divide

def repl():
    print("=" * 40)
    print("   🧮  Welcome to Simple Calculator  🧮")
    print("=" * 40)
    print("Type 'quit' or 'exit' to leave.\n")
    print("Supported operators: +  -  *  /\n")

    while True:
        expr = input("👉 Enter calculation (e.g., 2 + 2): ")
        if expr.lower() in ["quit", "exit"]:
            print("\n👋 Goodbye!")
            break

        try:
            tokens = expr.split()
            if len(tokens) != 3:
                print("⚠️  Invalid format. Use: number operator number")
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
                print("⚠️  Unsupported operator. Try + - * /")
                continue

            print(f"✅ Result: {a} {op} {b} = {result}\n")

        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    repl()
