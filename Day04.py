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

validity = []

letters = ["X", "M", "A", "S"]

letter

vDirection = []
hDirection = []

# {r + 1, c}, {r + 1, c + 1}, {r

def checkLetter(letter):
    if grid[r + 1][c + 1] == letter:

    elif grid[r + 1][c - 1] == letter:

    


for r in range(len(grid)):
    for c in range(len(grid[r])):


print(x_count)