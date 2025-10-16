from pathlib import Path

try:
    path = Path('non_existent.txt')
    contents = path.read_text()
    print(contents)

except FileNotFoundError:
    print("This file does not exist...")