v=["a","e","i","o","u"]
vd=[]
uc=[]
spl_ch=[]
end_dig=[]
f=open(r"C:\Users\Dell\Desktop\s1.txt","w+")
f.seek(0)
f.write("sulphuric acid&2\n")
f.write("HCl$1\n")
f.write("nitric acid@3\n")
f.seek(0)
for i in f:
    for j in i:
        if j in v:
            vd.append(j)
        else:
            continue
print(len(vd))
f.seek(0)
for k in f:
    for l in k:
        if l.isupper():
            uc.append(l)
        else:
            continue
print(len(uc))
f.seek(0)
for a in f:
    for b in a:
        if b.isalnum():
            continue
        else:
            spl_ch.append(b)
print(len(spl_ch))
f.seek(0)
yh=f.readlines()
for sd in yh:
    for fg in sd:
        print(sd[len(sd)-1])

    
    
    
