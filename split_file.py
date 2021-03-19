import os
import sys

SIZE_PART = 1048576

def split_file(the_file, to_dir, size_part=SIZE_PART):
    with open(the_file, 'rb') as the_f:
        i = 0
        while True:
            part_name = 'part_{:04}'.format(i)
            i += 1
            with open(os.path.join(to_dir, part_name), 'wb') as par_f:
                p = the_f.read(SIZE_PART)
                par_f.write(p)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        the_file = input('Enter path to file for split')
        to_dir = input('Enter target direcotry for storing parts of the splitting file')
        split_file(the_file, to_dir)
