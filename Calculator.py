class BasicCalculator:
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
            return "Error: Negative factorial!"
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def sqrt(self, x):
        if x < 0:
            return "Error: Negative square root!"
        start, end = 0, x
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
        while b:
            a, b = b, a % b
        return abs(a)

    def lcm(self, a, b):
        return abs(a * b) // self.gcd(a, b) if a and b else 0


class ScientificCalculator:
    def ln(self, x):
        if x <= 0:
            return "Error: ln domain is (0, ∞)"
        result = 0
        n = 100
        x -= 1
        for i in range(1, n):
            term = ((-1) ** (i + 1)) * (x ** i) / i
            result += term
        return round(result, 6)

    def log10(self, x):
        LN_10 = 2.302585
        ln_result = self.ln(x)
        if isinstance(ln_result, str):
            return ln_result
        return round(ln_result / LN_10, 6)

    def degrees_to_radians(self, deg):
        return deg * (3.14159265 / 180)

    def sin(self, deg):
        x = self.degrees_to_radians(deg)
        result = 0
        for i in range(10):
            sign = (-1) ** i
            result += sign * (x ** (2 * i + 1)) / self.factorial(2 * i + 1)
        return round(result, 6)

    def cos(self, deg):
        x = self.degrees_to_radians(deg)
        result = 0
        for i in range(10):
            sign = (-1) ** i
            result += sign * (x ** (2 * i)) / self.factorial(2 * i)
        return round(result, 6)

    def tan(self, deg):
        cos_val = self.cos(deg)
        if abs(cos_val) < 1e-6:
            return "Error: tan undefined"
        return round(self.sin(deg) / cos_val, 6)

    def factorial(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


class Calculator(BasicCalculator, ScientificCalculator):
    def menu(self):
        while True:
            print("\n====== Calculator Menu ======")
            print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
            print("5. Power\n6. Factorial\n7. Square Root")
            print("8. GCD\n9. LCM\n10. ln\n11. log10")
            print("12. sin\n13. cos\n14. tan\n0. Exit")

            choice = input("Enter choice (0-14): ")

            if choice == '0':
                print("Exiting calculator.")
                break

            if choice in ['1', '2', '3', '4', '5', '8', '9']:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))

            if choice == '1':
                print("Result:", self.add(a, b))
            elif choice == '2':
                print("Result:", self.subtract(a, b))
            elif choice == '3':
                print("Result:", self.multiply(a, b))
            elif choice == '4':
                print("Result:", self.divide(a, b))
            elif choice == '5':
                print("Result:", self.power(a, b))
            elif choice == '6':
                n = int(input("Enter number: "))
                print("Result:", self.factorial(n))
            elif choice == '7':
                x = float(input("Enter number: "))
                print("Result:", self.sqrt(x))
            elif choice == '8':
                print("Result:", self.gcd(a, b))
            elif choice == '9':
                print("Result:", self.lcm(a, b))
            elif choice == '10':
                x = float(input("Enter number: "))
                print("Result:", self.ln(x))
            elif choice == '11':
                x = float(input("Enter number: "))
                print("Result:", self.log10(x))
            elif choice == '12':
                deg = float(input("Enter angle in degrees: "))
                print("Result:", self.sin(deg))
            elif choice == '13':
                deg = float(input("Enter angle in degrees: "))
                print("Result:", self.cos(deg))
            elif choice == '14':
                deg = float(input("Enter angle in degrees: "))
                print("Result:", self.tan(deg))
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    calc = Calculator()
    calc.menu()

