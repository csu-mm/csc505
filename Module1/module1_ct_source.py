# Python Program: Module 1: Critical Thinking
# Created by Mukul Mondal
# Saturday, July 20th, 2025
#
'''
Problem statement:

For this assignment, you will first write a Python script and then answer some standard 
software systems development questions about the script you have written. Programmers, 
whether in teams or as individuals, have to be mindful of challenges during computer-based 
systems development. Put yourself in the position of a software developer.

To get familiar with Python programming and its related Integrated Development Environment
(IDE), begin by writing a simple Python script with any desired functionality.
Next, answer the following questions. Write out both the question and your answer:
Why does it take so long to get software finished?
Why are development costs so high?
Why can't we find all errors before we give the software to our customers?
Why do we spend so much time and effort maintaining existing programs?
Why do we continue to have difficulty in measuring progress, as software is being developed
 and maintained?
'''

#
# The program prompts user to enter two numbers.
# If user input is non-numeric then, user gets message with the input information and
#     more chances to enter any valid numeric input. 
# If both inputs are numeric then, the program shows the addition result.
#
# I'm using Visual Studio Code with python extension installed.
#
# It displays the result or message in the output window.
#
# I've added other important information, assumptions and comments inside the program itself.
#

import sys


# python supports 2 numeric types: int, float.
# Specific numeric Data types are not mentioned in the problem statement.
# Here, I'll provide code for both data types.
# To run with float data type, please uncomment the 2 lines of code for 'float' inside 'try' block.
#
# Assumption:
# Python's integer type (int) has arbitrary precision, so detecting overflow in numeric 
# operation, normally not needed. If you think, I should provide the logic for overflow 
# condition, then please let me know, I'll provide that logic.

redoInput = True  # I'll let user try again if incorrect input entered

while redoInput:   
    
    try:
        # Read user inputs and validate
        num1 = int(input('Enter your first number:\n'))     # for 'int' data types
        num2 = int(input('Enter your second number:\n'))    # for 'int' data types        
        redoInput = False
    except ValueError:
        print('Please try again with numeric inputs.')
        redoInput = True

# Prints for sum of the two numbers
print('The Sum: firstInput + secondInput: ', num1, ' + ', num2, ' = ', num1 + num2)

