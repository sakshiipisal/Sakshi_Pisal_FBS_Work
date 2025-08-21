length = int(input('Enter the length:'))
breadth = int(input('Enter the breadth:'))
radius = int(input('Enter the radius:'))

area = length * breadth + 1/2*3.14*radius**2
perimeter = 2*length+breadth+3.14*radius

print(f'Area of rec {area}')
print(f'perimeter of rec {perimeter}')