numberOfYear = int(input('Enter the year: '))
if (numberOfYear % 4) == 0 and (numberOfYear % 100) != 0:
    print('Yes')
elif numberOfYear % 400 == 0:
    print('Yes')
else:
    print('No')
