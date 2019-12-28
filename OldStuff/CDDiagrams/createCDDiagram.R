library("scmamp")
library("ggplot2")
library("Rgraphviz")
measures = c("AUPRC","Weighted","Pooled")
for(i in 1:length(measures)){
	dados = read.csv(paste(measures[i],"csv",sep="."), header = TRUE, sep = ",")
	plotCD (dados, alpha=0.05, cex=1.25, decreasing = TRUE)
}
