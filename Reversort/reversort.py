import numpy as np


def read_input():
    t = int(input())
    data_list = []
    for i in range(1, t+1):
        num_elements = int(input())
        data_list.append([int(s) for s in input().split(" ")])
    return data_list


def reversort(data):
    data_list = list(data).copy()
    new_data = list(data).copy()
    value = 0
    for i in range(len(data)-1):
        data_list = new_data.copy()
        j = np.argmin(data_list[i:]) + i
        if i > 0:
            new_data = data_list[:i] + list(reversed(data_list[i:(j+1)]))
        else:
            new_data = list(reversed(data_list[i:(j+1)]))

        if j < len(data_list):
            new_data += data_list[(j+1):]
        value += j - i + 1
    return str(value)

def write_output(values):
    content = ''
    for i in range(len(values)):
        content += f'Case #{i+1}: {values[i]}/n '
        print(f'Case #{i+1}: {values[i]}')
    write_txt(content)

def write_txt(text):
    with open('output.txt', 'w') as file:
        file.write(text)


def results():

    data_list = read_input()
    values = []
    for data in data_list:
        values.append(reversort(data))

    write_output(values)
    return values

results()