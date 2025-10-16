from pathlib import Path
import json

path = Path('users.json')
users =  path.read_text()
contents = json.loads(users)

count = 0

for line in contents:
    count += 1
    

print(count)