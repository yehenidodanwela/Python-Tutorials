coursework = float (input ("Enter coursework marks: "))
if not (0 <= coursework <= 100):
    print ("Coursework marks must between (0-100)")
    exit()
midterm_exam = float (input ("Enter midterm exam marks: "))
if not (0 <= midterm_exam <= 100):
    print ("midterm_exam marks must between (0-100)")
    exit()
final_exam = float (input ("Enter final exam marks: "))
if not (0 <= final_exam <= 100):
    print ("final exam marks must between (0-100)")
    exit()

weighted_coursework = coursework * 40/100
weighted_midterm_exam = midterm_exam * 25/100
weighted_final_exam = final_exam * 35/100

final_grade = weighted_coursework + weighted_midterm_exam + weighted_final_exam

if (70 <= final_grade <= 100 ):
    print ("Your final numeric grade is: " + str(final_grade))
    print ("Your letter grade is: A")
elif (50 <= final_grade <= 69 ):
    print ("Your final numeric grade is: " + str(final_grade))
    print ("Your letter grade is: B")
elif (40 <= final_grade <= 49 ):
    print ("Your final numeric grade is: " + str(final_grade))
    print ("Your letter grade is: C")
else :
    print ("Your final numeric grade is: " + str(final_grade))
    print ("Your letter grade is: F")



