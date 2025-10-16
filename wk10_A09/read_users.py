from pathlib import Path

users = Path('user.txt')
contents = users.read_text()

print(contents)