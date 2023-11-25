import os
import sys

def create_txt_for_data(path, name):
    dir_list = os.listdir(os.path.join(path, 'data'))

    f = open(os.path.join(path, f'{name}.txt'), mode="w")
    for file in dir_list:
        if os.path.splitext(file)[1] == '.jpg':
            f.write(f'{path}/data/{file}\n')
    f.close()


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 1:
        print('Error not enough args. \n Usage: python create_txt_for_data.py [ path to main directory ]')
        print('format of the directory should be:\n- /[main]\n\t- /data')
        print('The .txt file containing the paths to all .jpgs will be created in the "main" directory')

    create_txt_for_data(args[1])