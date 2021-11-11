stem_lines = []
with open("/Users/ahmad00.m/Desktop/bioinformatics research 2021/cleaning file/wt_stem.txt") as f:
    data = f.readlines()
    for i in data:
        stem_lines.append(i.split())
        
newList = []
for comparison_line in stem_lines:
    systemname = comparison_line[0]
    if systemname[0] == "Y":
        newList.append(comparison_line)

with open("/Users/ahmad00.m/Desktop/bioinformatics research 2021/cleaning file/systematic_names.txt", "w") as textfile:

    for lists in newList:
        fields = '\t'.join(lists)
        textfile.write(fields)
        textfile.write('\n')
