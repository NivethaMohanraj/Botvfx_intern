#a=int(input("Enter a:" ))
#b=int(input("en b:" ))
#c=int(input("ent c: "))
a,b,c=int(input("Enter a:" )),int(input("Enter b:" )),int(input("Enter c:" ))
if(a==b==c):
    print("Equilateral Triangle")
elif(a!=b and b!=c and c!=a):
    print("Scalene Triangle")
else:
    print("Isosceles Triangle")
