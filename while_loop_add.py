n=int(input("please enter the no:"))
for i in range(1500,2701):
    if(i%7==0)and(i%5==0):
        n.append(int(i))
print("divible no 5 and 7",n)

