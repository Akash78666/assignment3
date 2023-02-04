n=int(input("please in the hearRate:\n"))
def my_heatRate(n):

    if n==100:
        print("Your heartRate is v.High. take a bed rest")
    elif n>72:
        print("Your heartRate is High. to advice to walk in the morning")
    elif n==72:
        print("Your heartRate is normal.to take eaten healthy diet")
    elif n<72:
        print("Your heartRate is low becaue your sufferend anxiety.join us happy grourp")
    else:
        print("your the healthy person.don't prescrible medicine")  
my_heatRate(n)

