import re


def part_one() -> int:
    pairs = []
    counter = 0
    with open("input.txt") as f:
        for line in f:
            pairs.append(list(map(int,re.split("[,-]", line.replace("\n", "")))))
    for pair in pairs:
        if ((pair[0] <= pair[2]) and (pair[1] >= pair[3])) or ((pair[0] >= pair[2]) and (pair[1] <= pair[3])):
            counter += 1
    return counter


def part_two() -> int:
    pairs = []
    counter = 0
    with open("input.txt") as f:
        for line in f:
            pairs.append(list(map(int,re.split("[,-]", line.replace("\n", "")))))
    for pair in pairs:
        if (pair[2] <= pair[1]) and (pair[3] >= pair[0]):
            counter += 1
    return counter


if __name__ == "__main__":
    print(part_one())
    print(part_two())
