def figure_area(first_side, second_side, figure_type):
    area = 0
    if figure_type == 'T' or figure_type == 't':
        area = first_side * second_side / 2
    elif figure_type == 'S' or figure_type == 's':
        area = first_side ^ 2
    else:
        print('Wrong figure')
    return area


figure_type = input("Enter type of figure. 'T' if it's triangle and 'S' if it's square: ")
first_side = int(input('Enter the value of first side: '))
second_side = int(input('Enter the value of second side: '))
area = figure_area(first_side, second_side, figure_type)
if area:
    print(f'Area of figure is {area}')
