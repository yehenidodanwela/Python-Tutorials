def is_prime (number):
    if number <= 1:
        return False
    for i in range (2,number):
        if number % i == 0:
            return False
    return True

print (is_prime (2)) # Checking for the results
print (is_prime (8)) # Checking for the results
