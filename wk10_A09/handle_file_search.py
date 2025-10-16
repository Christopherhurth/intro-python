from pathlib import Path

users = Path('user.txt')
contents = users.read_text()

lines = contents.splitlines()
for line in lines:
    if "admin" in line:
        print(line)