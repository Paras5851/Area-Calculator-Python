print("******AREA CALCULATOR******")

print('''Press 1 to get Area of Square
Press 2 to get Area of Rectangle
Press 3 to get Area of Circle
Press 4 to get Area of Triangle''')

a = int(input("Enter a Number Between 1-4: "))

if a == 1:
    side = float(input("Enter the Length of one side: "))
    area = side**2
    print("The Area of Square is: ",area)
elif a == 2:
    length = float(input("Enter the Length of the Rectangle: "))
    width = float(input("Enter the Width of the Rectangle: "))
    area = length*width
    print("The Area of Rectangle is: ",area)
elif a == 3:
    radius = float(input("Enter the Radius of the Circle: "))
    area = ((22/7)*(radius**2))
    print("The Area of circle is: ",area)
elif a == 4:
    Base = float(input("Enter the Base of the Triangle: "))
    Height = float(input("Enter the Height of the Triangle: "))
    area = 0.5*Base*Height
    print("The Area of Triangle is: ",area)
else:
    print("Invalid Input!!")