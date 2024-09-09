a=int(input("enter a number: "))
b=int(input("enter a number: "))
operator=input("enter the operator(+,-,*,/,%): ")
if operator=="+":
    sum=a+b
    print("answer= ",sum)
elif operator=="-":
    difference=a-b
    print("answer= ",difference)
elif operator=="*":
    multiplication=a*b
    print("answer= ",multiplication)
elif operator=="/":
    division=a/b
    print("answer= ",division)
elif operator=="%":
    module=a%b
    print("answer= ",module)
else:
    print(f"unknown operator.please enter the appropriate operator!!")