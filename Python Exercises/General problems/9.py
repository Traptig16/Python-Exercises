int_a=[]
for i in range(10):
    n=int(input("Enter a number"))
    int_a.append(n)
int_asc=sorted(int_a)
print("SORTED ARRAY IN ASCENDING ORDER:",int_asc)
int_dsc=sorted(int_a,reverse=True)
print("SORTED ARRAY IN DESCENDING ORDER:",int_dsc)