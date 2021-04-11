import os
import sys
import re


READ_CHUNK = 2*20 * 10    # 2*20 = 1 Mb
ONE_HUND = 2*20 * 100  # 100 Mb

def test_parts(file_parts):
    """
    Checking the folder contains 
    only parts of the file.
    """
    pat = re.compile(r'^part_\d{3}$')
    for p in file_parts:
        if not pat.match(p):
            return p

def join_parts(dir_name, file_name, tar_dir=''):
    if not os.path.exists(dir_name):
        print('Enter correct path to the directory')
    file_parts = os.listdir(dir_name)
    file_parts.sort()
    testing = test_parts(file_parts)
    if testing:
        return f'Incorrect file: {testing}'
    with open(os.path.join(tar_dir, file_name), 'wb') as the_f:
        for name in file_parts:
            path_part = os.path.join(dir_name, name)
            with open(path_part, 'rb') as part_n:
                if os.path.getsize(path_part) > ONE_HUND:
                    while True:
                        part_bytes = part_n.read(ONE_HUND)
                        if not part_bytes:
                            break
                        the_f.write(part_bytes)
                else:
                    while True:
                        part_bytes = part_n.read(READ_CHUNK)
                        if not part_bytes:
                            break
                        the_f.write(part_bytes)
    return "File compiled successfully"


if __name__ == '__main__':
    dir_name = input('Enter the path to the file parts for join\n')
    name = input('Enter the name of new file\n')
    tar_dir = input('Enter target directory\n')
    print(join_parts(dir_name, name, tar_dir))