target_saving_goal = float (input("Enter your target saving goal: "))
current_saving_amount = float (input("Enter your current saving amount: "))
monthly_saving_amount = float (input("Enter your monthly saving amount: "))

months = (target_saving_goal - current_saving_amount) / monthly_saving_amount

print ("It will take approximately" + " " + str (round(months)) +" "+ "months to reach your goal")

