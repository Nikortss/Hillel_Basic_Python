NumberofYear = int(input('Enter the year: '))
if (NumberofYear % 4) == 0 and (NumberofYear % 100) != 0:
    print('Yes')
elif NumberofYear % 400 == 0:
    print('Yes')
else:
    print('No')
