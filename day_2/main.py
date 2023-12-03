with open('input.txt', 'r') as file:
    lines = file.read().strip()


if __name__ == '__main__':
    condition = {'red': 12, 'green': 13, 'blue': 14}
    ans = 0

    # PART 1
    for line in lines.split('\n'):
        temp = True
        game_id, line = line.split(':')
        game_id = game_id.split()[1]
        for turn in line.split(';'):
            for ball in turn.split(','):
                n, color = ball.split()
                if int(n) > condition[color]:
                    temp = False
        if temp:
            ans += int(game_id)

    print(ans)
    ans = 0

    # PART 2
    for line in lines.split('\n'):
        num_of_cubes = {'red': 0, 'green': 0, 'blue': 0}
        temp = 1
        line = line.split(':')[1]
        for turn in line.split(';'):
            for ball in turn.split(','):
                n, color = ball.split()
                if int(n) > num_of_cubes[color]:
                    num_of_cubes[color] = int(n)
        for value in num_of_cubes.values():
            temp *= value
        ans += temp

    print(ans)
