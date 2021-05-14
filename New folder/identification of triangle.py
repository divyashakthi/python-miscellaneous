print("Identification of triangle")
print("Let x,y and z be the lengths of the sides of the triangle...")
def sides(x,y,z):
    if x==y==z:
        print("It is an equilateral triangle")
    elif x==y or y==z or x==z:
        print("It is an isosceles triangle")
    else:
        print("It is a scalene triangle")
x=int(input("Enter the value of x:\t"))
y=int(input("Enter the value of y:\t"))
z=int(input("Enter the value of z:\t"))
sides(x,y,z)

