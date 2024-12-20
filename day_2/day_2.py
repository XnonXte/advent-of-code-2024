class Part1:
    def __init__(self, file_path=None):
        if file_path:
            with open(file_path) as file:
                self.data = [line.replace("\n", "") for line in file.readlines()]
                self.reports = [
                    [int(level) for level in report.split(" ")] for report in self.data
                ]

    def check_first_rule(self, report):
        is_increasing = is_descending = False
        for i in range(len(report)):
            try:
                if report[i] > report[i + 1]:
                    is_descending = True
                else:
                    is_increasing = True
                if is_increasing and is_descending:
                    return False
            except IndexError:
                return True

    def check_second_rule(self, report):
        for i in range(len(report)):
            if i != 0:
                if not 1 <= abs(report[i] - report[i - 1]) <= 3:
                    return False
            if i + 1 != len(report):
                if not 1 <= abs(report[i] - report[i + 1]) <= 3:
                    return False
        return True

    def run(self):
        safe = [
            report
            for report in self.reports
            if self.check_first_rule(report) and self.check_second_rule(report)
        ]
        print(f"Save reports: {len(safe)}")


class Part2:
    def __init__(self, file_path=None):
        if file_path:
            with open(file_path) as file:
                self.data = [line.replace("\n", "") for line in file.readlines()]
                self.reports = [
                    [int(level) for level in report.split(" ")] for report in self.data
                ]
        self.part_1 = Part1()

    def problem_dampener(self, report):
        for i in range(len(report)):
            new_report = report[:i] + report[i + 1 :]
            if self.part_1.check_first_rule(
                new_report
            ) and self.part_1.check_second_rule(new_report):
                return True
        return False

    def run(self):
        unsafe_reports = [
            report
            for report in self.reports
            if not (
                self.part_1.check_first_rule(report)
                and self.part_1.check_second_rule(report)
            )
        ]
        dampened_reports = [
            report for report in unsafe_reports if self.problem_dampener(report)
        ]
        print(f"Dampened reports: {len(dampened_reports)}")


if __name__ == "__main__":
    Part1("./input.txt").run()
    Part2("./input.txt").run()
