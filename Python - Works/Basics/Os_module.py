import os
import shutil

cwd = os.getcwd()                                # To know the Current Working Directory
print("The Current Working Directory is ", cwd ) 

if not os.path.exists('Data'):                   # Doesn't show error after executing next time
    os.mkdir('Data')
    
# for i in range(100):                           
#     os.mkdir(f'Data\Images {i+1}')             # It creates Sub-Folders inside Current Folder

# os.remove()                                    # It removes a single file
# os.rmdir()                                     # It removes an empty directory.    
# shutil.rmtree('Data')                          # It deletes a directory and all its contents.