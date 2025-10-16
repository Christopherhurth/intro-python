from pathlib import Path
import json

path = Path('users.json')
users =  path.read_text()
contents = json.loads(users)

print(contents)