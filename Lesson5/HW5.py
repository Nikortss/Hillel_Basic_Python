def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = (2 ** 0.5) * side
    results = (perimeter, area, diagonal)
    return results


side = int(input('Enter the size of square: '))
print(square(side))
