print("welcome to maa Sweets")
print("pleas choose a item:")
print("1.Samoshe")
print("2.GulabJamun")
priceofSamosa=7
priceofGJ=15
n=int(input("pleas enter the number option 1/2:"))
numberOfItems=int(input("plese enter the number of iteme:"))
if(n==1):
      print("your total amount is",priceofSamosa*numberOfItems)
else:
    print("your total amount is",priceofGJ*numberOfItems)