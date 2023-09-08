int_a=[]
for i in range(10):
    n=int(input("Enter a number"))
    int_a.append(n)
x=int(input("Enter a number which you want to search"))
for i in range(10):
    if x==int_a[i]:
        print("the value at index:",i)