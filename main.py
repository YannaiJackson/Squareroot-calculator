import math

a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))

s = math.pow(b,2)
t = s - (4*a*c)
y = math.sqrt(t)
X1 = (-b-y)/(2*a)
X2 = (-b+y)/(2*a)

print("X1 = "+str(X1))
print("X2 = "+str(X2))