import math
print(
    "1.add"
       
        "2. subtract"
       
        "3.multiplication"
       
      "4. division"
      
      "5. power"
      "6. exponential"
      "7. Trignometric function"
      "8. factorial"
"9. end")


for i in range(1,100):
    c=int(input("enter operator no."))
    if c==9:
      break
    else:

           if c==1:
            a = int(input("enter 1st no"))
            b = int(input("enter 2nd no."))
            print(a+b)
           elif c==2:
               a = int(input("enter 1st no"))
               b = int(input("enter 2nd no."))
               print(a-b)
           elif c==3:
               a = int(input("enter 1st no"))
               b = int(input("enter 2nd no."))
               print(a*b)
           elif c==4:
               a = int(input("enter 1st no"))
               b = int(input("enter 2nd no."))
               print(a/b)

           elif c==5:
               a = int(input("enter base  no"))
               b = int(input("enter power no."))
               print(pow(2,2))
           elif c==6:
               a = int(input("enter 1st no"))
               print(math.exp(a))
           elif c==7:
               d=input("enter trignometric function")
               a=int(input("enter a no."))
               if  d == 'sin':
                   print (math.sin(a))
               elif d == 'cos':
                    print(math.cos(a))
               elif  d == 'tan':
                    print(math.tan(a))
               elif d == 'cot':
                   print(math.cot(a))
               elif d == 'sec':
                   print(math.sec(a))
               elif d == 'cosec':
                   print(math.cosec(a))
           elif c==8:
               a=int(input("enter a no."))
               print(math.factorial(a))
           elif c == 9:
               print("end")



