import re


class Part1:
    def __init__(self, file_path):
        if file_path:
            with open(file_path) as file:
                self.data = [line.replace("\n", "") for line in file.readlines()]

    def run(self):
        pattern = r"\w*mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
        answer = sum(
            [
                sum([int(x) * int(y) for x, y in re.findall(pattern, line)])
                for line in self.data
            ]
        )
        print(f"Part 1 answer: {answer}")


class Part2:
    def __init__(self, file_path):
        if file_path:
            with open(file_path) as file:
                self.data = [line.replace("\n", "") for line in file.readlines()]

    def find_result(self, line):
        pattern = r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)"
        matches = re.finditer(pattern, line)
        result = []

        # Filter matches to "(x,y), don't(), and do()"
        for match in matches:
            if match.group(1) and match.group(2):
                result.append((match.group(1), match.group(2)))
            elif match.group(0) == "don't()":
                result.append(("don't()",))
            elif match.group(0) == "do()":
                result.append(("do()",))

        return result

    def run(self):
        answer = 0
        is_disabled = False
        results = [self.find_result(line) for line in self.data]
        for result in results:
            for i in range(len(result)):
                if result[i] == ("don't()",):
                    is_disabled = True
                    continue
                elif result[i] == ("do()",):
                    is_disabled = False
                    continue
                if not is_disabled:
                    answer += int(result[i][0]) * int(result[i][1])
        print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    Part1("./input.txt").run()
    Part2("./input.txt").run()
