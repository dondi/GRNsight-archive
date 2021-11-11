stem_lines = []
with open("address to the file you want to check .txt") as f:
    data = f.readlines()
    for i in data:
        stem_lines.append(i.split())

current_line_index = 0
for comparison_line in stem_lines:
    for current_line in stem_lines[current_line_index + 1:]:
        comparison_expressions = comparison_line[2:]
        current_expressions = current_line[2:]
        if comparison_expressions == current_expressions:
            stem_lines.remove(current_line)  # removes duplicates from the list 
    current_line_index += 1

with open("address to the file you want to write (with duplicates removed) .txt", "w") as textfile:

    for lists in stem_lines:
        fields = '\t'.join(lists)
        textfile.write(fields)
        textfile.write('\n')
