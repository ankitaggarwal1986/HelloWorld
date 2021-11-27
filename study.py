num = int(input("enter the number:"))
result = 1

if num<0:
    print("invalid input")
elif num == 0:
    print("factorial of zero is 1")
else:
    for i in range(1,num+1):
        result = result*i
    print("Factorial of",num,"is",result)        
