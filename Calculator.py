
class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b

    def power(self, base, exp):
        result = 1
        for _ in range(abs(exp)):
            result *= base
        if exp < 0:
            return 1 / result
        return result

    def factorial(self, n):
        if n < 0:
            return "Error: Factorial of negative number!"
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def sqrt(self, x):
        if x < 0:
            return "Error: Square root of negative number!"
        if x == 0 or x == 1:
            return x
        start = 0
        end = x
        ans = 0
        for _ in range(100):
            mid = (start + end) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
                ans = mid
            else:
                end = mid
        return round(ans, 6)

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def lcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.gcd(a, b)


def main():
    calc = Calculator()

    while True:
        print("\n----- Calculator Menu -----")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Factorial")
        print("7. Square Root")
        print("8. GCD")
        print("9. LCM")
        print("0. Exit")

        choice = input("Enter your choice (0-9): ")

        if choice == '0':
            print("Exiting Calculator. Goodbye!")
            break

        elif choice in ['1', '2', '3', '4', '5', '8', '9']:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

        if choice == '1':
            print("Result:", calc.add(a, b))
        elif choice == '2':
            print("Result:", calc.subtract(a, b))
        elif choice == '3':
            print("Result:", calc.multiply(a, b))
        elif choice == '4':
            print("Result:", calc.divide(a, b))
        elif choice == '5':
            print("Result:", calc.power(a, b))
        elif choice == '6':
            n = int(input("Enter a number: "))
            print("Result:", calc.factorial(n))
        elif choice == '7':
            x = float(input("Enter a number: "))
            print("Result:", calc.sqrt(x))
        elif choice == '8':
            print("Result:", calc.gcd(a, b))
        elif choice == '9':
            print("Result:", calc.lcm(a, b))
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
