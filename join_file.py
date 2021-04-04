import os
import sys


READ_CHUNK = 2*20 * 10

def join_parts(dir_name, file_name):
    if not os.path.exists(dir_name):
        print('Enter correct path to the directory')
    file_parts = os.listdir(dir_name)
    file_parts.sort()
    with open(file_name, 'wb') as the_f:
        for name in file_parts:
            path_parts = os.path.join(dir_name, name)
            with open(path_parts, 'rb') as part_n:
                while True:
                    part_bytes = part_n.read(READ_CHUNK)
                    if not part_bytes:
                        break
                    the_f.write(part_bytes)


if __name__ == '__main__':
    dir_name = input('Enter the path to the file parts for join\n')
    name = input('Enter the name of new file\n')
    join_parts(dir_name, name)