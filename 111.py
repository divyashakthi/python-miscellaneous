#LIST UPDATION
#R.DIVYA SHAKTHI XII H

print("LIST UPDATION")
print("_____________")
print("\nINPUT DATA")
print("__________\n")
n=int(input("Number of records"))
l=[]
for i in range(n):
    tab=eval(input("Enter tablet name and price"))
    l+=tab
    for j in l:
        for k in range(len(l)-1):
            for m in range(0,len(l)-k-1):
                if l[m]>l[m+1]:
                    l[m],l[m+1]=l[m+1],l[m]
print(l)

for i in range(len(l)):
    if l[i][1]>50:
        l[i][0]+="+"
print(l)


s=0
for i in range(len(l)):
    s+=l[i][1]
print(s)


for i in range(len(l)):
    dos=l[i][0]
print(dos)


m=["p","P"]
for i in l:
    if i[0][0] in m:
        l.remove(i)
print(l)


    
    
                
    

    
