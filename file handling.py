f=open(r"C:\Users\Dell\Desktop\CHEM.txt","r")
print(f.readlines())
f.seek(0)
for i in range(2):
    print(f.readline(),end="*")
print(f.tell(),"th position")
print(f.read(3))
