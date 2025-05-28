def calculator (num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return  num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error"
        return num1 / num2
        
    else:
        return "invalid operation"

print (calculator (1,2,"+")) # checking for the results
print (calculator (6,3,"-")) # checking for the results
print (calculator (8,5,"*")) # checking for the results
print (calculator (100,7,"/")) # checking for the results
    
