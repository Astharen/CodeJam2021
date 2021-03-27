import numpy as np


def value_permutations(data):
    data_list = list(data).copy()
    new_data = list(data).copy()
    value = 0
    perm_list = []
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
        perm_list.append(new_data)
    return str(value)


def results(N, C):
    max_value = get_max_value(N)

    if C > max_value or C < (N-1):
        vector = []
    elif C == max_value:
        vector = get_vector_with_max_value(N)
        vector = list(map(str, vector))
    elif C == (N-1):
        vector = list(range(1, N+1))   
        vector = list(map(str, vector))
    else:
        vector2 = get_vector_with_max_value(N)
        max_value = get_max_value(N)
        n1, n2 = getting_n1_n2(max_value, C, N)
        vector = prueba_permutaciones(vector2, n=n1, init_n=n2)
        vector = list(map(str, vector))
    if len(vector)>1:
        sol = ' '.join(vector)
        return value_permutations(vector)==str(C)
    else:
        return  True

def get_vector_with_max_value(N, init_number=1):

    return list(range(init_number+1, N + 1, 2)) + list(reversed(list(range(init_number, N + 1, 2))))


def get_max_value(N):
    return N - 1 + np.sum(np.arange(1, N))


def prueba_permutaciones(vector, n=1, init_n=0):
    n += init_n
    new_vector2 = get_vector_with_max_value(len(vector), init_n+1)
    new_vector = list(range(1, init_n + 1))
    v = new_vector + new_vector2

    arr = np.array(v)
    new_array = arr[arr>n][::-1]
    arr[arr>n] = new_array
    return list(arr)

def getting_n1_n2(max_value, C, N):
    supp_c = max_value
    n2 = 0
    for i in range(N-2, 0, -1):
        n2 += 1
        supp_c -= i + 1
        if supp_c <= C:
            n2 -= 1
            break

    n1 =  C - supp_c
    return n1, n2