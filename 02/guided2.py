current_salary = float (input("Enter your current salary: "))
increase_percentage = float(input ("Enter your salary increase percentage (If your salary increase percentage is 5.6% enter 5.6): "))/100
new_salary = current_salary + current_salary * increase_percentage
print ("Your new salary is:" + " " + str (new_salary))
