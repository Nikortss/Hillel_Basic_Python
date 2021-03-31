decimal_number = input('Enter your number: ')
integer_part, decimal_part = decimal_number.split('.')
print(f'First number after point is: {int(float(decimal_number) * 10) % 10}')
print(f'Decimal part is: {decimal_part}')
