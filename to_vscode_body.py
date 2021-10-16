import re

boundary_space_re = re.compile(r'^\s+')

lout = []

for line in open("snippet.txt"):
    line = line.strip("\n")
    search = boundary_space_re.search(line)
    rep = ''

    if search:
        for r in range(len(search.group()) - 1):
            rep += r'  '
    line = line.strip().replace('\\', '\\\\').replace('"', '\\"')
    lout.append('"' + rep + line + '"')

body = '[\n' + ',\n'.join(lout) + '\n]'

prefix = """
"name": {
    "prefix":  "" ,
    "body": %s,
    "description": ""
}
""".strip()
open("out.txt", "w").write(prefix % body)
