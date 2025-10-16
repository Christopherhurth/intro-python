from pathlib import Path
import json

users = ["esolstice", "mcoggeshall", "rjohansson", "Chatchett"]

path = Path('users.json')
contents = json.dumps(users)
path.write_text(contents)