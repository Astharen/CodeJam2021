import numpy as np

def get_median_index(median_dict, index, vector, Q):
    index = tuple(index)
    if index not in median_dict.keys() and tuple(reversed(list(index))) not in median_dict.keys():
    
        supp_v = vector[list(index)]
        median = np.median(supp_v)
        median_index = np.where(median == vector)[0][0] 
        Q += 1
    else:
        if index in median_dict.keys():
            median_index = median_dict[index]
        elif tuple(reversed(list(index))) not in median_dict.keys():
            median_index = median_dict[list(reversed(index))]
    return median_index, Q

def get_sorted_list(vector):

    sorted_list = []
    sorted_vector = np.sort(vector)

    for i in range(len(vector)):
        sorted_list.append(np.where(sorted_vector[i] == vector)[0][0] + 1)
    return sorted_list


def get_orded_list(N): 
    pos = 0
    list_pos = [0] * N
    all_pos_list = list(range(N))
    got_pos = []
    median_dict = {}
    vector = np.random.permutation(np.arange(1, N+1))
    Q = 0

    for j in range(int(np.ceil(N/2))+1):

        pos_list = all_pos_list.copy()
        if len(all_pos_list) <= 2:
            list_pos[int(np.floor((N-1)/2))] = pos_list
            break
        while len(pos_list) > 2:
            all_medians = []
            if len(pos_list) > 3:
                for i in range(len(pos_list)):
                    if i >= (len(pos_list)-2):
                        ind = i - (len(pos_list) - 2) + 1
                        index = pos_list[:ind] + pos_list[i:]
                    else:
                        index = pos_list[i:i+3]
                
                    median_index, Q = get_median_index(median_dict, index, vector, Q)
                    # Lo que te da el bot
                    median_index = np.where(np.array(pos_list) == median_index)[0][0]
                    all_medians.append(median_index)

            else:
            # input pos_list
                median_index, Q = get_median_index(median_dict, pos_list, vector, Q)
                median_index = np.where(np.array(pos_list) == median_index)[0][0]
                all_medians.append(median_index)

            for index in sorted(list(set(all_medians)), reverse=True):
                pos_list.pop(index)
        
        if len(pos_list) != 2:
            print("Error")
        
        if pos == 0:
            list_pos[pos] = pos_list[0]
            list_pos[N-pos-1] = pos_list[1]
        else:
            list_pos[pos] = pos_list
        
        for p in pos_list:
            index = np.where(np.array(all_pos_list) == p)[0][0]
            all_pos_list.pop(index)
        pos += 1

    supp_n = list_pos[0]
    for j in range(1, int(np.floor((N-1)/2))+1):
        supp_pos_ = np.array(list_pos[j])
        if len(supp_pos_) == 2:
            index_v = [supp_n] + list(supp_pos_) # input
            median_index, Q = get_median_index(median_dict, index_v, vector, Q)
            list_pos[j] = median_index
            list_pos[N-j-1] = supp_pos_[supp_pos_ != median_index][0]
            supp_n = median_index
        else:
            list_pos[j] = supp_pos_
            break

    real_pos = get_sorted_list(vector)
    list_pos2 = [int(i)+1 for i in list_pos]
    if (list_pos2 != real_pos and list_pos2 != list(reversed(real_pos))):# or Q > 300:
        print("Está mal", vector, real_pos, list_pos)
    print(output(list_pos))
    return list_pos, Q


def output(vector):
    vector = [int(i)+1 for i in vector]
    str_vector = list(map(str, vector))
    return ' '.join(str_vector)


def results():
    t = int(input())
    N = int(input())
    Q = int(input())
    
    all_q = 0
    for i in range(1, t+1):
        list_pos, q = get_orded_list(N)
        all_q += q
    print(all_q)

results()