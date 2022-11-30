import csv 

DATA_SOURCE = 'Apweiler_2012_wt.txt'
REFERENCE_SOURCE = 'gene_table.csv'
FINAL_FILE = 'extra_genes.csv'
SGD_REF = 'results.csv'

with open(DATA_SOURCE, 'r+') as f:
    reader1 = csv.reader(f, delimiter='\t')
    next(reader1, None)
    with open(REFERENCE_SOURCE, 'r') as ref:
        reader2 = csv.reader(ref, delimiter=',')
        next(reader2, None)
        some_dic = {}
        for row in reader2:
            some_dic[row[0]] = row[1]
        with open(SGD_REF, 'r') as ref1:
            reader3 = csv.reader(ref1, delimiter=',')
            sgd_dic = {}
            for row in reader3:
                sgd_dic[row[0]] = row[1]
            with open(FINAL_FILE, 'w') as write:
                empty_list = []
                extra_gene = []
                test_list = []
                in_list = []
                for row in reader1:
                    if row[0] not in some_dic:
                        extra_gene.append(row[0])
                print(len(extra_gene))
                for gene in extra_gene:
                    if gene not in sgd_dic:
                        test_list = [gene] * 2 
                        fields = ','.join(test_list)
                        write.write(fields)
                        write.write('\n')
                    else: 
                        test_list = []
                        test_list.append(gene)
                        if sgd_dic[gene] != '':
                            test_list.append(sgd_dic[gene])
                        else:
                            test_list.append(gene)
                        fields = ','.join(test_list)
                        write.write(fields)
                        write.write('\n')