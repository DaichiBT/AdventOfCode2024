def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


def check(num):
    levels = list(map(int, num.split()))

    for i in range(len(levels) - 1):
        if abs(levels[i] - levels[i + 1]) < 1 or abs(levels[i] - levels[i + 1]) > 3:
            return False

    increasing = True
    decreasing = True
    for i in range(len(levels) - 1):
        if levels[i] > levels[i + 1]:
            increasing = False
        if levels[i] < levels[i + 1]:
            decreasing = False
    return increasing or decreasing

file_data = get_file_data("Day02Input")
safe_count = 0

for report in file_data:
    if check(report):
        safe_count += 1


print(safe_count)
