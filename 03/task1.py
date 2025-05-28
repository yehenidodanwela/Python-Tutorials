gross_income = float (input ("Enter your gross income: "))

if (gross_income <= 12500):
    tax = 0
    net_income = gross_income
    print ("Tax owed: " + str(tax))
    print ("No tax deduction, Your net income is: " + str(net_income))
elif (12500 < gross_income <= 50000):
    tax = (gross_income - 12500)* (20/100)
    net_income = gross_income - tax
    print ("Tax owed: " + str(tax))
    print ("Your net income after tax deduction is : " + str(net_income))
elif (50000 < gross_income <= 150000):
    tax = (gross_income - 50000)*(40/100) + (50000-12500)*(20/100)
    net_income = gross_income - tax
    print ("Tax owed: " + str(tax))
    print ("Your net income after tax deduction is : " + str(net_income))
else :
    tax = (gross_income-150000)*(45/100) + (150000-50000)*(40/100) + (50000-12500)*(20/100)
    net_income = gross_income - tax
    print ("Tax owed: " + str(tax))
    print ("Your net income after tax deduction is : " + str(net_income))
    
