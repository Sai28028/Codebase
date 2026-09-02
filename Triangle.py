print("------------------------------------------------")
print("Program for lengths of the sides of the triangle")
print("------------------------------------------------")

print("Enter the lengths of the sides of the triangle:")
a=int(input("First side:"))
b=int(input("Second side:"))
c=int(input("Third side:"))

if a+b<=c or a+c<=b or b+c<=a:
 print("It cannot form a triangle")
elif a==b and b==c:
 print("It is an Equilateral Triangle")
elif a>b and b==c:
 print("It is an Isosceles Triangle")
elif b>a and a==c:
 print("It is an Isosceles Triangle")
elif c>a and a==b:
 print("It is an Isosceles Triangle")
else: print("It is a Scalene Triangle")
