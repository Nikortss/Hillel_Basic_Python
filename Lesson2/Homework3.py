VasyaSpeed = int(input('Enter the speed of Vasya: '))
HoursofRide = int(input('Enter how many hours he drives: '))
Vasyaposition = abs(VasyaSpeed * HoursofRide)
if VasyaSpeed > 0:
    print('Vasya is on this position now - ' + str(Vasyaposition))
    if Vasyaposition > 100:
        print('Man, you are too far, come back')
else:
    print("You're moving in wrong direction! You drive already " + str(Vasyaposition) + ' km in opposite side')
