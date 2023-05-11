from packages.math_function import add, subtract, multiply, divide
from packages.greeting import hello, goodbye

def main():
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
    hello()
    goodbye()

if __name__ == "__main__":
    main()