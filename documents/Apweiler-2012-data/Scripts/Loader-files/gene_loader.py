# connect to database server and run the following command 
# python3 gene_loader.py | psql postgresql://localhost/postgres
import csv

DATA_SOURCE = 'extra_genes.csv'
print('COPY fall2021.gene(gene_id, display_gene_id, species, taxon_id) FROM STDIN;')
with open(DATA_SOURCE, 'r+') as f:
    reader = csv.reader(f)
    for row in reader:
        gene_id = row[0]
        display_gene_id = row[1]
        species = 'Saccharomyces cerevisiae'
        taxon_id = '559292'

        print(f'{gene_id}\t{display_gene_id}\t{species}\t{taxon_id}')
print('\\.')
