class PartX:
    def __init__(self, file_path=None):
        if file_path:
            with open(file_path) as file:
                self.data = [line.replace("\n", "") for line in file.readlines()]

    def run(self):
        ...


if __name__ == "__main__":
    PartX("./input.txt").run()