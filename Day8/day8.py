import numpy as np


def part_one() -> None:
    carte = []
    scenic_scores_map = []
    visible_trees = 0
    with open("input.txt") as f:
        for line in f:
            carte.append([int(tree) for tree in line.rstrip("\n")])
    carte = np.array(carte)
    # visible_trees += sum(carte.shape)*2

    for i in range(carte.shape[0]):
        for j in range(carte.shape[1]):
            map_test = carte[i, j] > carte
            left = map_test[i, 0:j]
            right = map_test[i, j+1:map_test.shape[1]]
            up = map_test[0:i, j]
            down = map_test[i+1:carte.shape[0], j]
            directions = [list(reversed(left)), right, list(reversed(up)), down]
            conditions = (left.all() or right.all() or up.all() or down.all())
            if conditions.any():
                visible_trees += 1
            view_distances = []
            for direction in directions:
                view_distance = 0
                if not len(direction):
                    view_distances.append(0)
                for tree in direction:
                    if tree:
                        view_distance += 1
                    else:
                        view_distance += 1
                        break
                view_distances.append(view_distance)
            scenic_scores_map.append(np.prod(view_distances))
    scenic_scores_map = np.array(scenic_scores_map).reshape(carte.shape[0], carte.shape[1])
    print(visible_trees)
    print(np.max(scenic_scores_map))


if __name__ == "__main__":
    part_one()
