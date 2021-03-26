import numpy as np


def read_input():
    t = int(input()) # read a line with a single integer
    data_list = []
    for i in range(1, t+1):
        num_elements = int(input())
        data_list.append([int(s) for s in input().split(" ")])
    return data_list

def process_lines(x):
    x1 = x.split('/')[0]
    return list(map(int, x1.split()))


def reversort(data):
    data_list = list(data).copy()
    new_data = list(data).copy()
    value = 0
    for i in range(len(data)-1):
        data_list = new_data.copy()
        j = np.argmin(data_list[i:]) + i
        # print(j)
        # print(len(data_list))

        if i > 0:
            new_data = data_list[:i] + list(reversed(data_list[i:(j+1)]))
        else:
            new_data = list(reversed(data_list[i:(j+1)]))

        # print(new_data)
        if j < len(data_list):
            new_data += data_list[(j+1):]
        value += j - i + 1
        print(new_data)
    return str(value)

def write_output(values):
    content = ''
    for i in range(len(values)):
        content += f'Case #{i}: {values[i]}/n '
        print(f'Case #{i}: {values[i]}')
    write_txt(content)

def write_txt(text):
    with open('output.txt', 'w') as file:
        file.write(text)


def results():
    # a = input()
    # rows = np.array(a.split(' '))[2::2]
    # data_list = list(map(process_lines, rows))
    data_list = read_input()
    values = []
    for data in data_list:
        values.append(reversort(data))

    write_output(values)
    return values

results()