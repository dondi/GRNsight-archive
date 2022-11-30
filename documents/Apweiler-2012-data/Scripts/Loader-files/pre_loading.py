import csv

new_list1 = []
new_list2 = []
expression_list1 = []
expression_list2 = []

taxon_id = '559292'
dataset = 'Apweiler_2012_wt'

DATA_SOURCE = 'test_expression.txt'
with open(DATA_SOURCE, 'r+') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader, None)

    for row in reader:
        new_list1.append([row[0], row[1], row[3], row[5], row[7], row[9], row[11],
                          row[13], row[15], row[17]])
        new_list2.append([row[0], row[2], row[4], row[6], row[8], row[10], row[12],
                          row[14], row[16], row[18]]) 
    with open("processed_expression.txt", "a") as file1:
        index = 1
        for row in new_list1:
            expression_list1.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t0m-1', row[1], '0', dataset])
            index += 2
            expression_list1.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t3m-1', row[2], '3', dataset])
            index += 2
            expression_list1.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t7.5m-1', row[3], '7.5', dataset])
            index += 2
            expression_list1.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t15m-1', row[4], '15', dataset])
            index += 2
            expression_list1.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t30m-1', row[5], '30', dataset])
            index += 2
            expression_list1.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t60m-1', row[6], '60', dataset])
            index += 2
            expression_list1.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t110m-1', row[7], '110', dataset])
            index += 2
            expression_list1.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t150m-1', row[8], '150', dataset])
            index += 2
            expression_list1.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t300m-1', row[9], '300', dataset])
            index += 2
        index = 2
        for row in new_list2:
            expression_list2.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t0m-2', row[1], '0', dataset])
            index += 2
            expression_list2.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t3m-2', row[2], '3', dataset])
            index += 2
            expression_list2.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t7.5m-2', row[3], '7.5', dataset])
            index += 2
            expression_list2.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t15m-2', row[4], '15', dataset])
            index += 2
            expression_list2.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t30m-2', row[5], '30', dataset])
            index += 2
            expression_list2.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t60m-2', row[6], '60', dataset])
            index += 2
            expression_list2.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t110m-2', row[7], '110', dataset])
            index += 2
            expression_list2.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t150m-2', row[8], '150', dataset])
            index += 2
            expression_list2.append([row[0], taxon_id, str(index), 'BY4741_glucose_2%_LogFC_t300m-2', row[9], '300', dataset])
            index += 2 

        for lists in expression_list1:
            fields = ','.join(lists)
            file1.write(fields)
            file1.write('\n')
        for lists in expression_list2:
            fields = ','.join(lists)
            file1.write(fields)
            file1.write('\n')
