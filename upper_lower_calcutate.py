def string_test(s):
    d={"Upper_case":0, "Lower_case":0}
    for c in s:
        if c.isupper():
            d["Upper_case"]+=1
        elif c.islower():
            d["Lower_case"]+=1
        else:
            pass
n=input("please enter the letter:")
print("no.Upper_case:",d["Upper_case"])
print("no.Lower_case:",d["Lower_case"])
print(string_test)
