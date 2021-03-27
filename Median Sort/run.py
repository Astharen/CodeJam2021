import numpy as np

def get_median_index(median_dict, index):

  index = tuple(index)
  if index not in median_dict.keys() and tuple(reversed(list(index))) not in median_dict.keys():
    print(output(index))
    median_index = int(input())
    median_index -= 1
    median_dict[index] = median_index
  else:
    if index in median_dict.keys():
      median_index = median_dict[index]
    elif tuple(reversed(list(index))) not in median_dict.keys():
      median_index = median_dict[list(reversed(index))]
  return median_index


def get_orded_list(N): 
  pos = 0
  list_pos = [0] * N
  all_pos_list = list(range(N))
  got_pos = []
  median_dict = {}

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
          
          median_index = get_median_index(median_dict, index)
          # Lo que te da el bot
          median_index = np.where(np.array(pos_list) == median_index)[0][0]
          all_medians.append(median_index)

      else:
        # input pos_list
        median_index = get_median_index(median_dict, pos_list)
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
      median_index = get_median_index(median_dict, index_v)
      list_pos[j] = median_index
      list_pos[N-j-1] = supp_pos_[supp_pos_ != median_index][0]
      supp_n = median_index
    else:
      list_pos[j] = supp_pos_
      break

  return list_pos


def output(vector):
  vector = [int(i)+1 for i in vector]
  str_vector = list(map(str, vector))
  return ' '.join(str_vector)


def results():
  t, N, Q = [int(s) for s in input().split(" ")]
  
  for i in range(1, t+1):
    list_pos = get_orded_list(N)
    print(output(list_pos))
    _ = int(input())

results()