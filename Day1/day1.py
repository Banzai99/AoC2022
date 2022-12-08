if __name__ == "__main__":
    elf_calories = []
    sum_cal = 0
    with open(file="data/data.txt") as f:
        data = f.read()
        data_list = list(data.split("\n"))
        for calories in data_list:
            if calories:
                sum_cal += int(calories)
            else:
                elf_calories.append(sum_cal)
                sum_cal = 0
        print(max(elf_calories))
        elf_calories.sort()
        elf_calories.reverse()
        print(sum(elf_calories[0:3]))