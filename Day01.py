def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def get_total(file_data):
    llist = []
    rlist = []

    for line in file_data:
        numbers = line.split()
        llist.append(int(numbers[0]))
        rlist.append(int(numbers[1]))

    llist.sort()
    rlist.sort()

    total = 0
    for i in range(len(llist)):
        total += abs(llist[i] - rlist[i])

    return total

file_data = get_file_data("Day01Input")

total = get_total(file_data)
print(total)
