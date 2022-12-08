def part_one_and_two() -> None:
    filesystem_dict = {}
    current_directory = ""
    to_remove = []
    with open("input.txt") as f:
        for line in f:
            command = line.rstrip("\n").split(" ")
            if command[1] == "cd":
                if command[2] == "/":
                    current_directory = ""
                elif command[2] == "..":
                    current_directory = current_directory[:-to_remove.pop()]
                else:
                    current_directory = current_directory + "/" + command[2]
                    to_remove.append(len("/" + command[2]))
                if (current_directory + "/") not in filesystem_dict.keys():
                    filesystem_dict[current_directory + "/"] = []
            if command[0] != "$":
                if command[0] == "dir":
                    filesystem_dict[current_directory + "/"].append({"dir_name": command[1]})
                else:
                    filesystem_dict[current_directory + "/"].append({"size": command[0], "file_name": command[1]})
        folders_sizes = {}
        for folder, elems in filesystem_dict.items():
            folder_size = 0
            for elem in elems:
                for key, value in elem.items():
                    if key == "size":
                        folder_size += int(value)
            folders_sizes[folder] = folder_size
        folders_sizes.update(sorted(folders_sizes.items(), key=lambda x: x.count("/")))
        for folder_name, size in folders_sizes.items():
            for name, size_to_add in folders_sizes.items():
                if (folder_name != name) and (folder_name in name):
                    folders_sizes[folder_name] += size_to_add
        final_sum = 0
        for key, value in folders_sizes.items():
            if value <= 100000:
                final_sum += value
        print("Final sum of directories part one :", final_sum)
        delete_size = min([a for a in folders_sizes.values() if a > 30000000 - (70000000-folders_sizes["/"])])
        print("Size of folder to delete for update :", delete_size)


if __name__ == "__main__":
    part_one_and_two()
