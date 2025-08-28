days = int(input('Enter Days:'))

year = days // 365
days = days % 365
week = days // 7
days = days % 7

print(f'Total Year:{year}')
print(f'Weeks: {week}')
print(f'Days: {days}')