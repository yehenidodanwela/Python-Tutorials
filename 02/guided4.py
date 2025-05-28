length = float (input("Enter the legnth of the cuboid: "))
width = float (input("Enter the width of the cuboid: "))
height = float (input("Enter the height of the cuboid: "))

surface_area = (length * width + length * height + width * height)* 2
perimeter_of_the_base = (length + width)*2
volume = length * width * height

print ("Surface area of your cuboid is:" + " " + str(surface_area))
print ("Perimeter of the base of your cuboid is:" + " " + str(perimeter_of_the_base))
print ("Volume of your cuboid is:" + " " + str(volume))
