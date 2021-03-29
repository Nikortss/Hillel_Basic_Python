listOfNumbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
userNumber = abs(float(input('Enter your number: ')))
if userNumber in listOfNumbers:
    print('Number is in the list')
else:
    print('Try another number')
