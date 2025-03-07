#Let’s dive into a detailed explanation of Data Structures in Python, focusing on Lists and Strings. 
#These are two fundamental data structures in Python that you’ll encounter frequently, and mastering them will give you a solid foundation for programming. 
#I’ll break this down step-by-step with examples to make it clear and practical.

#1. Lists
#A list in Python is a mutable, ordered collection of items. 
#You can think of it as a dynamic container that can hold objects of any type—integers, strings, floats, even other lists! 
#Lists are incredibly versatile and commonly used for storing and manipulating sequences of data.

#1.1.Creation
#Lists are created using square brackets [], with items separated by commas. 
#Here’s how you can create a list:

# Empty list
my_list = []

# List with mixed data types
my_list = [1, "hello", 3.14, True]

# List with duplicate values
my_list = [1, 1, 2, 3, 3]

#You can also create a list using the list() constructor:

my_list = list("abc")  # Converts string to list: ['a', 'b', 'c']

#1.2.Indexing
#Lists are zero-indexed, meaning the first item is at index 0, the second at index 1, and so on. 
#You can access elements using their index:

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: "apple"
print(fruits[2])  # Output: "cherry"

#Negative indexing is also supported, counting from the end:

print(fruits[-1])  # Output: "cherry" (last item)
print(fruits[-2])  # Output: "banana"

#1.3.Slicing
#Slicing allows you to extract a portion of a list using the syntax list[start:stop:step]. 
#The stop index is exclusive.

numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])    # Output: [1, 2, 3] (from index 1 to 3)
print(numbers[:3])     # Output: [0, 1, 2] (start to index 2)
print(numbers[2:])     # Output: [2, 3, 4, 5] (index 2 to end)
print(numbers[::2])    # Output: [0, 2, 4] (every second item)
print(numbers[::-1])   # Output: [5, 4, 3, 2, 1, 0] (reverse the list)

#1.4.Basic Methods
#Lists come with a variety of built-in methods to manipulate them. 
#Here are some of the most commonly used ones:

◘append(item): Adds an item to the end of the list.

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ["apple", "banana", "cherry"]

◘remove(item): Removes the first occurrence of an item. Raises a ValueError if the item isn’t found.

fruits = ["apple", "banana", "apple"]
fruits.remove("apple")
print(fruits)  # Output: ["banana", "apple"]

◘pop(index): Removes and returns the item at the given index (defaults to the last item if no index is provided).

fruits = ["apple", "banana", "cherry"]
popped_item = fruits.pop(1)
print(popped_item)  # Output: "banana"
print(fruits)       # Output: ["apple", "cherry"]

◘insert(index, item): Inserts an item at a specific index.

fruits = ["apple", "cherry"]
fruits.insert(1, "banana")
print(fruits)  # Output: ["apple", "banana", "cherry"]

◘extend(iterable): Adds all items from an iterable (like another list) to the end.

fruits = ["apple"]
fruits.extend(["banana", "cherry"])
print(fruits)  # Output: ["apple", "banana", "cherry"]

◘index(item): Returns the index of the first occurrence of an item.

fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # Output: 1

◘sort(): Sorts the list in place (modifies the original list).

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]

#Lists are mutable, so you can also modify elements directly:

fruits = ["apple", "banana"]
fruits[1] = "orange"
print(fruits)  # Output: ["apple", "orange"]

#2. Strings
#A string in Python is an immutable sequence of characters. 
#Once created, you cannot change a string’s contents, but you can create new strings from it. 
#Strings are enclosed in single quotes '', double quotes "", or triple quotes ''' for multi-line strings.

#2.1.Creation

# Single-line strings
name = "Alice"
greeting = 'Hello'

# Multi-line string
message = '''This is a
multi-line
string'''

#2.2.Operations
#Strings support several operations:

◘Concatenation (+): Combines strings.

first = "Hello"
second = "World"
result = first + " " + second
print(result)  # Output: "Hello World"

◘Repetition (*): Repeats a string.

print("Ha" * 3)  # Output: "HaHaHa"

◘Indexing and Slicing: Works like lists (strings are sequences too!).

text = "Python"
print(text[0])     # Output: "P"
print(text[-1])    # Output: "n"
print(text[1:4])   # Output: "yth"
print(text[::-1])  # Output: "nohtyP" (reversed)

#2.3.Methods
#Strings have a rich set of methods. 
#Here are some key ones:

◘upper(): Converts all characters to uppercase.

text = "hello"
print(text.upper())  # Output: "HELLO"

◘lower(): Converts all characters to lowercase.

text = "WORLD"
print(text.lower())  # Output: "world"

◘split(separator): Splits a string into a list based on a separator (default is whitespace).

sentence = "Hello,world,Python"
words = sentence.split(",")
print(words)  # Output: ["Hello", "world", "Python"]

◘join(iterable): Joins elements of an iterable into a string, using the string as a separator.

words = ["Hello", "world"]
sentence = " ".join(words)
print(sentence)  # Output: "Hello world"

◘strip(): Removes leading and trailing whitespace (or specified characters).

text = "  hello  "
print(text.strip())  # Output: "hello"

◘replace(old, new): Replaces all occurrences of a substring with another.

text = "I like cats"
print(text.replace("cats", "dogs"))  # Output: "I like dogs"

◘find(substring): Returns the index of the first occurrence of a substring, or -1 if not found.

text = "Python"
print(text.find("th"))  # Output: 2
print(text.find("z"))   # Output: -1

#2.4.Formatting with f-strings
#F-strings (introduced in Python 3.6) provide a concise and readable way to embed expressions inside strings. 
#They are prefixed with f and use curly braces {} for placeholders:

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
# Output: "My name is Alice and I am 25 years old."

# You can include expressions
print(f"Next year, I’ll be {age + 1}.")
# Output: "Next year, I’ll be 26."

#F-strings are more intuitive than older methods like .format() or %, though those are still valid:

# Using .format()
print("My name is {} and I am {}.".format(name, age))
# Using %
print("My name is %s and I am %d." % (name, age))

#Key Differences Between Lists and Strings

◘Mutability: Lists are mutable (you can change their contents), while strings are immutable (you can’t modify them directly; operations create new strings).
◘Use Case: Use lists for collections of items you might need to modify; use strings for text data.
◘Methods: Lists have methods like append() and remove() for modification, while string methods like upper() or split() return new strings.

#Practical Example Combining Lists and Strings

# Create a list of words from a sentence
sentence = "Python is awesome"
words = sentence.split()
print(words)  # Output: ["Python", "is", "awesome"]

# Modify the list
words.append("indeed")
words[1] = "IS"

# Join back into a string
new_sentence = " ".join(words).upper()
print(new_sentence)  # Output: "PYTHON IS AWESOME INDEED"


