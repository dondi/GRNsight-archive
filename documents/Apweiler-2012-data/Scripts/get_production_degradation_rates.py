from pyclbr import Function
import psycopg2
import csv
import os

GENES = ['ACE2', 'CBF1', 'CUP9', 'FKH1', 'GCN4', 'GCR1', 'MCM1', 'MET28', 'MET32', 'PDR1', 'PHO4', 'PUT3', 'RPN4', 'TYE7', 'YAP1']
DEGRADATION_DESTINATION = '/Users/ahmad00.m/Desktop/script-results/degradation.csv'
PRODUCTION_DESTINATION = '/Users/ahmad00.m/Desktop/script-results/production.csv'

# Create folder paths 
if not os.path.exists('/Users/ahmad00.m/Desktop/script-results'):
    os.makedirs('/Users/ahmad00.m/Desktop/script-results')

def build_genes_query(genes):
    result = "("
    x = -1
    for gene in genes:
        x+=1
        result += f"{'' if x == 0 else ' OR '}(fall2021.gene.gene_id = '{gene}' OR fall2021.gene.display_gene_id = '{gene}')"
    return f"{result})"

def build_rates(rates):
    res_rates = {}
    for gene in rates:
        rate = gene[0]
        systematic = gene[1]
        standard = gene[2]
        res_rates[standard]= {"systematic": systematic, "rate": rate}
    return res_rates

def build_query(type):
    # type is either "production_rate" or "degradation_rate"
    result = f"SELECT {type}, gene.gene_id, display_gene_id FROM fall2021.{type}, fall2021.gene"
    result += f" WHERE gene.gene_id = {type}.gene_id AND {build_genes_query(GENES)}"
    return result + " ORDER BY gene.display_gene_id"

try:
    connection = psycopg2.connect(user="",
                                  password="",
                                  host="grnsight2.cfimp3lu6uob.us-west-1.rds.amazonaws.com",
                                  port="5432",
                                  database="postgres")
    cursor = connection.cursor()

    # Get the degradation rates
    postgreSQL_select_Query = build_query("degradation_rate")
    cursor.execute(postgreSQL_select_Query)
    degradation_rates = cursor.fetchall()
    degradation_rates = build_rates(degradation_rates)

    # Get the production rates
    postgreSQL_select_Query = build_query("production_rate")
    cursor.execute(postgreSQL_select_Query)
    production_rates = cursor.fetchall()
    production_rates = build_rates(production_rates)
            
    print(f'Creating degradation.csv\n')
    d_file = open(DEGRADATION_DESTINATION, 'w')
    headers = f'Systematic Name\tStandard Name\tDegradation Rate'
    d_file.write(f'{headers}\n')
    for gene in degradation_rates:
        d_file.write(f'{degradation_rates[gene]["systematic"]}\t{gene}\t{degradation_rates[gene]["rate"]}\n')
    d_file.close()

    print(f'Creating production.csv\n')
    p_file = open(PRODUCTION_DESTINATION, 'w')
    headers = f'Systematic Name\tStandard Name\tProduction Rate'
    p_file.write(f'{headers}\n')
    for gene in production_rates:
        p_file.write(f'{production_rates[gene]["systematic"]}\t{gene}\t{production_rates[gene]["rate"]}\n')
    p_file.close()

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")