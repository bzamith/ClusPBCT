# ClusPBCT

- Clus: Clus PBCT (without jar)
- DatasetsGenerator.py: Generate datasets (path, depth, subtree and regular)
```
python3 DatasetsGenerator.py -i pheno_yeast_FUN
```
- Datasets: Data used


- Old: 
  - Hierarchy: R scripts to create datasets
  - DatasetsNCBIWeb: Cerri's last suggestion, getting via Web query NCBI features
  - DatasetsNCBIWeb+NCBI: NCBI features combined with Path (Hierarchy) features
  - RunAll.py: Given a name as parameter, tune the datasets and run the final prediction for each measure, outputing the test measures values
  ```
    python RunAll.py -i "Church"
  ```
