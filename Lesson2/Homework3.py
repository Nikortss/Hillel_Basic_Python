vasyaSpeed = int(input('Enter the speed of Vasya: '))
hoursOfRide = int(input('Enter how many hours he drives: '))
vasyaPosition = abs(vasyaSpeed * hoursOfRide)
if vasyaSpeed > 0:
    print('Vasya is on this position now - ' + str(vasyaPosition))
    if vasyaposition > 100:
        print('Man, you are too far, come back')
else:
    print("You're moving in wrong direction! You drive already " + str(vasyaPosition) + ' km in opposite side')
