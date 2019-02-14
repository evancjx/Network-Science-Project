# File Object

# not normally recommended

# f = open('test.txt')  # open for reading
# f = open('test.txt', 'w')  # open for writing
# f = open('test.txt', 'r')  # open for reading
# f = open('test.txt', 'r+')  # open for reading and writing
#
# f = open('test.txt', 'r')  # open for reading
#
# print(f.name)
# print(f.mode)
#
# f.close()

# context manager
with open('test.txt', 'r') as f:
    # print(f.name)
    # f_contents = f.read()
    # f_contents = f.readlines()
    # f_contents = f.readline()
    # print(f_contents)

    # for line in f:
    #     print(line, end='')

    # size_to_read = 10
    # print(f.tell())
    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)

    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')
    # f.seek(0)
    # f_contents = f.read(size_to_read)
    # print(f_contents)
    pass

# with open('test2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# copy images

# with open('test.jpg', 'rb') as rf:
#     with open('test_copy.jpg', 'wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)

print(f.closed)
