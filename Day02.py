def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day02Input")


# Safe if -
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

def is_decreasing(nums):
    return nums == sorted(nums, reverse=True)


def is_increasing(nums):
    return nums == sorted(nums, reverse=False)


def in_range(lower, upper, nums):
    inRange = True
    for elem in nums:
        if int(elem) <= lower or int(elem) >= upper:
            return False
    return inRange


count = 0

for element in file_data:
    iElement = element.split(" ")
    diff_list = []
    for x, y in zip(iElement[0::], iElement[1::]):
        diff_list.append(abs(int(y) - int(x)))

    if is_increasing(iElement) or is_decreasing(iElement):
        if in_range(1, 3, diff_list):
            count += 1

print(count)
