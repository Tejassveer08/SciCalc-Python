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

## Taylor/Mclaurin Series - 
$$
\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots
\quad \text{for } -1 < x \leq 1
$$
 

## Change of Base Formula
$$
\log_{10}(x) = \frac{\ln(x)}{\ln(10)}
$$


## Taylor Series of Sin Function
$$
\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots
$$


## Taylor Series of Cos Function
$$
\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots
$$


## Tangent Function
$$
\tan(x) = \frac{\sin(x)}{\cos(x)}
$$




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
