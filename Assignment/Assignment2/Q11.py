amt = int(input('Enter Amount:'))

min_notes = amt // 2000
# min_notes = amt % 2000
min_notes = amt // 500

print(f'min notes of 2000: {min_notes}')
print(f'min notes of 500: {min_notes}')