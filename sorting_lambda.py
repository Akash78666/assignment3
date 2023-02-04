x=lambda a,b:a+b
y=lambda a,b:a-b
z=lambda a,b:a*b
A=lambda a,b:a/b
a=int(input("please enter the number:"))
operator=input("please enter operator:")
b=int(input("please enter the number:"))
if operator=="+":
    print(x(a+b))
elif operator=="-":
    print(y(a,b))
elif operator=="*":
    print(z(a,b))
else:
    print(A(a,b))

