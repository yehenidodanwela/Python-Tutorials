def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    
    fibonacci_sequence = [0,1]
    for i in range (2,n):
        next_term = fibonacci_sequence [-1] + fibonacci_sequence [-2]
        fibonacci_sequence = fibonacci_sequence + [next_term]
    return fibonacci_sequence

print (fibonacci_sequence (5))
print (fibonacci_sequence (10))
    

