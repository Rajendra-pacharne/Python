n1=int(input("Enter First Element"))
n2=int(input("Enter Second Element"))
n3=int(input("Enter Third Element"))

if(n1==n2 and n1==n3):
    print("Nuetral ")
elif(n1>n2 and n1>n3):
    print(n1," is max")
elif(n2>n1 and n2>n3):
    print(n2," is max")
else:
    print(n3,"is max")