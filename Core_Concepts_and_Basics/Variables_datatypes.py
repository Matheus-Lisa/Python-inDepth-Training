#Let’s dive into Python data types and variables, focusing on primitive data types (integers, floats, strings, and booleans), type conversion (casting), and the concepts of mutability versus immutability. 
#I’ll break this down step-by-step to make it clear and engaging, with examples to solidify your understanding.

#1. Variables in Python
#In Python, a variable is like a labeled box that holds a value. You don’t need to declare the type of a variable explicitly—Python figures it out based on the value you assign. 
#This is called dynamic typing. 
#You create a variable simply by assigning a value to a name using the = operator.

#Example:
x = 10        # x is an integer
name = "Alice" # name is a string

#The variable’s type can even change if you assign a new value of a different type:

x = 10       # integer
x = "hello"  # now a string

#2. Primitive Data Types
#Python has four main primitive data types—simple, foundational types that serve as building blocks for more complex data structures. 
#Let’s explore them:

#2.1. Integers (int)
->Represents whole numbers (positive, negative, or zero).
->No decimal points, infinite range (limited only by your computer’s memory).
->Examples: 5, -42, 0.

age = 25
temperature = -10
print(type(age))  # Output: <class 'int'>

#2.2. Floats (float)
->Represents numbers with decimal points or in scientific notation.
->Used for precise calculations, like measurements or percentages.
->Examples: 3.14, -0.001, 2.5e3 (which is 2500.0).

pi = 3.14159
height = 1.75
print(type(pi))  # Output: <class 'float'>

#2.3. Strings (str)
->Represents sequences of characters (text), enclosed in single (') or double (") quotes.
->Can include letters, numbers, symbols, or even be empty ("").
->Strings are ordered (characters have positions) and can be manipulated with operations like slicing.

name = "Python"
greeting = 'Hello, world!'
print(type(name))  # Output: <class 'str'>

#2.4. Booleans (bool)
->Represents truth values: True or False.
->Used in logic, conditions, and decision-making (e.g., if-statements).
->Internally, True is 1 and False is 0, but they’re distinct from integers.

is_active = True
has_permission = False
print(type(is_active))  # Output: <class 'bool'>

#3. Type Conversion (Casting)
#Sometimes you need to convert one data type to another. 
#Python provides built-in functions for this, called casting. 
#Here’s how it works for the primitive types:

->int(): Converts to an integer (drops decimal parts for floats).
->float(): Converts to a float (adds .0 to integers).
->str(): Converts to a string (wraps anything in quotes).
->bool(): Converts to a boolean (0, 0.0, "" become False; most other values become True).

#Examples:

# Float to int
x = 5.7
y = int(x)      # y = 5 (truncates decimal)
print(y)

# Int to float
a = 10
b = float(a)    # b = 10.0
print(b)

# String to int/float
num_str = "123"
num_int = int(num_str)    # num_int = 123
num_float = float(num_str) # num_float = 123.0
print(num_int, num_float)

# Anything to string
value = 42
text = str(value)  # text = "42"
print(text)

# To boolean
print(bool(0))      # False
print(bool(5))      # True
print(bool(""))     # False
print(bool("hi"))   # True

#Notes:
->Casting fails if the conversion doesn’t make sense (e.g., int("hello") raises an error).
->Be cautious with int() on floats—it truncates, not rounds (e.g., int(5.9) is 5, not 6).

#4. Mutability vs. Immutability

#This is a key concept in Python: whether a data type can be changed in place (mutable) or not (immutable). 
#It affects how variables behave when you modify them.

#4.1. Immutable Types
->Once created, their content cannot be altered without creating a new object.
->All primitive types (integers, floats, strings, booleans) are immutable.
->When you “change” them, Python creates a new object and reassigns the variable.

#Example with Strings:

word = "cat"
word = "dog"  # Creates a new string "dog", doesn’t modify "cat"
print(word)   # Output: dog

#Example with Integers:

x = 5
x = x + 1  # Creates a new integer 6, doesn’t modify 5
print(x)   # Output: 6

#4.2. Why Immutability Matters:
->Immutable objects are safe to share because they can’t be unexpectedly changed.
->Operations like += on a string don’t modify the original—they create a new string:

s = "hello"
s += " world"  # New string "hello world" is created
print(s)

#4.3.Mutable Types (For Contrast)
->Types like lists, dictionaries, and sets (not primitive types) are mutable—you can change their contents without creating a new object.

#Example with a list:

my_list = [1, 2, 3]
my_list[0] = 10  # Modifies the list in place
print(my_list)   # Output: [10, 2, 3]

->Primitive types don’t behave this way because they’re immutable.

#4.4. Immutability in Action

#Consider this:

a = 10
b = a
a = 20
print(b)  # Output: 10

#Here, b doesn’t change when a is reassigned because integers are immutable. 
#Assigning 20 to a creates a new object, leaving b pointing to the original 10.

#Compare with a mutable type (list):

a = [1, 2, 3]
b = a
a[0] = 99
print(b)  # Output: [99, 2, 3]

#Since lists are mutable, b reflects the change because a and b reference the same object.

#5. Putting It All Together

#Let’s tie this into a small program:

# Variables and types
age = 25          # int
height = 1.8      # float
name = "Alex"     # str
is_student = True # bool

# Type conversion
age_str = str(age)          # "25"
height_int = int(height)    # 1 (truncates)
status = bool(age > 20)     # True

# Immutability demo
name = name + " Smith"      # New string created
age = age + 1               # New integer created

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")
# Output: Name: Alex Smith, Age: 26, Height: 1.8, Student: True

#Key Takeaways

#1.Primitive Types: Integers (whole numbers), floats (decimals), strings (text), and booleans (True/False) are Python’s basic building blocks.
#2.Type Conversion: Use int(), float(), str(), and bool() to switch between types, but watch out for invalid conversions.
#3.Mutability: Primitive types are immutable—changes create new objects. This contrasts with mutable types like lists, which can be modified in place.
