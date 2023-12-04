with open('input.txt') as file:
    lines = file.read().strip().split('\n')

if __name__ == '__main__':
    cards = []
    counter = 0

    for line in lines:
        line = line.split(':')[1]
        points = 0
        tmp = 0

        win, have = line.split('|')
        win, have = win.split(), have.split()

        for elem in set(win):
            if elem in set(have):
                tmp += 1

        cards.append(tmp)

        if tmp > 0:
            points = 2**(tmp-1)

        counter += points

    print(f"Part 1 Answer: {counter}")
    size = len(cards)

    cards_points = [1 for _ in range(size)]
    arr = [i for i in range(size)]

    for elem in arr:
        if cards[elem] != 0:
            for i in range(cards[elem]):
                arr.append(elem+i+1)
                cards_points[elem+i+1] += 1

    print(f"Part 2 Answer: {sum(cards_points)}")
