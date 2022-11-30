# connect to database server and run the following command 
# python3 expression_metadata_loader.py | psql postgresql://localhost/postgres
print('BEGIN;')

time_values = [0, 3, 7.5, 15, 30, 60, 110, 150, 300]

for value in time_values:
    ncbi = 'GSE33099'
    pubmed = '22697265'
    control_strain = 'BY4742'
    treatment_strain = 'BY4742'
    control = 'glucose'
    treatment = 'glucose depletion'
    conc_val = 2
    conc_unit = 'percent'
    time_val = value 
    time_u = 'm'
    replicate_num = 2
    expres_table = 'Apweiler_2012_wt_log2_expression'

    print(f'INSERT INTO fall2021.expression_metadata VALUES(\'{ncbi}\', \'{pubmed}\', \'{control_strain}\', \'{treatment_strain}\', \'{control}\', \'{treatment}\', {conc_val}, \'{conc_unit}\', {time_val}, \'{time_u}\', {replicate_num}, \'{expres_table}\', \'\');')
    # changed the line above
print('COMMIT;')