import shutil
import os
import sys
import numpy
from create_txt_for_data import create_txt_for_data


def write_data_file(path, train_path):
    # writes the obj.data file for the training set

    f = open(f'{path}/obj.data', mode="w")
    f.write('classes = 1\n')
    f.write(f'train = {train_path}\n')
    f.write('names = data/obj.names\n')
    f.write('backup = backup/\n')

def split(path_to_original, train_fraction, shuffle = False):
    # splits the original data set by the train_fraction. Shuffles if shuffle = True

    f = open(path_to_original, mode="r")
    lines = f.readlines()
    if shuffle:
        numpy.random.shuffle(lines)

    path_components = path_to_original.split(os.path.sep)
    original_directory =  os.path.sep.join(path_components[:-1]) + os.path.sep
    base_directory = os.path.sep.join(path_components[:-2]) + os.path.sep

    train, test = lines[:int(len(lines) * train_fraction)], lines[int(len(lines) * train_fraction) :]
    f.close()

    # establishing directories 
    directory = f'{train_fraction * 100}_shuffled_split' if shuffle else f'{train_fraction * 100}_temporal_split'

    train_path = os.path.join(directory, "train", "data")
    os.makedirs(train_path, exist_ok=True)
    test_path = os.path.join(directory, "test", "data")
    os.makedirs(test_path, exist_ok=True)

    #f = open(f'{directory}/train/train.txt', mode="w")
    for i in range(len(train)):
        #f.write(f'{train_path}/frame{i}.jpg\n')
        shutil.copyfile(os.path.join(os.getcwd(), base_directory,  train[i].strip()), f'{train_path}/frame{i}.jpg')
        shutil.copyfile(f'{os.path.join(os.getcwd(), base_directory, os.path.splitext(train[i].strip())[0])}.txt', f'{train_path}/frame{i}.txt')
    #f.close()

    #f = open(f'{directory}/test/test.txt', mode="w")
    for i in range(len(test)):
        #f.write(f'{test_path}/frame{i}.jpg\n')
        shutil.copyfile(os.path.join(os.getcwd(), base_directory, test[i].strip()), f'{test_path}/frame{i}.jpg')
        shutil.copyfile(f'{os.path.join(os.getcwd(), base_directory, os.path.splitext(test[i].strip())[0])}.txt', f'{test_path}/frame{i}.txt')

    write_data_file(directory, f'{directory}/train/train.txt')
    shutil.copyfile(f'{original_directory}/obj.names', f'{directory}/obj.names')
    create_txt_for_data(f'{directory}/train', 'train')
    create_txt_for_data(f'{directory}/test', 'test')

#split(0.7)
#split(0.8, shuffle=True)

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        print('Error not enough args. \n Usage: python split_dataset.py [path to original .txt] [train_fraction] [shuffle (Y / N)]')
    
    split(args[1], float(args[2]), True if args[3] == 'Y' else False)
    