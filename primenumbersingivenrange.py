n1=int(input("Enter Start Number"))
n2=int(input("Enter End Number"))

def isprime(n):
    ct=0
    for i in range(1,n+1):
        if(n%i==0):
            ct=ct+1
    if(ct==2):
        return True
    else:
        return False

for i in range(n1,n2):
    if(isprime(i)):
        print(i)

