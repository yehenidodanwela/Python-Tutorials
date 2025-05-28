number = int(input("Enter a positive integer: "))
factorial = 1
i = number
while (i > 0):
    factorial *= i
    i -= 1
print ("The factorial of " + str(number) + " is " + str(factorial))
