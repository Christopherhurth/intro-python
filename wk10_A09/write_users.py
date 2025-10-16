from pathlib import Path

contents = "esolstice\n"
contents += "mcoggeshall\n"
contents += "rjohansson\n"
contents += "Chatchett"

path = Path('output.txt')
path.write_text(contents)