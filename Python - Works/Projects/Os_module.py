import os
import shutil

# os.mkdir('Data')                                          # To Create the Folder

files = os.listdir('Data')

cwd = os.getcwd()                                           # To know the Current Working Directory
print('The Current Working Directory is ', cwd)

i = 1

for file in files:
    #print(os.mkdir(f'Data\Day {i+1}'))                     # To itterate the Sub-Folders
    #os.rename(f'Data\Day {i+1}', f'Data\Tutorial {i+1}')   # To Rename the Sub-Folders
    if file = endswith('.jpg'):                             # To locate the name of the file
        os.rename(f'Data\{file}', f'Data\{i}.jpg')          # To Rename the name of the file
        i += 1
    

# os.remove('Data\Tutorial 5')                              # It removes a single file
# os.rmdir(f'Data\Tutorial {5+1}')                          # It removes an empty directory.    
# shutil.rmtree('Data')                                     # It deletes a directory and all its contents.