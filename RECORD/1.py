f=open("SCHOOL.txt","r")
g=f.read()
v=['a','e','i','o','u','A','E','I','O','U']
vcount=0
ccount=0
ucount=0
lcount=0
print(g)
for i in g:
    if i in v:
        vcount+=1
    elif i not in v and i!=" ":
        ccount+=1
for i in g:
    if i!=" ":
        if i.isupper():
            ucount+=1
        else:
            lcount+=1        
print(ccount)
print(vcount)
print(ucount)
print(lcount)
f.close()

        
    
    
    
