import pandas as pd
import re
import numpy as np
from urllib import urlopen
import argparse


grep = lambda s,c: [pos for pos, char in enumerate(s) if char == c] #retorna as posicoes do char (c) numa string (s)

def ancestorTotal(node):
    resp = []
    pos=grep(node,"/")
    while len(pos)>0:
        node=node[0:pos[len(pos)-1]]
        resp.append(node)
        pos=grep(node,"/")
    return resp


def get_query(hier_class):
	hier_class = hier_class.replace("/",".")
	fonts = ["cdd","ipg","protein","proteinclusters","sparcle","structure"]
	lines = open("/home/zamith/Documents/Grad_e_IC/8o_Semestre/BEPE/Mipsfunctional.txt","r").readlines()
	for line in lines:
		cap = re.search(hier_class,line)
		if cap is not None:
			cap = re.search("[+-]?\d+(?:\.\d+)?",line)
			start = cap.start()
			cap = re.search("[+-]?\d+(?:\.\d+)? ",line)
			end = cap.end()
			hier_class = line[start:(end-1)]
			pure_expression = line[end:len(line)]
			expression = pure_expression.replace(" ","+")
			values = [0]*len(fonts)
			for i in range(0,len(fonts)):
				url = "https://www.ncbi.nlm.nih.gov/"+fonts[i]+"/?term=%22"+expression+"%22"
				html = urlopen(url).read()
				#if it exists
				if (re.search("Quoted phrase not found",html) is None) or (re.search("No items found.",html) is None):
					#if it is one
					cap = re.search("Items:",html)
					if cap is None:
						values[i] = 1
					else:
						start = cap.start()
						quote = html[start:(start+50)]
						cap = re.search("of",quote)
						#if less than 20
						if cap is None:
							start = re.search("Items:",quote).end()
						else:
							start = re.search("of",quote).end()
						end = re.search("</h",quote).start()
						quote = quote[start:end]
						values[i] = int(filter(str.isdigit, quote))
				else:
					values[i] = 0
			#print("Classe: "+hier_class)
			#print("Name: "+pure_expression)
			query = "" 
			for value in values:
				query = query + "," + str(value)
			#print("Values: "+query)
			#print("\n")
			#print("\n")
			return(values)

def create_datasets(filename):
	lines = open("/home/zamith/Documents/Grad_e_IC/8o_Semestre/BEPE/"+filename,"r").readlines()
	attributes = list()
	lines_attributes = list()
	for i in range(0,len(lines)):
		line = lines[i].split('\n')[0]
		cap = re.search("@ATTRIBUTE",line)
		if cap is not None:
			quote = line[cap.end()+1:len(line)]
			end = re.search(" ",quote).start()
			quote = quote[:end]
			if quote != "class":
				lines_attributes.append(line)
				attributes.append(quote)
			else:
				quote=line[re.search("hierarchical ",line).end():len(line)]
				classes = re.split(',',quote)
				for i in range(0,len(classes)):
					quote = "@ATTRIBUTE "+str(classes[i])+" numeric"
					attributes.append(classes[i])
					lines_attributes.append(quote)
		else:
			cap = re.search("@DATA",line)
			if cap is not None:
				start = i+1
				end = len(lines)
				break


	lines = lines[start:end]
	df = pd.DataFrame(0, index=np.arange(len(lines)), columns=attributes)
	transpose = pd.DataFrame(0, index=np.arange(len(lines)), columns=classes)
	for i in range(0,len(lines)):
		lines[i] = lines[i].split('\n')[0]
		quote = lines[i].split(',')
		quote2 = quote[len(quote)-1].split('@')
		fill = quote[0:len(quote)-1]
		fill2 = [0]*len(classes)
		fill = fill + fill2
		for j in range(0,len(quote2)):
			cap = list(df).index(quote2[j])
			fill[cap] = 1
			cap = classes.index(quote2[j])
			fill2[cap] = 1
			ancestors = ancestorTotal(quote2[j])
			for k in range(0,len(ancestors)):
				cap = list(df).index(ancestors[k])
				fill[cap] = 1
				cap = classes.index(quote2[j])
				fill2[cap] = 1
		transpose.iloc[i]=fill2
		df.iloc[i]=fill

	#Writes intD1
	writer = open("/home/zamith/Documents/Grad_e_IC/8o_Semestre/BEPE/intD1_"+filename,"w")
	for i in range(0,len(lines_attributes)):
		writer.write(lines_attributes[i]+'\n')

	writer.write('\n')
	writer.write('@DATA\n')
	csv = df.to_csv(header=None, index=False).strip('\n').split('\n')
	for i in range(0,len(csv)):
		writer.write(csv[i]+'\n')

	writer.close()


	transpose = transpose.T 
	attributes = ["cdd","ipg","protein","proteinclusters","sparcle","structure"]
	lines_attributes = list()

	for i in range(0,len(attributes)):
		lines_attributes.append("@ATTRIBUTE "+attributes[i]+" numeric")

	for i in range(0,len(list(transpose))):
		quote = "Protein"+str(i)
		attributes.append(quote)
		lines_attributes.append("@ATTRIBUTE "+quote+" numeric")

	df = pd.DataFrame(0, index=np.arange(len(transpose)), columns=attributes)

	for i in range(0,len(list(transpose.index))):
		fill = get_query(list(transpose.index)[i])
		fill = fill + list(transpose.iloc[i])
		df.iloc[i]=fill



	#Writes intD2
	writer = open("/home/zamith/Documents/Grad_e_IC/8o_Semestre/BEPE/intD2_"+filename,"w")
	for i in range(0,len(lines_attributes)):
		writer.write(lines_attributes[i]+'\n')

	writer.write('\n')
	writer.write('@DATA\n')
	csv = df.to_csv(header=None, index=False).strip('\n').split('\n')
	for i in range(0,len(csv)):
		writer.write(csv[i]+'\n')

	writer.close()

parser = argparse.ArgumentParser(description='Please write the filename', add_help=True)
parser.add_argument('-i','--input', dest='inputFile', metavar='inputFile', type=str, help='Dataset', required=True)
args = parser.parse_args()

create_datasets(args.inputFile)