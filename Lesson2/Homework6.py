ListOfNumbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
UserNumber = abs(float(input('Enter your number: ')))
if UserNumber in ListOfNumbers:
    print('Number is in the list')
else:
    print('Try another number')
