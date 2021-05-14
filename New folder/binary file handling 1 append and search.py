import pickle
f=open("student.dat","wb")
n=int(input("Enter number of records:"))
for i in range(n):
    rollno=int(input("Enter roll number:"))
    name=str(input("Enter name:"))
    gender=str(input("Enter gender:"))
    standard=int(input("Enter std:"))
    section=str(input("Enter section:"))
    marks=float(input("Enter total marks:"))
    print("\n")
    l=[rollno,name,gender,standard,section,marks]
    pickle.dump(l,f)
f.close()
f=open("student.dat","rb")
en=int(input("Enter roll number to be searched:"))
ld=[]
try:
    while True:
        ld=pickle.load(f)
        if ld[0]==en:
            print(ld)
except EOFError:
    f.close()


