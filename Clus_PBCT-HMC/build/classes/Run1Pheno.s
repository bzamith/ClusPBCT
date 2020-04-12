[General]
%Compatibility = MLJ08

[Data]
File = intD1_pheno_FUN.trainvalid.arff
SecondFile = intD2_regular_pheno_FUN.trainvalid.arff
%PruneSet = intD1_pheno_FUN.valid.arff
TestSet = intD1_pheno_FUN.test.arff

[Hierarchical]
Type = TREE
HSeparator = /
WType = ExpAvgParentWeight

[Attributes]
Target = 70-524
Weights = 1

[Tree]
%FTest = [0.001,0.005,0.01,0.05,0.1,0.125]
FTest = 0.125

[Model]
%MinimalNumberExamples = 5
MinimalWeight = 5.0

[Output]
WritePredictions = Test
OutputMultiLabelErrors = Yes
