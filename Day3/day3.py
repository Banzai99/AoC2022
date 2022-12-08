def part_one() -> int:
    f = open("input.txt")
    total_priority = 0
    for line in f:
        values = [x - 96 if 97 <= x <= 122 else x-38 for x in list(map(ord, list(line.replace("\n", ""))))]
        for val in values[:len(values)//2]:
            if val in values[len(values)//2:]:
                total_priority += val
                break
    f.close()
    return total_priority


def part_two() -> int:
    sacs = []
    total_priority = 0
    with open("input.txt") as f:
        for line in f:
            sacs.append([x - 96 if 97 <= x <= 122 else x-38 for x in list(map(ord, list(line.replace("\n", ""))))])
    for i in range(0, len(sacs), 3):
        for item in sacs[i]:
            if (item in sacs[i+1]) and (item in sacs[i+2]):
                total_priority += item
                break
    return total_priority


if __name__ == "__main__":
    print(part_one())
    print(part_two())
