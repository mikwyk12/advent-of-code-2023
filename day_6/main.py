with open('input.txt') as file:
    lines = file.read().split('\n')


if __name__ == '__main__':
    time = lines[0].split(":")[1].split()
    distance = lines[1].split(":")[1].split()
    size = len(distance)

    races = [(int(time[i]), int(distance[i])) for i in range(size)]
    counter = 1

    for t, d in races:
        tmp = 0
        for car_speed in range(1, t):
            race_time = t - car_speed
            if car_speed * race_time > d:
                tmp += 1
        counter *= tmp

    print(f"Part One Answer: {counter}")

    time = lines[0].split(":")[1].replace(" ", '')
    distance = lines[1].split(":")[1].replace(" ", '')

    t, d = int(time), int(distance)

    counter = 0

    for car_speed in range(1, t):
        race_time = t - car_speed
        if car_speed * race_time > d:
            counter += 1

    print(f"Part Two Answer: {counter}")
