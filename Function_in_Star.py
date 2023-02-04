lineNumber=int(input())
i=lineNumber
for i in range(lineNumber,0,-1):
    for J in range(1,i+1):
        print(J," ",end="")
    print()
    i=i-1