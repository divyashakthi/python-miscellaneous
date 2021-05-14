with open("SCHOOL.txt","w+")as f:
    info=str(input("Enter school info:\t"))
    s=info.split(". ")
    l=[]
    for i in s:
        i+="\n"
        l.append(i)
    f.writelines(l)
    
with open("SCHOOL.txt","r")as f:
    red=f.readlines()
    for i in red:
        print(i,"\n")
print("______________________________")

with open("SCHOOL.txt","r")as f:
    with open("MYSCHOOL.txt","w+") as d:
        red=f.readlines()
        p=[]
        n = len(red)
        for i in range(n):
            if "T" in red[i]:
                p.append(red[i])
        for i in p:
            red.remove(i)
        d.writelines(p)    
                
    with open("MYSCHOOL.txt","r")as g:
        dred=g.readlines()
        for i in dred:
            print(i,"\n")
