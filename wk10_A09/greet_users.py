from pathlib import Path

users = Path('user.txt')
contents = users.read_text()

lines = contents.splitlines()
for line in lines:
  line = line.rstrip().lstrip()
  print(f"Hello {line}!")

  


