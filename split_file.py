import os
import sys

SIZE_PART = 2**20 * 10  # 10 Mb
ONE_HUND = 2**20 * 100  # 100 Mb

def split_file(the_file, to_dir, size_part=SIZE_PART, mod=False):
    """
    The function divides the_file into parts and places it
    in to_dir.
    Takes as arguments:
    1 - the path to the file;
    2 - folder path for parts of the file;
    3 - file part size (default: SIZE_PART (10 mb));
    """
    if mod == 'cd':
        size_part *= 70  # 700 Mb
    elif mod == 'dvd':
        size_part *= 450  # 4500 Mb
    if os.path.isfile(the_file):                       # checking if the path to the file exists
        file_size = os.path.getsize(the_file)
        num_parts = int(file_size/size_part) + 1
        if num_parts > 999:
            return f'The file is too large to split into {size_part} byte parts.'
        else:
            ans = input(f'The file {os.path.basename(the_file)} ' 
                        f'will be divided into {num_parts}. Continue? (y/n) ')
            if ans.lower() == 'n':
                print('Shutting down')
                return None
    else:
        print('Enter correct path to a file')
    
    if not os.path.exists(to_dir):
        ans = input(f'Create new folder: {os.path.basename(to_dir)} '
                    f'in directory {os.path.dirname(to_dir)} (y/n) ')
        if ans.lower() == 'y':
            os.mkdir(to_dir)
        else:
            print('Shutting down')
            return None
    with open(the_file, 'rb') as the_f:
        i = 0
        while True:
            part_name = 'part_{:03}'.format(i)
            i += 1
            max_size = 0
            if size_part > ONE_HUND:
                par_f = open(os.path.join(to_dir, part_name), 'wb')
                while max_size < size_part:
                    p = the_f.read(ONE_HUND)
                    max_size += ONE_HUND
                    if not p:
                        break
                    par_f.write(p)
            else:
                par_f = open(os.path.join(to_dir, part_name), 'wb')
                par_f.write(p)
            par_f.close()
            if not p:
                break
            
    return "File splitting completed successfully"


if __name__ == '__main__':
    if len(sys.argv) == 1:
        my_mode = input('For CD size (700 Mb part) or DVD size (4500 Mb part)?\n'
                        '(Enter cd/dvd) => ')
        the_file = input('Enter path to file for split:\n')
        to_dir = input('Enter target directory for storing parts of the splitting file:\n')
        if my_mode.strip().lower() == 'cd':
            split_file(the_file, to_dir, mod='cd')
        elif my_mode.strip().lower() == 'dvd':
            split_file(the_file, to_dir, mod='dvd')
        else:
            split_file(the_file, to_dir)
    else:
        the_file, to_dir = sys.argv[1:3]
        split_file(the_file, to_dir)
        
