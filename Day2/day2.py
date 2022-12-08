# A,X = Rock (1 point) / Lose
# B,Y = Paper (2 points) / Draw
# C,Z = Scissors (3 points) / Win
# Score round = shape selected + outcome (loss = 0, draw = 3, win = 6)

def compute_score_part1(ennemy:str, me:str) -> int:
    duel_score = 0
    if me == "X":
        duel_score += 1
        me = "A"
    elif me == "Y":
        duel_score += 2
        me = "B"
    else:
        duel_score += 3
        me = "C"
    if ennemy == me:
        duel_score += 3
    elif ((ennemy == "C") and (me == "A")) or ((ennemy == "A") and (me == "B")) or ((ennemy == "B") and (me == "C")):
        duel_score += 6
    else:
        pass
    return duel_score

def part_two():
    dictionary = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }
    file = open('data/input.txt', 'r')
    lines = file.readlines()

    value = 0
    for line in lines:
        line = line.strip()
        value += dictionary[line]

    return value


if __name__ == "__main__":
    score = 0
    with open("data/input.txt") as f:
        for line in f:
            line = line.replace("\n", "").split(" ")
            score += compute_score_part1(*line)
    print(part_two())