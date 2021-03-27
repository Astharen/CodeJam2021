


def get_vector_with_max_value(N):
    j = 0
    vector = np.arange(1, N+1)
    pos1 = 0
    pos2 = 0
    supp_pos1 = 0
    supp_pos2 = 0
    for i in range(1, N+1):
        if i == 1:
            vector[-1] = i
            pos1 += 2
            supp_pos2 += 1
        elif supp_pos2 == 1:
            vector[pos2] = i
            supp_pos2 += 1
            pos2 += 1
        elif supp_pos2 == 2:
            vector[pos2] = i
            supp_pos2 = 0
            supp_pos1 = 1
            pos2 += 1
        elif supp_pos1 == 1:
            vector[-pos1] = i
            supp_pos1 += 1
            pos1 += 1
        elif supp_pos1 == 2:
            vector[-pos1] = i
            supp_pos1 = 0
            supp_pos2 = 1
            pos1 += 1
    return vector



def prueba_permutaciones2(vector, n=1):
    new_vector = list(range(1, n+1))
    new_vector2 = get_vector_with_max_value2(len(vector), n+1)
    v = new_vector + new_vector2
    print(v)
    return value(v)

def prueba_permutaciones2(vector, n=1, impar=True, init_n=1):
    new_vector2 = get_vector_with_max_value2(len(vector), n+1)
    
    if impar:
        new_vector = list(reversed(list(range(init_n, n+1))))
        v = new_vector2 + new_vector
    else:
        new_vector = list(range(init_n, n+1))
        v = new_vector + new_vector2
    print(v)
    return value(v)


def prueba_permutaciones3(vector, n=1, impar=True, init_n=1):

    arr = np.array(vector)
    new_array = arr[arr>n]
    new_vector2 = get_vector_with_max_value2(len(new_array) + n,  n+1)
    print(new_vector2, new_array)
    arr[arr>n] = np.array(new_vector2)
    return value(list(arr))


def prueba_permutaciones(vector):
    print(vector)
    new_vector = vector.copy()
    new_vector[1] = vector[3]
    new_vector[3] = vector[1]
    value, _ = value_permutations(new_vector)
    return value



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