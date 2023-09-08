def factorial(num):
    if num == 1:
        return 1
    elif num==0:
        return 1
    else:
        return num * factorial(num - 1)
num = int(input("Enter a number: "))
result = factorial(num)
print(result)