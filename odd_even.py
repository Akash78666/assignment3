def checkEvenOrOdd(x):
    if x%2==0:
        return True
    else:
        return False
     
a=int(input("pleas enter the numbear which you want to check:"))
if(checkEvenOrOdd(a)):
    print("number is even")
else:
    print("number is odd")

    