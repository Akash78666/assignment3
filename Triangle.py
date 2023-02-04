x=int(input("pleas enter lenghts of the triangle:"))
y=int(input("pleas enter lenghts of the triangle:"))
z=int(input("pleas enter lenghts of the triangle:"))
if x==y==z:
    print("Equilateral Traingle")
elif x==y or y==z or x==z:
    print("isosceles Traingle")
else:
    print("Scalene Traingle")
