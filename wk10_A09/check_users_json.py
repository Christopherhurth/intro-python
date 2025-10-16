from pathlib import Path
import json

path = Path('users.json')
contents =  path.read_text()
users = json.loads(contents)

for user in users:
    if "rjohansson" in user:
        print(f"{user} is a user on this terminal.")