import re
stem_lines = []
with open("address to the file that you want to select the systematic names") as f:
    data = f.readlines()
    for i in data:
        stem_lines.append(i.split())
        
r = re.compile("Y[A-P][LR][0-9][0-9][0-9][WwCc](-[A-Z])?")
current_line_index = 0
newList = []
for comparison_line in stem_lines:
    for match in r.finditer(comparison_line[0]):
        gene = match.group()
        if gene in comparison_line:
            newList.append(comparison_line)

with open("address to the file you want data to be written to", "w") as textfile:

    for lists in newList:
        fields = '\t'.join(lists)
        textfile.write(fields)
        textfile.write('\n')
