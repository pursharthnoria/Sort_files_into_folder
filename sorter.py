import os
import shutil
import sys

path = sys.argv[1]
files = os.listdir(path)

def get_unique_files():
    unique_ext = []
    for file in files:
        ext = str(file).split('.')[-1]
        if ext not in unique_ext:
            unique_ext.append(ext)
    return unique_ext

extensions = get_unique_files()

def create_folders():
    for ext in extensions:
        if not os.path.exists(path+'\\'+ext+'_files'):
            os.mkdir(path+'\\'+ext+'_files')

def move_files():
    for file in files:
        ext = str(file).split('.')[-1]
        if ext!='py':
            shutil.move(path+'\\'+file,path+'\\'+ext+'_files'+'\\'+file)

create_folders()
move_files()