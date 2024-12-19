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
stringOfAll = " ".join(file_data)
splitup = stringOfAll.split("|")

before = []


def get_char_before(string, char):
    index = string.find(char)
    if index > 0:
        before.append(string[index - 2] + string[index - 1])
    else:
        return None


def get_char_after(string, char):
    index = string.find(char)
    if index > 0:
        before.append(string[index + 1] + string[index + 2])
    else:
        return None


get_char_before(stringOfAll, '|')
get_char_after(stringOfAll, '|')

print(before)
