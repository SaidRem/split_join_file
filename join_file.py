import os
import sys


READ_CHUNK = 262144

def join(dir_name, file_name):
    if not os.path.exists(dir_name):
        print('Enter correct path to the directory')
    file_parts = os.listdir(dir_name)
    file_parts.sort()
    with open(file_name, 'wb') as col_file:
        for name in file_parts:
            path_to = os.path.join(dir_name, name)
            with open('path_to', 'rb') as p_file:
                while True:
                    break