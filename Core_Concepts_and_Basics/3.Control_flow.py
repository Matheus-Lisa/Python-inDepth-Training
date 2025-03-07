#Let’s dive into control flow in Python, which is essentially how you direct the execution of your program. 
#It’s like giving Python a roadmap to follow based on conditions, repetitions, or interruptions. We’ll cover conditional statements (if, elif, else), loops (for and while), and the special statements break, continue, and pass. 
#I’ll explain each in detail, with examples, and keep it clear and engaging.

#1. Conditional Statements: if, elif, else
#Conditional statements let your program make decisions. 
#They evaluate whether a condition is True or False and execute code accordingly.

#How It Works
◘if: Executes a block of code if its condition is True.
◘elif: Short for "else if," it checks another condition if the previous if or elif was False.
◘else: Runs if none of the above conditions are True. It’s the fallback option.

#Syntax

if condition:
    # code to run if condition is True
elif another_condition:
    # code to run if another_condition is True
else:
    # code to run if all conditions are False
    
◘Conditions are expressions that evaluate to a Boolean (True or False), like x > 5 or name == "Alice".
◘The colon : marks the start of the code block, and indentation (usually 4 spaces) defines what’s inside that block.

#Example:

age = 20
if age >= 18:
    print("You’re an adult!")
elif age >= 13:
    print("You’re a teenager!")
else:
    print("You’re a kid!")
    
#Output: You’re an adult!

◘Here, age >= 18 is True, so the if block runs, and the rest is skipped.

#Key Points
◘You can have zero or more elif clauses, but only one else (optional).
◘Python evaluates conditions top-down and stops at the first True one.
◘Use comparison operators (>, <, ==, !=, etc.) or logical operators (and, or, not) to build conditions.

#Nested Conditionals

#You can put if statements inside others:

score = 85
if score >= 60:
    print("You passed!")
    if score >= 90:
        print("With flying colors!")
else:
    print("Better luck next time.")
    
#Output: You passed!

#2. Loops: for and while
#Loops let you repeat code. 
#Python has two main types: for loops (for iterating over a sequence) and while loops (for repeating until a condition is False).

#For Loop
◘Purpose: Iterates over a sequence (like a list, string, or range).
◘Syntax:

for variable in sequence:
    # code to repeat for each item
    
◘variable takes the value of each item in sequence one by one.

#Example:

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
    
#Output:

I like apple
I like banana
I like cherry

◘Using range(): Generates numbers to loop over.

for i in range(3):  # 0, 1, 2
    print(i)
    
#Output:

0
1
2

#While Loop
◘Purpose: Repeats as long as a condition is True.
◘Syntax:

while condition:
    # code to repeat
    
#Example:

count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1  # Increment to avoid infinite loop
    
#Output:

Count is 0
Count is 1
Count is 2

◘Warning: Forgetting to update the condition (like count += 1) can cause an infinite loop!

#Key Differences

◘Use for when you know how many times to iterate (e.g., over a list or range).
◘Use while when the number of iterations depends on a condition.

#3. Break, Continue, and Pass Statements
#These statements modify how loops (and sometimes conditionals) behave.

break
◘Purpose: Exits the loop immediately, skipping the rest of it.
◘Example:
    
for num in range(10):
    if num == 5:
        break
    print(num)
    
#Output:

0
1
2
3
4

◘Loop stops when num == 5.

continue
◘Purpose: Skips the current iteration and moves to the next one.
◘Example:
    
for num in range(5):
    if num == 2:
        continue
    print(num)
    
#Output:

0
1
3
4

◘When num == 2, continue skips the print, but the loop keeps going.

pass
◘Purpose: Does nothing! It’s a placeholder when syntax requires a statement but you don’t want action yet.
◘Example:
    
for num in range(5):
    if num == 2:
        pass  # TODO: Add logic later
    else:
        print(num)
        
#Output:

0
1
3
4

◘Useful for sketching code without errors.

#Key Points

◘break and continue work in both for and while loops.
◘pass can also be used in conditionals or functions as a no-op.


#Putting It All Together
#Here’s an example combining everything:

number = 0
while number < 10:
    if number == 7:
        print("Lucky 7! Stopping here.")
        break
    elif number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    number += 1
    
#Output:

0 is even
1 is odd
2 is even
3 is odd
4 is even
5 is odd
6 is even
Lucky 7! Stopping here.

◘The while loop runs until number < 10.
◘if/elif/else checks conditions each iteration.
◘break stops the loop at 7.

#Why It Matters
#Control flow is the backbone of programming logic. 
#Conditional statements let your code decide, loops handle repetition, and break/continue/pass give you fine-tuned control. 
#Mastering these lets you write efficient, flexible Python programs.