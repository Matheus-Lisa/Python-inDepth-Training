# 1. Introduction to Strings
    #A string in Python is an immutable sequence of characters enclosed in single ('), double ("), or triple (''' or """) quotes. 
    #Strings are a fundamental data type used for text manipulation, including words, sentences, or even entire documents.

#2. Characteristics of Strings
    #Immutable: Strings cannot be modified after they are created.
    #Indexed and Sliced: You can access specific characters or substrings using indexes.
    #Iterable: Strings can be looped through using a for loop.
    #Unicode Support: Python strings support Unicode, allowing multilingual text handling.

#3. String Representation in Memory
    #Strings are stored as an ordered collection of Unicode characters, 
    #where each character is represented by a unique code point. 
    #Python uses the UTF-8 encoding by default, which supports a wide range of characters from different languages.

#4. String Operations in Python
    #Strings in Python support a variety of operations, including concatenation, slicing, indexing, searching, formatting, and more. 
    #Below is a comprehensive breakdown of all the operations that can be performed on strings.
    #Basic Operations
    #Summary of String Operations
        
        #Operation	Description	Example
        Concatenation	+ operator joins strings	"Hello" + " World" → "Hello World"
        Repetition	* operator repeats string	"Hi" * 3 → "HiHiHi"
        Indexing	Access character by index	"Python"[0] → 'P'
        Slicing	Extract substring	"Python"[1:4] → "yth"
        Membership	Check if substring exists	"Py" in "Python" → True
        Length	Get number of characters	len("Python") → 6
        Case Methods	Convert case	"hello".upper() → "HELLO"
        Trim	Remove spaces	" hi ".strip() → "hi"
        Find/Replace	Locate or replace substrings	"hello".replace("h", "H") → "Hello"
        Split	Convert to list	"a,b,c".split(",") → ['a', 'b', 'c']
        Join	Convert list to string	" ".join(['a', 'b', 'c']) → "a b c"
        Formatting	Insert variables	f"Age: {25}" → "Age: 25"
        Encoding	Convert to bytes	"Hi".encode() → b'Hi'
        Escape Sequences	Insert special characters	"Hello\nWorld" → Multiline output
        Reversal	Reverse a string	"Python"[::-1] → "nohtyP"

#5. String Methods

    #1. Case Conversion Methods
    .upper() = Converts all characters to uppercase
    .lower() = Converts all characters to lowercase
    .capitalize() = Capitalizes the first letter
    .title() = Capitalizes the first letter of each word
    .swapcase() = Swaps uppercase to lowercase and vice versa
    
    #2. Trimming & Padding Methods
    .strip() = Removes leading and trailing whitespace
    .lstrip() = Removes leading (left) whitespace
    .rstrip() = Removes trailing (right) whitespace
    .center(width, fillchar) = Centers text with padding
    .ljust(width, fillchar) = Left-aligns text with padding
    .rjust(width, fillchar) = Right-aligns text with padding
    
    #3. Searching & Finding Methods
    .find(substring) = Returns index of first occurrence (-1 if not found)
    .rfind(substring) = Returns last occurrence of substring
    .index(substring) = Like .find(), but raises an error if not found
    .rindex(substring) = Like .rfind(), but raises an error if not found
    .count(substring) = Counts occurrences of a substring
    
    #4. String Modification Methods
    .replace(old, new, count) = Replaces occurrences of a substring
    .translate(table) = Translates characters using a translation table
    .maketrans(old, new) = Creates a translation table
    
    #5. Checking String Content (Boolean Methods)
    .startswith(substring) = Checks if string starts with given substring
    .endswith(substring) = Checks if string ends with given substring
    .isalpha() = Checks if all characters are alphabetic
    .isdigit() = Checks if all characters are digits
    .isalnum() = Checks if all characters are alphanumeric
    .isspace() = Checks if string contains only whitespace
    .islower() = Checks if all characters are lowercase
    .isupper() = Checks if all characters are uppercase
    .istitle() = Checks if string follows title case
    
    #6. Splitting & Joining Methods
    .split(separator, maxsplit) = Splits string into a list
    .rsplit(separator, maxsplit) = Splits from right side
    .splitlines(keepends=False) = Splits at line breaks (\n)
    .partition(separator) = Splits into a tuple of three parts
    .rpartition(separator) = Like .partition(), but starts from the right
    .join(iterable) = Joins elements of an iterable into a string
    
    #7. Formatting Methods
    .format(*args, **kwargs) = Formats a string using placeholders
    .format_map(mapping) = Similar to .format(), but with a mapping dictionary
    f"{var}" = f-string formatting (Python 3.6+)
    
    #8. Encoding & Decoding Methods
    .encode(encoding, errors) = Converts string to bytes
    .decode(encoding, errors) = Converts bytes to string
    
    #9. Escape Sequence Handling
    .expandtabs(tabsize=8) = Replaces tab characters (\t) with spaces
    
    #10. String Alignment & Filling
    .zfill(width) = Pads string with zeros from the left
    
    #11. Case Folding (for Case-Insensitive Comparisons)
    .casefold() = Converts to lowercase, better for case-insensitive comparisons
    
    #12. Unicode Handling & Normalization
    .isprintable() = Checks if all characters are printable
    .isascii() = Checks if string contains only ASCII characters
    
    #13. Raw String Representation
    repr(string) = Returns a string representation with escape characters
    
    #14. Removal of Prefix & Suffix (Python 3.9+)
    .removeprefix(prefix) = Removes a specific prefix from a string
    .removesuffix(suffix) = Removes a specific suffix from a string
    
    #15. Reversing a String (No Direct Method, but Commonly Used)
    [::-1] = Reverse a string using slicing
    
    #16. Checking Unicode Numeric Characters
    .isnumeric() = Checks if string contains only numeric characters
    .isdecimal() = Checks if string contains only decimal characters

#6. String Formatting

    # 1. Using f-strings (Python 3.6+)
    name = "Alice"
    age = 25
    print(f"My name is {name} and I am {age} years old.")  = "My name is Alice and I am 25 years old."

    # 2. Using .format() method
    print("My name is {} and I am {} years old.".format(name, age)) = "My name is Alice and I am 25 years old."

    # 3. Using .format() with positional arguments
    print("I love {1} and {0}.".format("Python", "Java"))  = "I love Java and Python."

    # 4. Using .format() with named arguments
    print("My name is {n} and I am {a} years old.".format(n=name, a=age))  = "My name is Alice and I am 25 years old."

    # 5. Formatting numbers (decimal places)
    pi = 3.1415926535
    print(f"Pi rounded to 2 decimals: {pi:.2f}")  = "Pi rounded to 2 decimals: 3.14"

    # 6. Formatting numbers with commas
    large_number = 1000000
    print(f"Formatted number: {large_number:,}")  = "Formatted number: 1,000,000"

    # 7. Padding and alignment
    text = "Python"
    print(f"{text:<10}")  = Left align: 'Python    '
    print(f"{text:>10}")  = Right align: '    Python'
    print(f"{text:^10}")  = Center align: '  Python  '

    # 8. Using old-style formatting (% operator)
    print("My name is %s and I am %d years old." % (name, age))  = "My name is Alice and I am 25 years old."

    # 9. Binary, Octal, Hexadecimal conversion
    num = 255
    print(f"Binary: {num:b}, Octal: {num:o}, Hex: {num:x}")  = "Binary: 11111111, Octal: 377, Hex: ff"

    # 10. Percentage formatting
    value = 0.25
    print(f"Percentage: {value:.2%}")  = "Percentage: 25.00%"

    # 11. Using .format_map() with a dictionary
    data = {"name": "Alice", "age": 25}
    print("My name is {name} and I am {age} years old.".format_map(data))  = "My name is Alice and I am 25 years old."

    # 12. Escape curly braces in f-strings
    print(f"Curly braces: {{Hello}}")  = "Curly braces: {Hello}"
    
#7. Escape Sequences

    # 1. Newline (\n) - Moves to a new line
    print("Hello\nWorld")  # Output:
    # Hello
    # World

    # 2. Tab (\t) - Inserts a tab space
    print("Hello\tWorld")  # Output: Hello   World

    # 3. Backslash (\\) - Prints a backslash
    print("This is a backslash: \\")  # Output: This is a backslash: \

    # 4. Single quote (\') - Prints a single quote
    print('It\'s a beautiful day!')  # Output: It's a beautiful day!

    # 5. Double quote (\") - Prints a double quote
    print("He said, \"Python is awesome!\"")  # Output: He said, "Python is awesome!"

    # 6. Carriage return (\r) - Moves cursor to the beginning of the line
    print("Hello\rWorld")  # Output: World  (Hello is overwritten)

    # 7. Backspace (\b) - Deletes the previous character
    print("Hello\b World")  # Output: Hell World

    # 8. Form feed (\f) - Moves to a new page (rarely used)
    print("Hello\fWorld")  # Output may vary based on terminal

    # 9. Vertical tab (\v) - Moves to the next vertical tab stop
    print("Hello\vWorld")  # Output may vary based on terminal

    # 10. Unicode Character (\uXXXX) - Prints a Unicode character
    print("\u2764")  # Output: ❤ (Heart symbol)

    # 11. Unicode Character (\UXXXXXXXX) - Prints a Unicode character with 8-digit code
    print("\U0001F600")  # Output: 😀 (Smiley emoji)

    # 12. Octal value (\ooo) - Represents characters using octal values
    print("\101")  # Output: A (Octal 101 = ASCII 'A')

    # 13. Hex value (\xhh) - Represents characters using hexadecimal values
    print("\x41")  # Output: A (Hex 41 = ASCII 'A')

    # 14. Null character (\0) - Represents a null character (used in low-level programming)
    print("Hello\0World")  # Output: HelloWorld (Null character ignored in printing)

    # 15. Bell/Alert (\a) - Triggers a system alert sound
    print("\a")  # May trigger a beep sound in some systems

    # 16. Raw string (r"") - Treats backslashes as literal characters
    print(r"C:\Users\Name\Documents")  # Output: C:\Users\Name\Documents

    # 17. Raw string with escape sequences - Avoids special interpretation
    print(r"Hello\nWorld")  # Output: Hello\nWorld (Does not interpret \n as newline)

    # 18. Multi-line string using triple quotes (""" or ''')
    print("""Hello
    World""")  # Output:
    # Hello
    # World

    # 19. Escaping curly braces in f-strings
    print(f"Curly braces: {{Hello}}")  # Output: Curly braces: {Hello}

    # 20. Combining escape sequences
    print("Line1\nLine2\tTabbed\n\"Quoted\"")  
    # Output:
    # Line1
    # Line2   Tabbed
    # "Quoted"
    


