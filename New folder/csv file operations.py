import csv
with open("employee.csv","w",newline="")as f:
    cw=csv.writer(f)
    cw.writerow(["employee id","employee name","salary"])
    n=int(input("Enter number of employees:"))
    for i in range(n):
        emp_id=int(input("Enter emp id"))
        name=str(input("Enter employee name"))
        sal=input("Enter salary")
        l=[emp_id,name,sal]
        cw.writerow(l)
with open("employee.csv","r",newline="")as f:
    cr=csv.reader(f)
    for i in cr:
        if i[2]!="salary":
            if int(i[2])>5:
                print(i)
        
