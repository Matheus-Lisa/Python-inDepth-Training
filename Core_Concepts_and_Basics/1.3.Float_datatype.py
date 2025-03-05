#A floating-point number (or simply "float") is a numerical data type used in Python to represent real numbers that have a fractional part. 
#They are used when precision with decimal values is needed.
#In Python, floating-point numbers are implemented using the double-precision (64-bit) IEEE 754 standard. 
# This format allows for a wide range of values but comes with certain limitations due to the way numbers are stored in memory.

#1. What is a Float?
#A float in Python is a number that can have a fractional part. 
#It is represented using the IEEE 754 standard, which means it is a double-precision floating-point number (64-bit).
#Examples
    a = 3.14       # A float number
    b = -0.001     # A small negative float
    c = 2.0        # Even though this is 2, the decimal makes it a float
    d = 1.23e3     # Scientific notation (1.23 × 10³ = 1230.0)
    e = 4.56E-2    # Scientific notation (4.56 × 10⁻² = 0.0456)

#2. Creating Floats
#There are multiple ways to create floats in Python:
    
    #2.1 Direct Assignment
    x = 10.5
    y = -2.7
    
    #2.2 Using float() Constructor
    #You can convert other types to floats using float():
    
    a = float(5)        # Converts an integer to a float: 5.0
    b = float("3.14")   # Converts a string to a float: 3.14
    c = float("1e2")    # Converts scientific notation string to float: 100.0
    
    #3. Floating-Point Precision and Representation Issues
        
        #3.1 Precision Limitation
        #Floats in Python use binary (base-2) representation, meaning some decimal numbers cannot be represented exactly. 
        #This leads to small precision errors.
        #Example:
        print(0.1 + 0.2)  # Output: 0.30000000000000004
        
        #3.2 Rounding Errors
        #To mitigate precision issues, you can round floats using round():
        print(round(0.1 + 0.2, 2))  # Output: 0.3

#4. Operations on Floats
    
    #You can perform arithmetic operations on floats just like integers:
    #4.1 Basic Arithmetic
        a = 5.5
        b = 2.0

        print(a + b)  # Addition: 7.5
        print(a - b)  # Subtraction: 3.5
        print(a * b)  # Multiplication: 11.0
        print(a / b)  # Division: 2.75
        print(a // b) # Floor division: 2.0 (returns float if at least one operand is float)
        print(a % b)  # Modulus: 1.5
        print(a ** b) # Exponentiation: 30.25

    #4.2 Special Float Values
    #Python supports special floating-point values:
    import math

    print(math.inf)      # Positive Infinity
    print(-math.inf)     # Negative Infinity
    print(math.nan)      # Not a Number (NaN)

#5. Handling Float Precision Issues
    
    #5.1 The decimal Module (For High-Precision Arithmetic)
    #If you need precise decimal calculations, use the decimal module:
    from decimal import Decimal, getcontext
    getcontext().prec = 10  # Set precision to 10 decimal places
    x = Decimal("0.1") + Decimal("0.2")
    print(x)  # Output: 0.3 (No floating-point error)

    #5.2 The fractions Module (For Exact Representations)
    #For exact fractional representations, use the fractions module:
    from fractions import Fraction
    frac = Fraction(0.1)  # Imprecise due to float conversion
    print(frac)  # Output: 3602879701896397/36028797018963968
    frac = Fraction("0.1")  # Exact representation
    print(frac)  # Output: 1/10

#6. Comparing Floats
#Due to precision errors, comparing floats directly with == can be unreliable.

    #6.1 Using math.isclose()
    #Use math.isclose() for reliable float comparisons:
    import math
    a = 0.1 + 0.2
    b = 0.3
    print(math.isclose(a, b, rel_tol=1e-9))  # True
    
#7. Converting Floats
    #7.1 Float to Integer
    -> int(): Truncates (removes decimal, does NOT round)
    
    print(int(5.9))   # Output: 5
    print(int(-3.7))  # Output: -3
    
    ->round(): Rounds to the nearest integer

    print(round(5.9))   # Output: 6
    print(round(-3.7))  # Output: -4
    
    #7.2 Float to String
    str(): Converts float to string
    
    print(str(3.14))  # Output: "3.14"

    #Formatting for better control:
    
    print(f"{3.141592:.2f}")  # Output: "3.14" (2 decimal places)

#8. Memory Usage and Performance
#Floats take 64 bits (8 bytes) in memory. If you need lower precision, you can use NumPy's float32:

import numpy as np
x = np.float32(3.14)
print(x)  # 3.14 stored as 32-bit float

#This reduces memory usage but limits precision.




