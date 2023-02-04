def add(n):
    if n==0:
        return 0
    return n+add(n-1)
n=int(input("please in the no:"))
print("sum of frist n number is",add(n))
