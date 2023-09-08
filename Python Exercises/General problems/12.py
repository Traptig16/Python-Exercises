
a=[]
for i in range(5):
    c=int(input("enter numbers for a:"))
    a.append(c)
b=[]
for j in range(5):
    d=int(input("enter numbers for b:"))
    b.append(d)
if sorted(a)==sorted(b):
    print("array is equal in terms of elements")
else:
    print("array is not equal in terms of element")
if a==b:
    print("arrays is euqal in terms of element and position")
else:
    print("array is not equal in terms of element and position")

