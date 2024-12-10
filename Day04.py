import re


def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day04Input")

grid = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)

count = 0
x_count = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == "X":
            x_count += 1

print(x_count)