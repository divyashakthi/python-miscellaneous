with open("INDIA.txt","w+")as f:
    info=str(input("Enter info about India:\t"))
    s=info.split(".")
    k=[]
    for i in s:
        i+="\n"
        k.append(i)
    f.writelines(k)
with open("INDIA.txt","r")as f:
    red=f.readlines()
    print("Number of lines:\t",len(red))
    count=0
    for i in red:
        g=i.split()
        for j in g:
            if j=="India":
                count+=1
    print("Occurence of the word 'India':\t",count)
with open("INDIA.txt","r")as f:
    st=" "
    while st:
        st=f.readline()
        st=st.replace(" ","#")
        print(st,end="\n")
    
