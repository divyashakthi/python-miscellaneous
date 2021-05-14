f=open("school.txt","r+")
m=open("myschool.txt","w+")
'''s=eval(input("Enter info about school"))
for i in s:
    f.write(i)
    f.write("\n")'''
print(f.read())
l=[]
p=f.readlines()
print(p)
for i in p:
    for j in i:
        if j=="T":
            p.remove(i)
            l.append(i)
        else:
            continue
m.writelines(l)
f.close()
m.close()


            
            
