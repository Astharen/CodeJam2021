import numpy as np


def results():
    t = int(input())
    for i in range(1, t+1):
        N, C = [int(s) for s in input().split(" ")]
        max_value = get_max_value(N)

        if C > max_value or C < (N-1):
            vector = []
        else:
            vector2 = get_vector_with_max_value(N)
            max_value = get_max_value(N)
            n1, n2 = getting_n1_n2(max_value, C, N)
            vector = prueba_permutaciones(vector2, n=n1, init_n=n2)
            vector = list(map(str, vector))
        if len(vector)>1:
            sol = ' '.join(vector)
            # print(value_permutations(vector)==str(C))
        else:
            sol = 'IMPOSSIBLE'
        print (f'Case #{i}: {sol}')

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
    # value = value_permutations(list(arr))
    return list(arr)

# N = 8
# C = 18

# vector = get_vector_with_max_value(N)
# max_value = get_max_value(N)

#for n2 in range(3, 5):
#    for n1 in range(1, 6):
#        print(n1, n2)
#        print(prueba_permutaciones(vector, n=n1, init_n=n2))


def getting_n1_n2(max_value, C, N):
    supp_c = max_value
    n2 = 0
    for i in range(N-2, 0, -1):
        if supp_c <= C:
            n2 -= 1
            break
        n2 += 1
        supp_c -= i + 1
        # print(supp_c, n2)

    n1 =  C - supp_c
    return n1, n2


# print(getting_n1_n2(max_value, C, N))
# n1, n2 = getting_n1_n2(max_value, C, N)
# print(prueba_permutaciones(vector, n=n1, init_n=n2))

results()