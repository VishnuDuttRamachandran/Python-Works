#program that replicates the work of a calculator in basic operations(+,-,*,/)
ch=input("Hi there!!! Please enter the Mathematial operation to perform(+,-,*,/): ")
if ch=='+':
    n=int(input("Enter the number of numbers to add: "))
    sum=0
    for i in range(n):
        num=int(input("Enter the number: "))
        sum+=num
        result=sum
elif ch=='-':
    n=int(input("Enter the number of numbers to subtract: "))
    dif=0
    for i in range(n):
        num=int(input("Enter the number: "))
        dif=num-dif
        result=dif
elif ch=="*":
    prod=1
    n=int(input("Enter the number of numbers to multiply: "))
    for i in range(n):
        num=int(input("Enter the number: "))
        prod*=num
        result=prod
elif ch=='/':
    n=int(input("Enter the number of numbers to divide: "))
    div=1
    for i in range(n):
        num=int(input("Enter the number: "))
        div/=num
        result=div
else:
    for i in range(3):
        print("Wrong Input!!! Enter the appropriate operator to continue!!!")
    print("Number of tries exceeded!!!Killing the program!!!")
    quit()
print("The result is:",result)
        
