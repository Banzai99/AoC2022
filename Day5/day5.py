import numpy as np


def part_one() -> None:
    f_ready = []
    queues = []
    with open("input.txt") as f:
        for line in f:
            f_ready.append(line.rstrip("\n").replace("    ", " ").split(" "))
    data_table = [
        list("DTRBJLWG"),
        list("SWC"),
        list("RZTM"),
        list("DTCHSPV"),
        list("GPTLDZ"),
        list("FBRZJQCD"),
        list("SBDJMFTR"),
        list("LHRBTVM"),
        list("QPDSV")
    ]
    recette = f_ready[10:]
    for line in recette:
        number_to_move = int(line[1])
        start = int(line[3])-1
        destination = int(line[5])-1
        data_table[destination].extend(data_table[start][-number_to_move:][::-1])
        for _ in range(number_to_move):
            data_table[start].pop(-1)
    for line in data_table:
        print(line)


def part_two() -> None:
    f_ready = []
    queues = []
    with open("input.txt") as f:
        for line in f:
            f_ready.append(line.rstrip("\n").replace("    ", " ").split(" "))
    data_table = [
        list("DTRBJLWG"),
        list("SWC"),
        list("RZTM"),
        list("DTCHSPV"),
        list("GPTLDZ"),
        list("FBRZJQCD"),
        list("SBDJMFTR"),
        list("LHRBTVM"),
        list("QPDSV")
    ]
    recette = f_ready[10:]
    for line in recette:
        number_to_move = int(line[1])
        start = int(line[3]) - 1
        destination = int(line[5]) - 1
        data_table[destination].extend(data_table[start][-number_to_move:])
        for _ in range(number_to_move):
            data_table[start].pop(-1)
    for line in data_table:
        print(line)

if __name__ == "__main__":
    part_one()
    print("================================ Part 2 ================================")
    part_two()
