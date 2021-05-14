def create(filename):
    with open(filename,"w+")as f:
        info=str(input("Enter school info:\t"))
        s=info.split(".")
        k=[]
        for i in s:
            i+="\n"
            k.append(i)
        f.writelines(k)
create("school.txt")

def view(filename):
    with open(filename,"r")as f:
        red=f.readlines()
        for i in red:
            print(i,"\n")
view("school.txt")

def remove(filename,file):
    with open(filename,"r")as f:
        with open(file,"w+")as d:
            red=f.readlines()
            for i in red:
                if "T" in i:
                    red.remove(i)
                    d.write(i)
    with open(file,"r")as g:
        p=g.readlines()
        for i in p:
            print(i,"\n")
remove("school.txt","myschool.txt")
            
    


        

            
