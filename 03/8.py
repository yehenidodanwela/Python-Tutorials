purchase_amount = float (input ("Enter the purchase amount: "))

if purchase_amount > 1000:
    discount = purchase_amount * (10/100)
    print ("10% Discount applied, Discount amount is ",discount )
elif 500 < purchase_amount < 1000:
    discount = purchase_amount * (5/100)
    print ("5% Discount applied, Discount amount is ",discount )
else :
    discount = 0
    print ("No discount")
