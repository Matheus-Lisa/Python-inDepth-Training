#Booleans in Python represent one of the fundamental data types used for logical operations. 
#They are primarily used in decision-making and control flow structures like conditional statements and loops.

#1. What is a Boolean in Python?
#A Boolean is a data type that can hold one of two values:

->True
->False

#Booleans are a subclass of integers (int), where:

->True is equivalent to 1
->False is equivalent to 0

#You can verify this by checking their integer values:

print(int(True))   # Output: 1
print(int(False))  # Output: 0

#Since bool is a subclass of int, we can also perform arithmetic operations:

print(True + True)   # Output: 2  (1 + 1)
print(False + True)  # Output: 1  (0 + 1)
print(False * 10)    # Output: 0  (0 * 10)

#2. Boolean Values in Python
#In Python, the boolean values True and False are defined as keywords:

print(type(True))   # Output: <class 'bool'>
print(type(False))  # Output: <class 'bool'>

#3. Boolean Expressions
#Boolean expressions are expressions that evaluate to either True or False.

    #3.1 Comparison Operators
    #Comparison operators return boolean values:

    #Operator	Description	            Example	Result
        ==	    Equal to	             5 == 5	 True
        !=	    Not equal to	         5 != 4	 True
        >	    Greater than	         10 > 5	 True
        <	    Less than	             5 < 10	 True
        >=	    Greater than or equal to 5 >= 5	 True
        <=	    Less than or equal to	 4 <= 5	 True
        
    #Example:
        x = 10
        y = 5

        print(x > y)   # True
        print(x == y)  # False
        
    #3.2 Logical Operators
    #Logical operators are used to combine boolean expressions.

    #Operator	Description	                                    Example	        Result
       and	     Returns True if both conditions are True	     True and True	 True
       or	     Returns True if at least one condition is True	 True or False	 True
       not	     Negates a boolean value	                     not True	     False
       
    #Example:
        x = 10
        y = 5
        z = 0

        print(x > y and y > z)  # True
        print(x < y or z == 0)  # True
        print(not (x > y))      # False

#4. Boolean Type Conversion
#In Python, different values can be converted to True or False.

    #4.1 Using bool() Function
    #The bool() function is used to convert values into boolean values.
    
    print(bool(10))      # True
    print(bool(0))       # False
    print(bool("Hello")) # True
    print(bool(""))      # False

    #4.2 Truthy and Falsy Values
    #Python considers some values as Truthy (evaluates to True) and some as Falsy (evaluates to False).

    #Falsy Values:
        
    None
    False
    0 (integer)
    0.0 (float)
    "" (empty string)
    [] (empty list)
    {} (empty dictionary)
    set() (empty set)
    () (empty tuple)
    Everything else is Truthy.

    #Example:
    if []:
    print("This is True")
    else:
    print("This is False")  # Output: This is False
    
#5. Booleans in Conditional Statements
#Booleans are heavily used in if, elif, and else statements.

#Example:

age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    
#6. Booleans in Loops
#Booleans are often used as conditions in loops.

#Example:

x = 5

while x > 0:
    print(x)
    x -= 1
    
#Here, the loop runs as long as x > 0 evaluates to True.

#7. Short-Circuit Evaluation
#Python uses short-circuit evaluation for and and or operations.

In and, if the first condition is False, the second condition is not evaluated.
In or, if the first condition is True, the second condition is not evaluated.
#Example:

def check():
    print("Function executed")
    return True

print(False and check())  # Output: False (function is not executed)
print(True or check())    # Output: True (function is not executed)

#8. Using Booleans in Functions
#Booleans are commonly used in functions for return values.

#Example:

def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False

#9. The is Operator vs ==
#The is operator checks if two variables refer to the same object in memory, while == checks if they have the same value.

a = True
b = 1

print(a == b)  # True (because True == 1)
print(a is b)  # False (because they are different objects in memory)

#10. Conclusion
#Booleans (True and False) are essential in Python.
#They are a subclass of integers (True == 1, False == 0).
#They are used in comparisons, logical operations, conditionals, and loops.
#Python treats some values as Truthy and others as Falsy.
#Short-circuit evaluation helps optimize logical operations.


