character = input("Enter a character: ")

if ("A" <= character <= "Z"):
    print ("Uppercase")
elif ("a" <= character <= "z"):
    print ("Lowercase")
elif ("0" <= character <= "9"):
    print ("Digit")
else:
    print ("Special Character")
    


