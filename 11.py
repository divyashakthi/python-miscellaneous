f=[]
tablet=eval(input("Enter a list of tablets"))
for i in tablet:
    f.append(i)
print(f)
for j in f:
    for k in j:
        if k.isdigit():
            continue
        else:
            del j[k]
            print(j)

        
    
