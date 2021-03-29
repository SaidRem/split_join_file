import os
import sys

SIZE_PART = 2**20 * 10   # 10 Mb 

def split_file(the_file, to_dir, size_part=SIZE_PART):
    """
    The function takes as arguments:
    the_file - path to file for split to parts
    to_dir - target directory for store splitted file
    optional arguments:
    size_part - size of part of the file 
    """
    if os.path.exists(the_file):                       # check for path exists to the file
        file_size = os.path.getsize(the_file)          # 
        if file_size/SIZE_PART > 9999:
            return f'The file too large to be split into {SIZE_PART} byte chunks.'
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
