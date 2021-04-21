import os
import sys

ONE_MB = 2**20  # 1 Mb
ONE_HUND = 2**20 * 100  # 100 Mb


def split_file(the_file, to_dir, size_part=ONE_MB, mod=False):
    """
    The function divides the_file into parts and places it
    in to_dir.
    Takes as arguments:
    1 - the path to the file;
    2 - folder path for parts of the file;
    3 - file part size (default: ONE_MB (1048576 bytes = 1 mb));
    4 - mod - cd = 700 Mb part; dvd = 4500Mb part;
    """
    if mod == 'cd':
        size_part *= 700  # 700 Mb
    elif mod == 'dvd':
        size_part *= 4500  # 4500 Mb
                    
    file_size = os.path.getsize(the_file)
    num_parts = int(file_size/size_part) + 1
    if num_parts > 99:
        return f'The file is too large to split into {size_part} byte parts.'
    else:
        ans = input(f'The file {os.path.basename(the_file)} ' 
                    f'will be divided into {num_parts}. Continue? (y/n) ')
        if ans.rstrip().lower() == 'n':
            print('Shutting down')
            return None
    
    if not os.path.exists(to_dir):
        ans = input(f'Create new folder: {os.path.basename(to_dir)} '
                    f'in directory {os.path.dirname(to_dir)} (y/n) ')
        if ans.lower() == 'y':
            os.mkdir(to_dir)
        else:
            print('Shutting down')
            return None
    with open(the_file, 'rb') as the_f:
        i = 1
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

def test_path(path_to_file, path_to_dir):
    test_file = ''
    test_dir = ''
    if os.path.exists(path_to_file):
        if os.path.isfile(path_to_file):
            test_file = True
        else:
            test_file = 'Enter path to the file.'
    else:
        test_file = 'File does not exists. Enter correct path to a file.'

    if os.path.exists(path_to_dir):
        if os.path.isdir(path_to_dir):
            test_dir = True
        else:
            test_dir = 'Enter path to a directory for storing parts of file.'
    else:
        test_dir = 'Directory does not exists. Enter correct path to a directory.'
    
    return test_file, test_dir

            

def main():
    if len(sys.argv) == 1:
        my_mode = input('Splitting for CD size (700 Mb part) or DVD size (4500 Mb part)?\n'
                        '(Enter cd/dvd) => ')
        while True:
            the_file = input('Enter path to file for split:\n')
            to_dir = input('Enter target directory for storing parts of the splitting file:\n')
            test_file, test_dir = test_path(the_file, to_dir)
            if test_file is True and test_dir is True:
                break
            else:
                print(f'Test file: {test_file}\nTest directory: {test_dir}')
        if my_mode.strip().lower() == 'cd':
            split_file(the_file, to_dir, mod='cd')
        elif my_mode.strip().lower() == 'dvd':
            split_file(the_file, to_dir, mod='dvd')
        else:
            split_file(the_file, to_dir)
    else:
        if len(sys.argv) == 3:
            the_file, to_dir = sys.argv[1:]
            split_file(the_file, to_dir)
        elif len(sys.argv) == 4:
            the_file, to_dir, mod = sys.argv[1:]
            split_file(the_file=the_file, to_dir=to_dir, mod=mod)


if __name__ == '__main__':
    main()
    
        
