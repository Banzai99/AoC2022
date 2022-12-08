def part_one():
    window_size = 4
    with open("input.txt") as f:
        input = f.read().rstrip("\n")
    for i in range(0, len(input)):
        if len(set(input[i:i+window_size])) == window_size:
            print(str(i+window_size) + " characters processed")
            break
        else:
            pass


def part_two():
    window_size = 14
    with open("input.txt") as f:
        input = f.read().rstrip("\n")
    for i in range(0, len(input)):
        if len(set(input[i:i+window_size])) == window_size:
            print(str(i+window_size) + " characters processed")
            break
        else:
            pass


if __name__ == "__main__":
    part_one()
    part_two()
