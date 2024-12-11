def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def get_total(file_data):
    left_list = []
    right_list = []

    for line in file_data:
        numbers = line.split()
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))

    left_list.sort()
    right_list.sort()

    total = 0
    for i in range(len(left_list)):
        total += abs(left_list[i] - right_list[i])

    return total

file_data = get_file_data("Day01Input")

total = get_total(file_data)
print(total)
