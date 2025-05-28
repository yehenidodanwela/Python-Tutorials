for number in range (2,21):
    is_prime = True              # assume the number is prime
    for i in range (2,number):
        if number % i == 0:      # check if number is dividible by any number from 2 to number-1
            is_prime = False
            break                # exit the loop if divisable
    if is_prime:
        print (number)           # if the number is prime it will print
