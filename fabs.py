import math
def execmain():
    x=eval(input("Enter a number:"))
    if (math.fabs(x)==x):
        print("You entered a positive number")
    else:
        x*=-1
        print("Number made positive:",x)
execmain()
