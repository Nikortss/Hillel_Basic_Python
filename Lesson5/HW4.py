from random import randint
count = 0
random_list = [randint(0, 100) for i in range(20)]
print(random_list)
for i in range(len(random_list)):
    if random_list[i] % 2 != 0:
        count += 1
        random_list[i] = 0
print(random_list)
print(f'Quantity of odd numbers: {count}')
