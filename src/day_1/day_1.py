class Part1:
    def __init__(self, file_path):
        if file_path:
            with open(file_path) as file:
                self.data = [line.replace("\n", "") for line in file.readlines()]

    def run(self):
        sorted_left_list = sorted([int(line.split()[0]) for line in self.data])
        sorted_right_list = sorted([int(line.split()[1]) for line in self.data])
        total_distances = sum(
            [
                abs(sorted_left_list[i] - sorted_right_list[i])
                for i in range(len(sorted_left_list))
            ]
        )
        print(total_distances)


class Part2:
    def __init__(self, file_path):
        if file_path:
            with open(file_path) as file:
                self.data = [line.replace("\n", "") for line in file.readlines()]

    def run(self):
        sorted_left_list = sorted([int(line.split()[0]) for line in self.data])
        sorted_right_list = sorted([int(line.split()[1]) for line in self.data])
        similarity_scores = 0
        for left_number in sorted_left_list:
            count = 0
            for right_number in sorted_right_list:
                if left_number == right_number:
                    count += 1
            similarity_scores += left_number * count
        print(similarity_scores)


if __name__ == "__main__":
    Part1("./input.txt").run()
    Part2("./input.txt").run()
