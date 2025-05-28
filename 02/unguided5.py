sub1 = float (input("Enter your marks for the subject 1: "))
sub2 = float (input("Enter your marks for the subject 2: "))
sub3 = float (input("Enter your marks for the subject 3: "))
sub4 = float (input("Enter your marks for the subject 4: "))
sub5 = float (input("Enter your marks for the subject 5: "))

average = (sub1 + sub2 + sub3 + sub4 + sub5)/5

print ("Your average mark is:" + " " + str(average))

if average >= 75:
    print ("Your grade is: A")
elif average >= 65:
    print ("Your grade is: B")
elif average >= 55:
    print ("Your grade is: c")
elif average >= 35:
    print ("Your grade is: S")
else:
    print ("Your grade is: F")
