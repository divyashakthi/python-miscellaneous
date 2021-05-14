n=int(input("Enter value of n:"))
r=int(input("Enter value of r:"))
f=1
d=1
p=1
for i in range(1,n+1):
    f*=i
for j in range(1,r+1):
    d*=j
s=n-r
for k in range(1,s+1):
    p*=k
ncr=f/(d*p)
print("The binomial coefficient of",n,"and",r,"is",ncr)
