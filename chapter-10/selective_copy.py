import os, shutil

from pathlib import Path
selected_folder = Path(Path.home() / 'amFOSS/automate-the-boring-stuff/chapter-09')
os.mkdir(selected_folder / '../chapter-10/destination')
for folder, subfolder, filenames in os.walk(selected_folder):
    for filename in filenames:
        if filename.endswith('.txt'):
            shutil.copy(selected_folder / filename, Path.home() / 'amFOSS/automate-the-boring-stuff/chapter-10/destination')
