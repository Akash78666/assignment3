print("Temperature Converter")
print("1. Fahrenhiet to Celcius")
print("2.Celcius to Fahrenhiet ")
print("3.Reaumur to celcoius ")
print("4.Celcious to Reaumar ")
print("5.Kelvin to celcius ")
print("6.Celcius to kinlvin ")
Choice=int(input("please Choose a ption"))
if Choice==1:
    tem=int(input("please enter the temperature in degree Fahrenhiet Scale:"))
    celcius=(tem-32)*5/9
    print("Temperature in celcius is",celcius)
elif(2):
    temp=int(input("please enter the temperature in degree Celcius Scale:"))
    Fahren=temp*9/5+32
    print=("Temperature in celcius is,",Fahren)
elif(3):
    temp=int(input("please enter the temperature in degree Celcius Scale:"))
    Reaumar=(4*temp)/5
    print("Temperature in celcius is,",Reaumar)
elif(4):
    temp=int(input("please enter the temperature in degree Reaumar Scale:"))
    celcius=(temp*5)/4
    print("Temperature in Reaumar is,",celcius)
elif(5):
    temp=int(input("please enter the temperature in degree Celcius Scale:"))
    kelvine=temp+273
    print=("Temperature in celcius,",kelvine)
else:
    temp=int(input("please enter the temperature in degree kelvine Scale:"))
    celcius=temp-273
    print=("Temperature in kelvine,",celcius)




    
