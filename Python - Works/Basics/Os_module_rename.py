import os
import shutil

cwd = os.getcwd()                                   # To know the Current Working Directory
print("The Current Working Directory is ", cwd ) 

# if not os.path.exists('Data'):                      # Doesn't show error after executing next time
#     os.mkdir('Data')
   
files = os.listdir("Data")
i = 1
    
for file in files:
    if file.endswith(".jpg"):
        os.rename(f'Data/{file}', f'Data/{i}.pdf')   # It renames the Folders/Files
        i = i + 1
# os.remove()                                       # It removes a single file
# os.rmdir()                                        # It removes an empty directory.    
# shutil.rmtree('Data')                             # It deletes a directory and all its contents.