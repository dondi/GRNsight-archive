### 1 --> First the following command was run to avoid primary and foreign key constraints 
      
    INSERT INTO ref (pubmed_id, authors, publication_year, title, doi, ncbi_geo_id) VALUES ('22697265', 'Apweiler E., Sameith K., Margaritis T., Brabers N., Pasch L., Bakker L., Leenen D., Holstege F., Kemmeren P.', '2012', 'Yeast glucose pathways converge on the transcriptional regulation of trehalose biosynthesis', '10.1186/1471-2164-13-239', 'GSE33099');
### 2 --> Run the `expression_metadata.py` script to avoid primary and foreign key constraints using the following command 
    
    python3 expression_metadata_loader.py | psql postgresql://localhost/postgres
### 3 --> There are some genes not present in the gene table in our database so we add them using `extra_gene_addition.py` script using the following command 

    python3 extra_gene_addition.py
### 4 --> Then load the file containing the genes not present on our database using the following command

    python3 gene_loader.py | psql postgresql://localhost/postgres
### 5 --> Run `preloading.py` script to attain the correctly formatted file for input to the expression table and preparation for next step
    python3 preloading.py
### 6 --> After all data is loaded to expression_metadata, gene, and ref table, run the following command to load the Apweiler data

    python3 Apweiler_loader.py | psql postgresql://localhost/postgres
