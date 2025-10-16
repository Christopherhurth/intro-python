from pathlib import Path

    
path = Path('user.txt')
try:   
    contents = path.read_text()
    print(contents)

except FileNotFoundError:
    print(f"The file {path} does not exist!")

try:
    path = Path('backup.txt')
    path.write_text(contents)
    
except Exception:
    print("something went wrong!")