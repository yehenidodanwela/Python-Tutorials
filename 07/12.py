def exponentiation (base, exponent):
    result = 1
    if exponent > 0:
        for i in range (exponent):
            result *= base

    elif exponent < 0:
        for i in range (-exponent):
            result *= base
        result = 1/result
    
    else:
        result = 1
    
    return result


print(exponentiation (2, 3)) # checking for the results
print(exponentiation (2, -3)) # checking for the results
