feet = int(input('Enter Distance in feet:'))
inches = int(input('Enter Distance in inches:'))

meter = (feet * 0.3048) + (inches *0.0254)
centimeter = (meter * 100)

print(f'Distance in meter is {meter}')
print(f'Distance in centimeter is {centimeter}')