from pathlib import Path
import re

p = Path(Path.home() / "amFOSS/automate-the-boring-stuff/chapter-09")

search = input("Enter regex to search for: ")
search_regex = re.compile(search)

for file in list(p.glob('*.txt')):
    results = search_regex.search(file.read_text())
    try:
        print(f"{results.group(0)} in {file}")
    except AttributeError:
        print(f"No results in {file}")