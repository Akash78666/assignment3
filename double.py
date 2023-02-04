def removing(mylist):
    mylist2=[]
    for x in mylist:
        if x not in mylist2:
            mylist2.append(x)
    
    for z in mylist2:
        print(z,end=" ")
a=[4,5,6,6]
removing(a)