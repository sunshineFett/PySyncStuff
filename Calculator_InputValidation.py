## @package Calculator_InputValidation
## My first Python program

print "Hello World!"

## Prompt user for two numbers
userNumber1 = int(raw_input("Please enter your first number: "))
userNumber2 = int(raw_input("Please enter your second number: "))

## Custom add function
def add(num1, num2):
	return num1 + num2
	
## Custom subtract function
def subtract(num1, num2):
	return num1 - num2
	
## Custom multiply function
def multiply(num1, num2):
	return num1 * num2
	
## Custom divide function
## @def
def divide(num1, num2):
	return num1 / num2

## @choice
choice = 0

##prompt to user for operation selection
choice = input("Choose your option:  #1 Add/#2 Sub/#3 Multiply/#4 Div or 5 to exit: ")

##Add input validation here, ensuring only digits 1 through 5 are entered, otherwise give error message to user
if choice != {1 -5}:
	print "Please enter a valid value of 1 - 5"



## 1 is to add the numbers
if choice == 1:
	print userNumber1, " + ", userNumber2, "=",add(userNumber1, userNumber2)
## 2 is to subtract the numbers
if choice == 2:
	print userNumber1, " - ", userNumber2, "=",subtract(userNumber1, userNumber2)	
## 3 is to multiply the numbers
if choice == 3:
	print userNumber1, " * ", userNumber2, "=",multiply(userNumber1, userNumber2)	
## 4 is to divide the numbers
if choice == 4:
	print userNumber1, " / ", userNumber2, "=",divide(userNumber1, userNumber2)
## 5 is to exit program
elif choice == 5:
	choice = 0
	
print "Thank you!"
	


