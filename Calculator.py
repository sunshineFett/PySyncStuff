# My first Python program Sunny

print "Hello World!"

# Prompt user for two numbers
userNumber1 = int(raw_input("Please enter your first number: "))
userNumber2 = int(raw_input("Please enter your second number: "))

# Custom add function
def add(num1, num2):
	return num1 + num2
	
# Custom subtract function
def subtract(num1, num2):
	return num1 - num2
	
# Custom multiply function
def multiply(num1, num2):
	return num1 * num2
	
# Custom divide function
def divide(num1, num2):
	return num1 / num2

choice = 0

#prompt to user for operation selection
choice = input("Choose your option:  #1 Add/#2 Sub/#3 Multiply/#4 Div or 5 to exit: ")


# 1 is to add the numbers
if choice == 1:
	print userNumber1, " + ", userNumber2, "=",add(userNumber1, userNumber2)
if choice == 2:
	print userNumber1, " - ", userNumber2, "=",subtract(userNumber1, userNumber2)	
if choice == 3:
	print userNumber1, " * ", userNumber2, "=",multiply(userNumber1, userNumber2)	
if choice == 4:
	print userNumber1, " / ", userNumber2, "=",divide(userNumber1, userNumber2)	
elif choice == 5:
	choice = 0
	
print "Thank you!"
	


