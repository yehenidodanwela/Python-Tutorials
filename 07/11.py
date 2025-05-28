import math

def area_of_a_triangle (a,b,c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


print(area_of_a_triangle (2,3,4))  # checking for the results
