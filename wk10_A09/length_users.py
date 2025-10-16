from pathlib import Path

users = Path('user.txt')
contents = users.read_text()

lines = contents.splitlines()
for line in lines:
    print(f'{line}: {len(line)}')
    