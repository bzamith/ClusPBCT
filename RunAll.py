import subprocess
import re
import argparse
import os

tunes = ["Auroc","AUPRC","Weighted","Pooled"]
tunes_values =[0,0,0,0]
tunes_out_file = ["Average AUROC:","Average AUPRC:","Average AUPRC \\(weighted\\):","Pooled AUPRC:"]
tunes_out_predicted = [0,0,0,0]

def runall(name):
	path = os.path.abspath(os.curdir)
	os.chdir(path+"/"+name)
	command = "java -jar ../Clus_v5.jar "+"Tune"+name+".s > OutputTuning.txt"
	subprocess.call(command, shell=True)
	os.remove("Tune"+name+".out")

	lines = open("OutputTuning.txt","r").readlines()
	pos = 0
	for i in range(0,len(lines)):
		if (lines[i]=="intD2_"+name.lower()+"_FUN.train.arff\n"):
			pos = i
			break

	if pos != 0:
		tunes_values[0] = float(lines[pos-4].replace('\n',''))
		tunes_values[1] = float(lines[pos-3].replace('\n',''))
		tunes_values[2] = float(lines[pos-2].replace('\n',''))
		tunes_values[3] = float(lines[pos-1].replace('\n',''))
	else:
		print("Error 1!")

	lines = open("Run"+name+".s","r").readlines()
	pos = 0
	for i in range(0,len(lines)):
		if(lines[i].startswith("FTest = ")):
			pos = i
			break

	if pos!=0:
		for i in range(0,4):
			with open("Run"+name+tunes[i]+".s", "w") as output:
				for j in range(0,len(lines)):
					if j!=pos:
						output.write(lines[j])
					else:
						output.write("FTest = "+str(tunes_values[i])+"\n")
	else:
		print("Error 2!")

	for i in range(0,4):
		command = "java -jar ../Clus_v5.jar Run"+name+tunes[i]+".s > Output"+name+tunes[i]+".txt"
		subprocess.call(command, shell=True)
		lines = open("Run"+name+tunes[i]+".out", "r").readlines()
		count = 0
		for j in range(0,len(lines)):
			if re.search(tunes_out_file[i],lines[j]):
				count = count+1
			if count == 2:
				tunes_out_predicted[i]=float(re.findall("\d+\.\d+",lines[j])[0])
				break

	with open("SaidaFinal.txt","w") as output:
		output.write(name+"\n\n")
		for i in range(0,4):
			output.write(str(tunes_values[i])+"\n")
		output.write("\n\n")
		for i in range(0,4):
			output.write(str(tunes_out_predicted[i])+"\n")


parser = argparse.ArgumentParser(description='Please write the dataset name', add_help=True)
parser.add_argument('-i','--input', dest='inputFile', metavar='inputFile', type=str, help='Dataset', required=True)
args = parser.parse_args()

runall(args.inputFile)