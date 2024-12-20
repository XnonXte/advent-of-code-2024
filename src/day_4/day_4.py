from sys import argv, exit


class Part1:
    def __init__(self, file_path=None):
        if file_path:
            with open(file_path) as file:
                self.data = [line.strip() for line in file.readlines()]

    def run(self):
        answer = 0
        rows, cols = len(self.data), len(self.data[0])
        for i in range(rows):
            for j in range(cols):
                if self.data[i][j] == "X":
                    # Horizontal non-inverted XMAS
                    if j + 3 < cols and self.data[i][j + 1 : j + 4] == "MAS":
                        answer += 1

                    # Horizontal inverted XMAS
                    if j - 3 >= 0 and self.data[i][j - 3 : j] == "MAS"[::-1]:
                        answer += 1
                    # Vertical upward XMAS
                    if i - 3 >= 0 and all(
                        self.data[i - k][j] == c for k, c in enumerate("MAS", 1)
                    ):
                        answer += 1

                    # Vertical downward XMAS
                    if i + 3 < rows and all(
                        self.data[i + k][j] == c for k, c in enumerate("MAS", 1)
                    ):
                        answer += 1

                    # Diagonal top right XMAS
                    if (
                        i - 3 >= 0
                        and j + 3 < cols
                        and all(
                            self.data[i - k][j + k] == c for k, c in enumerate("MAS", 1)
                        )
                    ):
                        answer += 1

                    # Diagonal top left XMAS
                    if (
                        i - 3 >= 0
                        and j - 3 >= 0
                        and all(
                            self.data[i - k][j - k] == c for k, c in enumerate("MAS", 1)
                        )
                    ):
                        answer += 1

                    # Diagonal bottom right XMAS
                    if (
                        i + 3 < rows
                        and j + 3 < cols
                        and all(
                            self.data[i + k][j + k] == c for k, c in enumerate("MAS", 1)
                        )
                    ):
                        answer += 1
                    # Diagonal bottom left XMAS
                    if (
                        i + 3 < rows
                        and j - 3 >= 0
                        and all(
                            self.data[i + k][j - k] == c for k, c in enumerate("MAS", 1)
                        )
                    ):
                        answer += 1

        print(f"Total XMAS: {answer}")


class Part2:
    def __init__(self, file_path=None):
        if file_path:
            with open(file_path) as file:
                self.data = [line.strip() for line in file.readlines()]

    def run(self):
        answer = 0
        possible_x_shaped_mas = ["MSAMS", "SSAMM", "MMASS", "SMASM"]
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                try:
                    top_left = self.data[i][j]
                    top_right = self.data[i][j + 2]
                    center = self.data[i + 1][j + 1]
                    bottom_left = self.data[i + 2][j]
                    bottom_right = self.data[i + 2][j + 2]
                    combined = (
                        top_left + top_right + center + bottom_left + bottom_right
                    )
                    if combined in possible_x_shaped_mas:
                        answer += 1
                except IndexError:
                    continue
        print(f"Total X shaped MAS: {answer}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: <input>")
        exit(1)
    file_path = argv[1]
    Part1(file_path).run()
    Part2(file_path).run()
    exit(0)

