p=[]
h=list(f)
for y in h:
    p.append(y.replace("\n",""))
print(p)
    
for x in p:
    x[len(x.rstrip("0123456789")):]
print(x)




for x in p:
    if x[-1].isdigit=="True":
        print(x[-1])
        end_dig.append(x[-1])
    else:
        continue
print(end_dig)
