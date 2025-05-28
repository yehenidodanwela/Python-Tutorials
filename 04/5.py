total = 0
number = 0
while (number >= 0):     # Loop continues as long as the number is non-negative
    number = float (input("Enter a positive number: " ))
    if (number >= 0):        # Check if the entered number is positive
        total += number      # Add the positive number to the total
print ("The total sum of the entered positive numbers is:", total)     # Output the total sum of positive numbers
        
