# connect to database server and run the following command 
# python3 Apweiler_loader.py | psql postgresql://localhost/postgres

import csv

DATA_SOURCE = 'processed_expression_copy.txt'
print('COPY fall2021.expression(gene_id, taxon_id, sort_index, sample_id, expression, time_point, dataset) FROM STDIN;')
with open(DATA_SOURCE, 'r+') as f:
    reader = csv.reader(f)
    for row in reader:
        gene_id = row[0]
        taxon_id = row[1]
        sort_index = row[2]
        sample_id = row[3]
        expression = row[4]
        time_point = row[5]
        dataset = row[6]

        print(f'{gene_id}\t{taxon_id}\t{sort_index}\t{sample_id}\t{expression}\t{time_point}\t{dataset}')
print('\\.')
