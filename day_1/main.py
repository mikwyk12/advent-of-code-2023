with open("input.txt", 'r') as file:
    lines = file.readlines()


def text2num(text: list[str]) -> list[list[int]]:
    result = []

    for sub in text:
        result.append([int(i) for i in sub if i.isdigit()])

    return result


def nums_counter(numbers: list[list[int]]) -> int:
    answer = 0

    for num in numbers:
        if len(num) > 1:
            answer += 10 * num[0] + num[-1]
        elif len(num) == 1:
            answer += 10 * num[0] + num[0]
        else:
            answer += 0

    return answer


def replace_words(text: list[str], numbers: dict[str, str]):
    i = 0
    for sub in text:
        for name, value in numbers.items():
            if name in sub:
                sub = sub.replace(name, value)
        text[i] = sub
        i += 1

    return text


if __name__ == '__main__':
    num = {
        'zero': 'z0o', 'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r',
        'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'
    }

    # PART 1
    res = text2num(lines)
    ans = nums_counter(res)
    print(f"First Part Answer: {ans}")

    # PART 2
    lines = replace_words(lines, num)
    res = text2num(lines)
    ans = nums_counter(res)
    print(f"Second Part Answer: {ans}")
