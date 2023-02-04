n=int(input("please in the mark price:"))
discount=int(input("Please enter the discount percent"))
discount=n*discount*0.01
actualPrice=n-discount
print("discount=",discount)
print("Total amount ",actualPrice)


