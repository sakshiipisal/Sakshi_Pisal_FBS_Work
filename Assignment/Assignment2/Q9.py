#swap two number without using third variable
a = int(input("Enter number:"))
b = int(input("Enter number:"))

print(f"before swapping a:",a,"b:",b)
a , b = b , a

print("after swapping:",a,"b:",b)