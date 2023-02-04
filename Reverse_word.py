n=int(input("input a word:-"))
def reverse(n):
 for char in range(len(n)-1,-1,-1):
    print(n[char],end="")
print(reverse(n))