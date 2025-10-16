from pathlib import Path

users = Path('user.txt')
contents = users.read_text()

lines = contents.splitlines()

count = 0

for line in lines:
  line = line.lstrip()
  count += 1
  print(f"Hello {line}!")
  
print(count)