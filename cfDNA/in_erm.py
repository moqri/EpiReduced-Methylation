import pandas as pd
erm_sites_file='../ErM/erm_sites.csv'
erm_genes_file='../ErM/erm_genes.csv'
cfDNA_sites_file='sites.txt'
cfDNA_genes_file='genes.txt'

erm_sites=pd.read_csv(erm_sites_file)['Probe_ID'].values
cfDNA_sites=pd.read_csv(cfDNA_sites_file,header=None)[0].values
i=0
for site in cfDNA_sites:
    i+=1
    if site in erm_sites:
        print(i, site, 'YES')
    else:
        print(i, site, 'NEED TO CHECK')    
erm_genes=set(pd.read_csv(erm_genes_file,index_col=0)['Gene'].values)
cfDNA_genes=pd.read_csv(cfDNA_genes_file,header=None)[0].values
for gene in cfDNA_genes:
    if gene in erm_genes:
        print(i, gene, 'YES')
    else:
        print(i, gene, 'NEED TO CHECK')
