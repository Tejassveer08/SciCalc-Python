**Calculator built on OOPS**



Hello, this is a simple yet effective calculator script written in basic python with various classes for carrying out mathematical operations and displaying the result.
It uses OOPS and Inheritance principles and does not contain any inbuilt module from python's extensive library.
To use it, download the script and run it locally, it's menu based and takes user input as well.


This Calculator is capable of Multiplication, Addition, Subtraction, Division along with a few complex features like exponents, Square roots, Factorial, Greatest Common Divisor, Lowest Common Multiple, and calculating basic trigonometric functions as well.


For the Scientific Calculator, here's the logic and reasoning for class creation


# 📐 Scientific Calculator (No Math Module)

This is a scientific calculator class implemented in **pure Python** using **Object-Oriented Programming (OOP)** concepts. It performs:

- Basic arithmetic operations
- Power, factorial, square root
- **Logarithmic functions** (`ln`, `log10`)
- **Trigonometric functions** (`sin`, `cos`, `tan`)

All functions are computed **without using the `math` module** — approximations are done using **Taylor series expansions** and **basic algebra**.

---

## 🧠 Class: `ScientificCalculator`

### ✅ Methods Overview

| Method       | Description                         | Implementation Technique       |
|--------------|-------------------------------------|--------------------------------|
| `ln(x)`      | Natural logarithm                   | Taylor/Maclaurin series        |
| `log10(x)`   | Base-10 logarithm                   | Change-of-base formula         |
| `sin(deg)`   | Sine function (in degrees)          | Taylor series                  |
| `cos(deg)`   | Cosine function (in degrees)        | Taylor series                  |
| `tan(deg)`   | Tangent function (in degrees)       | sin / cos                      |
| `factorial(n)` | Factorial (helper method)        | Loop-based                     |

---

## 📊 Logarithmic Functions

### 🔹 `ln(x)`: Natural Logarithm

```python
def ln(self, x):
    if x <= 0:
        return "Error: ln domain is (0, ∞)"
    x -= 1
    result = 0
    for i in range(1, 100):
        term = ((-1) ** (i + 1)) * (x ** i) / i
        result += term
    return round(result, 6)
