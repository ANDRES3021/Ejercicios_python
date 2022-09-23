# Ask the user ton input 2 values and store them variables num1 num2
num1, num2 = input('Enter 2 numbers:  ').split()

# convert the strings into regular numbers
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum 
sum = num1 + num2
# substact values and store in difference 
difference = num1 - num2
#multiply 
 
product = num1 * num2
#divide

quotient = num1 /  num2
#use moduls  

remainder = num1 % num2

#print results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
>>> print("{:d} Battery street".format(98))