def is_prime(number):
    smlst_prime = 2
    while number % smlst_prime != 0:
        smlst_prime += 1
    return smlst_prime == number
number = int(input('Enter your number: '))
print(is_prime(number))
