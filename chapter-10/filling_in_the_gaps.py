import os, shutil

nums = []
from pathlib import Path
for folder, subfolder, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        filename_without_ext = os.path.splitext(filename)[0]
        test = filename_without_ext.removeprefix('spam')
        try:
            nums.append(int(test))
        except ValueError:
            continue

nums.sort()
bad_files = []
for i in range(len(nums)):
    if nums[i] != i+1:
        bad_files.append(i+1)
        nums.sort()
i = 1
for folder, subfolder, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        filename_without_ext = os.path.splitext(filename)[0]
        test = filename_without_ext.removeprefix('spam')
        try:
            nums.append(int(test))
            file_name = 'spam' + str(i).rjust(3,'0') + '.txt'
            shutil.move(os.path.abspath(filename),  os.path.abspath(folder) + file_name)
        except ValueError:
            continue