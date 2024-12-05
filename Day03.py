import re

def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day03Input")

sum = 0

for element in file_data:
    x = re.findall('mul\([0-9]+,[0-9]+\)', element)
    for elem in x:
        nums = re.findall('[0-9]+', elem)
        sum += int(nums[0]) * int(nums[1])


print(sum)
