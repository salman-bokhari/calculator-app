from calculator import add, subtract, multiply, divide

def main():
    print("📦 Running Calculator Demo inside Docker...\n")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"20 / 5 = {divide(20, 5)}")

    print("\n✅ Calculator demo finished successfully.")

if __name__ == "__main__":
    main()
