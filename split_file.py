import os
import sys

SIZE_PART = 2**20 * 10   # 10 Mb 

def split_file(the_file, to_dir, size_part=SIZE_PART):
    """
    The function divides the_file into parts and places it
    in to_dir.
    Takes as arguments:
    1 - the path to the file;
    2 - folder path for parts of the file;
    3 - file part size (default: SIZE_PART (10 mb));
    """
    if os.path.isfile(the_file):                       # check for path exists to the file
        file_size = os.path.getsize(the_file)
        num_parts = int(file_size/SIZE_PART) + 1
        if num_parts > 999:
            return f'The file is too large to split into {SIZE_PART} byte parts.'
        else:
            ans = input(f'The file {os.path.basename(the_file)} ' 
                        f'will be divided into {num_parts}. Continue? (y/n) ')
            if ans.strip() == 'n':
                return None
    else:
        print('Enter correct path to a file')
    with open(the_file, 'rb') as the_f:
        i = 0
        while True:
            part_name = 'part_{:03}'.format(i)
            i += 1
            with open(os.path.join(to_dir, part_name), 'wb') as par_f:
                p = the_f.read(SIZE_PART)
                if not p:
                    break
                par_f.write(p)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        the_file = input('Enter path to file for split:\n')
        to_dir = input('Enter target directory for storing parts of the splitting file:\n')
        split_file(the_file, to_dir)
    else:
        the_file, to_dir = sys.argv[1:3]
        
