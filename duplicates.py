mylist=["apple","orange","apple","orange"]
while n<=mylist.count():
    j=i+1
    while j<=mylist.count():
        if mylist[i]==mylist[j]:
            mylist.remove(mylist[j])
    j=j+1
    i=i+1
print(mylist)