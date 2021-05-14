f=open(r"sample.txt","w")
f.write("divya\n")
f.write("XII H\n")
f.write("SCIENCE")
f.close()
f=open(r"C:\Users\Dell\Desktop\sample.txt","r")
for i in range(2):
    s=f.readline()
    print(s)
