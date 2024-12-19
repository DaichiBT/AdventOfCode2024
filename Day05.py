import re


def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day05Input")

grid = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)

count = 0
string = " ".join(file_data)
splitup = string.split("|")


print(splitup)