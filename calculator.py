def calculator(number1, number2, operator):
	if(operator == "+"):
		return number1 + number2
	elif(operator == "-"):
		return number1 - number2
	elif(operator == "*"):
		return number1 * number2
	elif(operator == "/"):
		return number1 /  number2
	elif(operator == "//"):
		return number1 // number2
	elif(operator == "**"):
		return number1 ** number2
	else:
		print("Invalid operator")
		return False
"""
Caculator

Calculate a certain equation given two numbers and an operator

Parameters
----------
number1
	First number to be use
number2
	Second number to be use
operator
	operation to be use by the two numbers

Return
-------
float
	outcome of the +,-,*,/,//,** operation
boolean
	False if the inputed operator is invalid

Example
-------
number1 = 2
number2 = 3
operator = "*"
2 * 6 = 6
number1 = 4
number2 = 3
operator = "**"
4 ** 3 = 64
number1 = 2.4
number2 = 2
operator = "//"
2.4 // 2 = 1
"""


def input_output():
	number1 = float(input("Enter first number: "))
	number2 = float(input("Enter second number: "))
	operator = input("Enter the operation: ")
	print(calculator(number1, number2, operator))
	exit = input("Do you wish to exit? ")
	if(exit != "y"):
		input_output()
	else :
		return
"""
Take input from user and give output

Ask for user inputs, and Display the result
and ask the user if they want to exit or not

Parameters
--------

no parameter


Return
-------

Print out the return of calculator function
Print out to ask user want to exit or not

Example
--------
Enter first number: 4
Enter second number: 2
Enter the operation: **
16
Do you wish to exit? n
Enter first number: 8
Enter second number: 3
Enter the operation: *
24
Do you wish to exit? y
"""

input_output()
