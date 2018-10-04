import pandas as pd
import re
import numpy as np
from urllib import urlopen
import argparse


grep = lambda s,c: [pos for pos, char in enumerate(s) if char == c] #retorna as posicoes do char (c) numa string (s)

def create_datasets(dataset):
	cat = ["trainvalid","train"]
	for i in range(0,len(cat)):
		linesPath = open("/home/zamith/Documents/Grad_e_IC/8o_Semestre/Outros/BEPE/DatasetsHierarchy/Path/"+dataset+"/intD2_path_"+dataset.lower()+"_FUN."+cat[i]+".arff","r").readlines()
		linesNCBI = open("/home/zamith/Documents/Grad_e_IC/8o_Semestre/Outros/BEPE/DatasetsNCBIWeb/"+dataset+"/intD2_"+dataset.lower()+"_FUN."+cat[i]+".arff","r").readlines()
		append_datasets(linesPath,linesNCBI,dataset,cat[i])

def append_datasets(linesPath,linesNCBI,dataset,cat):
	#find NCBI attributes until Protein0
	attributesNCBI = list()
	for i in range(0,len(linesNCBI)):
		line = linesNCBI[i]
		cap = re.search("@ATTRIBUTE",line.upper())
		if cap is not None:
			cap = re.search("PROTEIN0",line.upper())
			if cap is not None:
				break
			else:
				attributesNCBI.append(line)
	#find NCBI instances
	for i in range(0,len(linesNCBI)):
		line = linesNCBI[i]
		cap = re.search("@DATA",line.upper())
		if cap is not None:
			startNCBI = i+1
			endNCBI = len(linesNCBI)
			break
	#append NCBI attributes to beginning of Path
	linesComplete = list()
	for i in range(0,len(linesPath)):
		line = linesPath[i]
		cap = re.search("ATTRIBUTE",line.upper())
		if cap is not None:
			linesComplete = linesComplete + attributesNCBI
			break
		else:
			linesComplete.append(line)
	#append Paths attributes
	for i in range(i,len(linesPath)):
		line = linesPath[i]
		cap = re.search("@DATA",line.upper())
		if cap is None:
			linesComplete.append(line)
		else:
			linesComplete.append(line)
			break
	nbAttrNCBI = len(attributesNCBI)
	j=startNCBI
	for i in range(i+1,len(linesPath)):
		line = linesPath[i]
		lineNCBI = linesNCBI[j]
		commas = grep(lineNCBI,",")[0:nbAttrNCBI+1]
		linesComplete.append(lineNCBI[0:commas[nbAttrNCBI-1]]+","+line)
		j=j+1
	#Writes intD1
	writer = open("/home/zamith/Documents/Grad_e_IC/8o_Semestre/Outros/BEPE/DatasetsPath+NCBI/"+dataset+"/intD2_"+dataset.lower()+"_FUN."+cat+".arff","w")
	for i in range(0,len(linesComplete)):
		writer.write(linesComplete[i]+'\n')
	writer.close()

