#swap two numbers using third variable
no1 = int(input("Enter Number:"))
no2 = int(input("Enter Number:"))

print(f"Before Swapping no1=",no1, "no2=",no2)

c = no1
no1 = no2
no2 = c

print(f"After Swapping no1=",no1, "no2=",no2)