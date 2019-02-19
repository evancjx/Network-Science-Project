from itertools import groupby
import time

def count_degree(vertex, egdeto):
    # not a good way to get degree
    # each_node_degree = [len(list(group)) for key, group in groupby(vertex)]
    # print(len(each_node_degree))

    start_time = int(round(time.time() * 1000))

    each_node_degree = [];
    index = 1;
    for key, group in groupby(vertex):
        # print('key: ' + str(key))
        # print('index: ' + str(index))

        if int(key) != int(index):
            # print('not equal')
            each_node_degree.insert(index-1, 0)
            index += 2
        else:
            index += 1

        each_node_degree.append(len(list(group)))
        # if key == '10':
        #     break

    end_time = int(round(time.time() * 1000))
    compute_time = int(end_time) - int(start_time)
    print('({}ms) Count degree'.format(compute_time))

    # for index, degree in enumerate(each_node_degree):
    #     # print(key, degree)
    #     print(index, degree)
    #     if index == 100:
    #         break

    return each_node_degree
