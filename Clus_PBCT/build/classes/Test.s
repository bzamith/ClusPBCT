[General]
Compatibility = MLJ08

[Data]
File = cellcycle_FUN.train.arff
TestSet = cellcycle_FUN.test.arff

[Hierarchical]
Type = TREE
HSeparator = /
WType = ExpAvgParentWeight

[Attributes]
%Target = 64-562
Weights = 1

[Tree]
FTest = 0.500
PBCT = Yes

[Model]
MinimalWeight = 5.0

[Output]
OutputMultiLabelErrors = True
