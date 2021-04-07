def runner(initial_distance, current_distance):
    day_number = 1
    while True:
        initial_distance = initial_distance + initial_distance * 1.1
        day_number += 1
        if initial_distance >= current_distance:
            return day_number

