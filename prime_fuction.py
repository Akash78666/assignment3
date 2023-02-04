n=int(input("pleas enter the numbers:"))
def prime(num):
    if(n==1):
        return False
    elif(n==2):
        return True;
    else:
        for x in range(2,n):
            if(n%x==0):
                return False
        return True
print(prime(n))
