import os

from pathlib import Path
for folder, subfolder, filenames in os.walk(os.getcwd()):
    for filename in filenames:  
        if os.path.getsize(os.path.join(folder, filename)) > 104857600:
            print(f"{filename} in {folder} is greater than 100 MB")
