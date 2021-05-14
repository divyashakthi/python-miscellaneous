with open("school.txt","w+")as f:
    info=str(input("Enter school info:\t"))
    s=info.split(".")
    l=[]
    for i in s:
        i+="\n"
        l.append(i)
    f.writelines(l)

with open("school.txt","r")as d:
    uc=0;lc=0;v=0;c=0
    vowels=['a','e','i','o','u','A','E','I','O','U']
    r=d.readlines()
    for i in r:
        for j in i:
            if j.isupper():
                uc+=1
            if j.islower():
                lc+=1
            if j in vowels:
                v+=1
            elif j.isalpha() and j not in vowels:
                c+=1
print("Number of upper case letters=\t",uc)
print("Number of lower case letters=\t",lc)
print("Number of vowels=\t",v)
print("Number of consonants=\t",c)
                
