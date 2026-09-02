print("---------------------------------")
print("Program to derive greatest number")
print("--------------------------------=")

print("Enter the numbers:")
a=int(input("First Number:"))
b=int(input("Second Number:"))
c=int(input("Third Number:"))
if a==b and b==c:
 print("all three numbers are equal")
elif a==b and b>c:
 print("The greatest number is:",a)
elif a==c and c>b:
 print("The greatest number is:",a)
elif b==c and c>a:
 print ("The greatest number is:",b)
elif a>b and a>c:
 print("The greatest number is:",a)
elif b>a and b>c:
 print("The greatest number is:",b)
else: 
 print("The greatest number is:",c)