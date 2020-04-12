# ClusPBCT

- Clus: Clus PBCT (without jar)
- DatasetsGenerator.py: Generates datasets (path, depth, subtree and regular), creates Settings Files, tune and executes Clus_v5.jar
```
python3 DatasetsGenerator.py -i pheno_yeast_FUN

execute in dir with Clus_v5.jar and folder Datasets/
folder Datasets ex:
Datasets/pheno_yeast_FUN/pheno_yeast_FUN_train.arff
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