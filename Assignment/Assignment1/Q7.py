m1 = int(input('Enter marks of sub1:'))
m2 = int(input('Enter marks of sub2:'))
m3 = int(input('Enter marks of sub3:'))
m4 = int(input('Enter marks of sub4:'))
m5 = int(input('Enter marks of sub5:'))

gain_marks = m1 + m2 + m3 + m4 + m5

per = (gain_marks / 500) * 100

print(f'percentage is {per}%')