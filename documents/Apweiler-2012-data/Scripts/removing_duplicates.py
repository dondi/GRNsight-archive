stem_lines = []
new_list = []
with open("/Users/ahmad00.m/Desktop/exp_data_cleaning/systematic_IDs.txt") as f:
    data = f.readlines()
    for i in data:
        stem_lines.append(i.split())

current_line_index = 0
for comparison_line in stem_lines:
    for current_line in stem_lines[current_line_index + 1:]:
        comparison_expressions = comparison_line[1:]
        current_expressions = current_line[1:]
        if comparison_expressions == current_expressions:
            stem_lines.remove(current_line)
    current_line_index += 1

with open("/Users/ahmad00.m/Desktop/exp_data_cleaning/unique_sys_IDs.txt", "w") as textfile:

    for lists in stem_lines:
        fields = '\t'.join(lists)
        textfile.write(fields)
        textfile.write('\n')
