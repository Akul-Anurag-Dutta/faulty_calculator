#Faulty Calculator 

print("Enter the first number")
num1 = int(input())
print("Enter the second number")
num2 = int(input())
print("What do want to do! +, -, *, /")
sum = input()

if num1==5 and num2==5 and sum=='+':
    print("Result is = 100")
if num1==50 and num2==5 and sum=='-':
    print("Result is = 35")
if num1==10 and num2==2 and sum=='*':
    print("Result is = 30")
if num1==100 and num2==100 and sum=='/':
    print("Result is = 0.1")
elif sum=='+':
    Result= num1+num2
    print(Result)
elif sum=='-':
    Result2= num1-num2
    print(Result2)
elif sum=='*':
    Result3= num1*num2
    print(Result3)
elif sum=='/':
    Result4= num1/num2
    print(Result4)

