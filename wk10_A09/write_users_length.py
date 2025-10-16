from pathlib import Path

contents = "esolstice\n"
contents += "mcoggeshall\n"
contents += "rjohansson\n"
contents += "chatchett\n"
contents += "admin"

lines = contents.splitlines()

output = ""
for line in lines:
    output += f'{line}: {len(line)}\n'.upper()
    # print(f'{line}: {len(line)}')
    

path = Path('output.txt')
path.write_text(output)