a=int(input())
x=(a%10)
y=(a/10)
z=(x**2)+(y**2)
print(z)
b=z/10
if(b==0 or b==1 or b==9) and z%2==0 :
    print("beautiful number")
else:
    print("not a beautiful number")
