d=input("Enter a list")
def elem(d):
    for i in range(len(d)):
        if d[i].isdigit()=="True":
            i=str(i)+str(i)+str(i)
            print(i)
        elif d[i].isalpha()=="True":
            i+=str("#")
print("List before modification:",d)
elem(d)
print("\nList after modification:",d)
            
    
