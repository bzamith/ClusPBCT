import re
from urllib import urlopen

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
			print("Classe: "+hier_class)
			print("Name: "+pure_expression)
			query = "" 
			for value in values:
				query = query + "," + str(value)
			print("Values: "+query)
			print("\n")
			print("\n")
			return(values)




