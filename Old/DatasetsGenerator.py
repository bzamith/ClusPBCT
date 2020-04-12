import os
import sys
import re
import argparse
import subprocess
import pandas as pd
from pathlib import Path
from shutil import copyfile


class Dataset:
	def __init__(self,file_name='',data_type=''):
		self.file_name = file_name
		self.data_type = data_type
		self.intD1 = ''
		self.intD2_path = ''
		self.intD2_depth = ''
		self.intD2_children = ''
		self.intD2_subtree = ''
		self.header = ''
		self.intD1_attr_names = ''
		self.intD1_labels_names = ''
		self.intD2_path_attr_names = ''
		self.intD2_depth_attr_names = ''
		self.intD2_children_attr_names = ''
		self.intD2_subtree_attr_names = ''
		self.intD2_path_labels_names = ''
		self.intD2_depth_labels_names = ''
		self.intD2_children_labels_names = ''
		self.intD2_subtree_labels_names = ''
		self.target_begin = 0
		self.target_end = 0
	def set_intD1(self,intD1):
		self.intD1 = intD1
	def set_intD2_path(self,intD2):
		self.intD2_path = intD2
	def set_intD2_depth(self,intD2):
		self.intD2_depth = intD2
	def set_intD2_children(self,intD2):
		self.intD2_children = intD2
	def set_intD2_subtree(self,intD2):
		self.intD2_subtree = intD2
	def set_header(self,header):
		self.header = header
	def set_intD1_attr_names(self,attr_names):
		self.intD1_attr_names = attr_names
		self.target_begin = len(attr_names)+1
	def set_intD1_labels_names(self,labels_names):
		self.intD1_labels_names = labels_names
		self.target_end = self.target_begin + len(labels_names) - 1
	def set_intD2_path_attr_names(self,attr_names):
		self.intD2_path_attr_names = attr_names
	def set_intD2_depth_attr_names(self,attr_names):
		self.intD2_depth_attr_names = attr_names
	def set_intD2_children_attr_names(self,attr_names):
		self.intD2_children_attr_names = attr_names
	def set_intD2_subtree_attr_names(self,attr_names):
		self.intD2_subtree_attr_names = attr_names
	def set_intD2_path_labels_names(self,labels_names):
		self.intD2_path_labels_names = labels_names
	def set_intD2_depth_labels_names(self,labels_names):
		self.intD2_depth_labels_names = labels_names
	def set_intD2_children_labels_names(self,labels_names):
		self.intD2_children_labels_names = labels_names
	def set_intD2_subtree_labels_names(self,labels_names):
		self.intD2_subtree_labels_names = labels_names
	def set_intD2_attr_names(self,attr_names,approach):
		approach = approach.upper()
		if approach == "PATH":
			self.intD2_path_attr_names = attr_names
		elif approach == "DEPTH":
			self.intD2_depth_attr_names = attr_names
		elif approach == "CHILDREN":
			self.intD2_children_attr_names = attr_names
		elif approach == "SUBTREE":
			self.intD2_subtree_attr_names = attr_names
		else:
			print("\t\t! Unknown approach in set_intD2_attr_names: "+approach)
			sys.exit()
	def set_intD2_labels_names(self,labels_names,approach):
		approach = approach.upper()
		if approach == "PATH":
			self.intD2_path_labels_names = labels_names
		elif approach == "DEPTH":
			self.intD2_depth_labels_names = labels_names
		elif approach == "CHILDREN":
			self.intD2_children_labels_names = labels_names 
		elif approach == "SUBTREE":
			self.intD2_subtree_labels_names = labels_names
		else:
			print("\t\t! Unknown approach in set_intD2_labels_names: "+approach)
			sys.exit()
	def set_intD2(self,data_frame,approach):
		approach = approach.upper()
		if approach == "PATH":
			self.intD2_path = data_frame
		elif approach == "DEPTH":
			self.intD2_depth = data_frame
		elif approach == "CHILDREN":
			self.intD2_children = data_frame 
		elif approach == "SUBTREE":
			self.intD2_subtree = data_frame
		else:
			print("\t !Unknown approach in set_intD2: "+approach)
			sys.exit()
	def get_file_name(self):
		return self.file_name
	def get_intD2_path(self):
		return self.intD2_path
	def get_intD2_depth(self):
		return self.intD2_depth
	def get_intD2_children(self):
		return self.intD2_children
	def get_intD2_subtree(self):
		return self.intD2_subtree
	def get_header(self):
		return self.header
	def get_intD1(self):
		return self.intD1
	def get_intD1_attr_names(self):
		return self.intD1_attr_names
	def get_intD1_labels_names(self):
		return self.intD1_labels_names
	def get_intD2_path_attr_names(self):
		return self.intD2_path_attr_names
	def get_intD2_depth_attr_names(self):
		return self.intD2_depth_attr_names
	def get_intD2_children_attr_names(self):
		return self.intD2_children_attr_names
	def get_intD2_subtree_attr_names(self):
		return self.intD2_subtree_attr_names	
	def get_intD2_path_labels_names(self):
		return self.intD2_path_labels_names
	def get_intD2_depth_labels_names(self):
		return self.intD2_depth_labels_names
	def get_intD2_children_labels_names(self):
		return self.intD2_children_labels_names
	def get_intD2_subtree_labels_names(self):
		return self.intD2_subtree_labels_names
	def get_target_begin(self):
		return self.target_begin
	def get_target_end(self):
		return self.target_end
	def get_intD2_attr_names(self,approach):
		approach = approach.upper()
		if approach == "PATH":
			return self.intD2_path_attr_names
		elif approach == "DEPTH":
			return self.intD2_depth_attr_names
		elif approach == "CHILDREN":
			return self.intD2_children_attr_names
		elif approach == "SUBTREE":
			return self.intD2_subtree_attr_names
		else:
			print("\t\t! Unknown approach in get_intD2_attr_names: "+approach)
			sys.exit()
	def get_intD2_labels_names(self,approach):
		approach = approach.upper()
		if approach == "PATH":
			return self.intD2_path_labels_names
		elif approach == "DEPTH":
			return self.intD2_depth_labels_names
		elif approach == "CHILDREN":
			return self.intD2_children_labels_names
		elif approach == "SUBTREE":
			return self.intD2_subtree_labels_names
		else:
			print("\t\t! Unknown approach in get_intD2_labels_names: "+approach)
			sys.exit()
	def get_intD2(self,approach):
		approach = approach.upper()
		if approach == "PATH":
			return self.intD2_path
		elif approach == "DEPTH":
			return self.intD2_depth
		elif approach == "CHILDREN":
			return self.intD2_children
		elif approach == "SUBTREE":
			return self.intD2_subtree
		else:
			print("\t\t! Unknown approach in get_intD2: "+approach)
			sys.exit()

class Hierarchy:
	def __init__(self,node='',labels=''):
		self.node = node
		self.labels = labels
	# returns all ancestors of a node
	# input: node = 001/003/01
	# return: [001/003,001]
	def ancestorsComplete(self):
		if self.node == '':
			print("\t\t! Can't obtain ancestorsComplete for node = empty")
			sys.exit()
		s = []
		node = self.node
		s.append(node)
		pos = node.rfind('/')
		while(not pos == -1):
			node = node[0:pos]
			s.append(node)
			pos = node.rfind('/')
		return s
	# returns number of levels in an array of labels
	# input: labels = [001,001/003,001/002,001/003/01,001/003/01/40,002,002/50,004]
	# return: 4 
	def nbLevels(self):
		if self.labels == '':
			print("\t\t! Can't obtain nbLevels for labels = empty")
			sys.exit()
		s = 0
		labels = self.labels
		for i in range(0,len(labels)):
			cur = labels[i].count('/') + 1
			if cur > s:
				s = cur
		return s
	# returns the depth of a certain node
	# input: node = 001/003/01
	# return: [0,1,2]
	def nodeLevels(self):
		if self.node == '':
			print("\t\t! Can't obtain nodeLevel for node = empty")
			sys.exit()
		return [str(x) for x in range(0,self.node.count('/')+1)]
	# returns nodes that are in first level from an array of labels or returns the first level of a given node
	# input: labels = [001,001/003,001/002,001/003/01,001/003/01/40,002,002/50,004]
	# return: [001,002,004]
	# or
	# input: node = 001/003/01
	# return: 001
	def nodesFirstLevel(self):
		if self.labels == '':
			node = self.node
			if node.count('/') == 0:
				return node
			else:
				pos = re.search("/",node).start()
				return node[0:pos]
		elif self.node == '':
			s=[]
			labels = self.labels
			for item in labels:
				if item.count('/') == 0:
					s.append(item)
			return s
		else:
			print("\t\t! Can't obtain nodesFirstLevel for node != empty and labels != empty")
			sys.exit()
	# returns children from a given node and a given array of labels
	# input: node = 001/003/01 labels = [001,001/003,001/002,001/003/01,001/003/01/40,002,002/50,004]
	# return: [001/003/01/40]
	def childrenComplete(self):
		if self.node == '':
			print("\t\t! Can't obtain chilDrenComplete for node = empty")
			sys.exit()
		if self.labels == '':
			print("\t\t! Can't obtain chilDrenComplete for labels = empty")
			sys.exit()
		s = []
		node = self.node
		labels = self.labels
		size = len(node)
		for item in labels:
			pos = re.search(node,item)
			if not pos is None:
				if pos.start() == 0:
					s.append(item)
		return s
	#input: labels = [001/0/0,001/003/0]
	#return: [001,001/003]
	def cleanLabels(self):
		if self.labels == '':
			print("\t\t! Can't obtain cleanLabels for labels = empty")
			sys.exit()
		labels = self.labels 
		s = []
		for item in labels:
			pos = item.rfind("/0")
			while not pos == -1:
				if pos + 2 == len(item):
					item = item[0:pos]
					pos = item.rfind("/0")
				else:
					break
			s.append(item)
		return s

class DatasetsGenerator:
	# file_name = "pheno_yeast_FUN"
	# file_path = "/home/docs/datasets/", by default = working directory
	train = ''
	valid = ''
	trainvalid = ''
	test = ''
	def __init__(self, file_name, file_path=os.path.abspath(os.curdir)):
		self.train = Dataset(file_name,"train")
		self.valid = Dataset(file_name,"valid")
		self.trainvalid = Dataset(file_name,"trainvalid")
		self.test = Dataset(file_name,"test")

		# read all datasets
		self.read_datasets(file_path, file_name)
		# get interaction datasets (intD2)
		self.get_interaction_datasets()
		# write datasets
		copyfile(file_path+"/"+file_name+".train.arff",os.path.abspath(os.curdir)+"/"+file_name+".train.arff")
		copyfile(file_path+"/"+file_name+".valid.arff",os.path.abspath(os.curdir)+"/"+file_name+".valid.arff")
		copyfile(file_path+"/"+file_name+".test.arff",os.path.abspath(os.curdir)+"/"+file_name+".test.arff")
		self.create_settings_file(self.train,"hmc")
		print("\t\t> Created settings file for hmc")
		self.write_arff(self.train,"intD1",file_name+"_intD1_train.arff")
		print("\t\t> Wrote intD1_train")
		self.write_arff(self.train,"path",file_name+"_intD2_path_train.arff")
		print("\t\t> Wrote intD2_path_train")
		self.create_settings_file(self.train,"Path")
		print("\t\t> Created settings file for path")
		self.write_arff(self.train,"depth",file_name+"_intD2_depth_train.arff")
		print("\t\t> Wrote intD2_depth_train")
		self.create_settings_file(self.train,"Depth")
		print("\t\t> Created settings file for depth")
		self.write_arff(self.train,"children",file_name+"_intD2_children_train.arff")
		print("\t\t> Wrote intD2_children_train")
		self.create_settings_file(self.train,"Children")
		print("\t\t> Created settings file for children")
		self.write_arff(self.train,"subtree",file_name+"_intD2_subtree_train.arff")
		print("\t\t> Wrote intD2_subtree_train")
		self.create_settings_file(self.train,"Subtree")
		print("\t\t> Created settings file for subtree")
		self.write_arff(self.valid,"intD1",file_name+"_intD1_valid.arff")
		print("\t\t> Wrote intD1_valid")
		self.write_arff(self.trainvalid,"intD1",file_name+"_intD1_trainvalid.arff")
		print("\t\t> Wrote intD1_trainvalid")
		self.write_arff(self.trainvalid,"path",file_name+"_intD2_path_trainvalid.arff")
		print("\t\t> Wrote intD2_path_trainvalid")
		self.write_arff(self.trainvalid,"depth",file_name+"_intD2_depth_trainvalid.arff")
		print("\t\t> Wrote intD2_depth_trainvalid")
		self.write_arff(self.trainvalid,"children",file_name+"_intD2_children_trainvalid.arff")
		print("\t\t> Wrote intD2_children_trainvalid")
		self.write_arff(self.trainvalid,"path",file_name+"_intD2_subtree_trainvalid.arff")
		print("\t\t> Wrote intD2_subtree_trainvalid")
		self.write_arff(self.test,"intD1",file_name+"_intD1_test.arff")
		print("\t\t> Wrote intD1_test")
	def read_datasets(self, file_path, file_name):
		#read train
		file = self.check_file_exists(file_path, file_name, "train")
		self.extract_dataset_info(file,self.train)
		print("\t\t> Read train dataset and created intD1_train")
		#read valid
		file = self.check_file_exists(file_path, file_name, "valid")
		self.extract_dataset_info(file,self.valid)
		print("\t\t> Read valid dataset and created intD1_valid")
		#create trainvalid
		self.trainvalid.set_header(self.train.get_header())
		self.trainvalid.set_intD1(self.train.get_intD1().append(self.valid.get_intD1(), ignore_index = True))
		self.trainvalid.set_intD1_attr_names(self.train.get_intD1_attr_names())
		self.trainvalid.set_intD1_labels_names(self.train.get_intD1_labels_names())
		print("\t\t> Created intD1_trainvalid")
		#read test
		file = self.check_file_exists(file_path, file_name, "test")
		self.extract_dataset_info(file,self.test)
		print("\t\t> Read test dataset and created intD1_test")
	def check_file_exists(self, file_path, file_name, file_type):
		file = Path(file_path+"/"+file_name+"."+file_type+".arff")
		if not file.is_file():
			file = Path(file_path+"/"+file_name+"_"+file_type+".arff")
			if not file.is_file():
				print("\t\t! No file found: "+file_type)
				sys.exit()
		return file
	def extract_dataset_info(self, file, data_set):
		attr_names = []
		attr_types = []
		labels_names = []
		header = []
		count = 0
		h_key_attr = False
		with open(file, 'r') as dataset_file:
			data = dataset_file.readlines()
		for line in data:
			header.append(line)
			line = line.rstrip()
			if line == '':
				header.pop()
			if "@DATA" in line.upper():
				header.pop()
				break
			if "@ATTRIBUTE" in line.upper():
				if "numeric" in line.lower() or "{" in line.lower():
					spaces = [x.start() for x in re.finditer(' ', line)]
					attr_names.append(line[spaces[0]+1:spaces[1]])
				elif "class" in line.lower() and "hierarchical" in line.lower():
					spaces = [x.start() for x in re.finditer(' ', line)]
					labels_names = line[spaces[len(spaces)-1]+1:len(line)].split(",")
					hier = Hierarchy(labels=labels_names)
					labels_names = hier.cleanLabels()
					header.pop()
				elif "key key" in line.lower():
					h_key_attr = True
					header.pop()
				else:
					print("\t\t! Unknown attribute type: "+line)
					sys.exit()
			count += 1
		intD1 = pd.DataFrame(columns=attr_names+labels_names)
		for i in range(count+1,len(data)-1):
			line = data[i].rstrip()
			if "%" in line:
				line = line[0:line.rfind('%')-1]
			attr_values = line.split(",")
			if h_key_attr:
				attr_values.pop()
			labels_ref = attr_values.pop().split('@')
			hier = Hierarchy(labels=labels_ref)
			labels_ref = hier.cleanLabels()
			labels_values = [0]*len(labels_names)
			for item in labels_ref:
				labels_values[labels_names.index(item)]=1
				hier = Hierarchy(node = item)
				ancestors = hier.ancestorsComplete()
				for item2 in ancestors:
					labels_values[labels_names.index(item2)]=1
			intD1.loc[intD1.shape[0]] = attr_values+labels_values
		data_set.set_intD1(intD1)
		data_set.set_intD1_attr_names(attr_names)
		data_set.set_intD1_labels_names(labels_names)
		data_set.set_header(header)
	def get_interaction_datasets(self):
		nbRows = len(self.train.get_intD1_labels_names())
		labels = self.train.get_intD1_labels_names()
		#path
		path_dataframe = pd.DataFrame(columns=labels)
		#depth
		hier = Hierarchy(labels=self.train.get_intD1_labels_names())
		levels = [str(x) for x in range(0,hier.nbLevels())]
		depth_dataframe = pd.DataFrame(columns=levels)
		#children
		children_dataframe = pd.DataFrame(columns=labels)
		#subtree
		hier = Hierarchy(labels=labels)
		firstLevel = hier.nodesFirstLevel()
		subtree_dataframe = pd.DataFrame(columns=firstLevel)
		for i in range(0,nbRows):
			#path
			attr_values = [0]*path_dataframe.shape[1]
			hier = Hierarchy(node=labels[i])
			ancestors = hier.ancestorsComplete()
			for item in ancestors:
				attr_values[labels.index(item)]=1
			path_dataframe.loc[path_dataframe.shape[0]] = attr_values
			#depth
			attr_values = [0]*depth_dataframe.shape[1]
			hier = Hierarchy(node=labels[i])
			nodeLevels = hier.nodeLevels()
			for item in nodeLevels:
				attr_values[levels.index(item)]=1
			depth_dataframe.loc[depth_dataframe.shape[0]] = attr_values
			#children
			attr_values = [0]*children_dataframe.shape[1]
			hier = Hierarchy(node=labels[i],labels=labels)
			child = hier.childrenComplete()
			for item in child:
				attr_values[labels.index(item)]=1
			children_dataframe.loc[subtree_dataframe.shape[0]] = attr_values
			#subtree
			attr_values = [0]*subtree_dataframe.shape[1]
			hier = Hierarchy(node=labels[i])
			first = hier.nodesFirstLevel()
			attr_values[firstLevel.index(first)]=1
			subtree_dataframe.loc[subtree_dataframe.shape[0]] = attr_values
			
		#path
		self.save_interaction_datasets(self.train,path_dataframe,"PATH",self.train.get_intD1_labels_names())
		print("\t\t> Created intD2_path_train")
		self.save_interaction_datasets(self.trainvalid,path_dataframe,"PATH",self.trainvalid.get_intD1_labels_names())
		print("\t\t> Created intD2_path_trainvalid")
		
		#depth
		self.save_interaction_datasets(self.train,depth_dataframe,"DEPTH",["Level"+str(x) for x in range(0,len(levels))])
		print("\t\t> Created intD2_depth_train")
		self.save_interaction_datasets(self.trainvalid,depth_dataframe,"DEPTH",["Level"+str(x) for x in range(0,len(levels))])
		print("\t\t> Created intD2_depth_trainvalid")
		
		#children
		self.save_interaction_datasets(self.train,children_dataframe,"CHILDREN",self.train.get_intD1_labels_names())
		print("\t\t> Created intD2_children_train")
		self.save_interaction_datasets(self.trainvalid,children_dataframe,"CHILDREN",self.trainvalid.get_intD1_labels_names())
		print("\t\t> Created intD2_children_trainvalid")
		
		#subtree
		self.save_interaction_datasets(self.train,subtree_dataframe,"SUBTREE",firstLevel)
		print("\t\t> Created intD2_subtree_train")
		self.save_interaction_datasets(self.trainvalid,subtree_dataframe,"SUBTREE",firstLevel)
		print("\t\t> Created intD2_subtree_trainvalid")

	def save_interaction_datasets(self,data_set,data_frame,approach,attrs):
		data = data_set.get_intD1().drop(columns = data_set.get_intD1_attr_names())
		data = data.transpose()
		data_set.set_intD2_attr_names(attrs,approach)
		data_set.set_intD2_labels_names(["Protein"+str(x) for x in range(0,data.shape[1])],approach)
		data = pd.concat([data_frame.reset_index(),data.reset_index()],axis=1)
		data_set.set_intD2(data.drop(columns = data.columns.values[0]),approach) # drop index column
	def write_arff(self,data_set,approach,output_file):
		if approach.upper() == "INTD1":
			header = data_set.get_header()
			data_labels_names = data_set.get_intD1_labels_names()
			data_attr_names = data_set.get_intD1_attr_names()
			data_frame = data_set.get_intD1()
		else:
			header = ''
			data_labels_names = data_set.get_intD2_labels_names(approach)
			data_attr_names = data_set.get_intD2_attr_names(approach)
			data_frame = data_set.get_intD2(approach)
		with open(output_file, 'w') as file:
			if not header == '':
				for i in range(0,len(header)):
					file.write(header[i])
				for i in range(0,len(data_labels_names)):
					file.write("@ATTRIBUTE "+data_labels_names[i]+" numeric\n")
			else:
				file.write("@RELATION new")
				file.write('\n\n')
				for i in range(0,len(data_attr_names)):
					file.write("@ATTRIBUTE "+data_attr_names[i]+" numeric\n")
				for i in range(0,len(data_labels_names)):
					file.write("@ATTRIBUTE "+data_labels_names[i]+" numeric\n")
			file.write('\n')
			file.write("@DATA\n")
			vals = data_frame.to_string(header=False,index=False,index_names=False).split('\n')
			vals = [','.join(item.split()) for item in vals]
			for i in range(0,len(vals)):
				file.write(vals[i]+'\n')
	def create_settings_file(self,data_set,approach):
		file_name = data_set.get_file_name()
		with open("tune_"+file_name+"_"+approach.lower()+".s",'w') as file:
			if not approach.lower() == "hmc":
				file.write("[Data]\n")
				file.write("File = "+file_name+"_intD1_train.arff\n")
				file.write("SecondFile = "+file_name+"_intD2_"+approach.lower()+"_train.arff\n")
				file.write("PruneSet = "+file_name+"_intD1_valid.arff\n")
				file.write("%TestSet = "+file_name+"_intD1_test.arff\n")
				file.write("\n")
				file.write("[Hierarchical]\n")
				file.write("Type = TREE\n")
				file.write("HSeparator = /\n")
				file.write("WType = ExpAvgParentWeight\n")
				file.write("\n")
				file.write("[Attributes]\n")
				file.write("Target = "+str(data_set.get_target_begin())+"-"+str(data_set.get_target_end())+"\n")
				file.write("Weights = 1\n")
				file.write("\n")
				file.write("[Tree]\n")
				file.write("FTest = [0.001,0.005,0.01,0.05,0.1,0.125]\n")
				file.write("\n")
				file.write("[Model]\n")
				file.write("MinimalWeight = 5.0\n")
				file.write("\n")
				file.write("[Output]\n")
				file.write("OutputMultiLabelErrors = Yes")
			else:
				file.write("[Data]\n")
				file.write("File = "+file_name+".train.arff\n")
				file.write("PruneSet = "+file_name+".valid.arff\n")
				file.write("TestSet = "+file_name+".test.arff\n")
				file.write("\n")
				file.write("[Hierarchical]\n")
				file.write("Type = TREE\n")
				file.write("HSeparator = /\n")
				file.write("WType = ExpAvgParentWeight\n")
				file.write("OptimizeErrorMeasure = AverageAUPRC\n")
				file.write("\n")
				file.write("[Attributes]\n")
				file.write("Weights = 1\n")
				file.write("\n")
				file.write("[Tree]\n")
				file.write("FTest = [0.001,0.005,0.01,0.05,0.1,0.125]\n")
				file.write("\n")
				file.write("[Model]\n")
				file.write("MinimalWeight = 5.0\n")
				file.write("\n")

class Tuner:
	tuned = ["AUPRC","Weighted","Pooled"]
	tune_names = ["AverageAUPRC","WeightedAverageAUPRC","PooledAUPRC"]
	tuned_out_names = ["Average AUPRC:","Average AUPRC \\(weighted\\):","Pooled AUPRC:"]
	#matrix = [path,subtree,children,depth,hmc]
	#matrix = [auprc,weighted,pooled]
	tuned_ftest = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	tuned_values = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	induction_time = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	nodes = [["","",""],["","",""],["","",""],["","",""],["","",""]]
	def __init__(self,file_name):
		path = os.path.abspath(os.curdir)
		#depth
		command = "java -jar Clus_v5.jar "+"tune_"+file_name+"_depth.s > output_tune"+file_name+"_depth.txt"
		subprocess.call(command, shell=True)
		print("\t\t> Tuned depth")
		os.remove("tune_"+file_name+"_depth.out")
		self.read_tuned_ftest(file_name,"DEPTH")
		print("\t\t> Obtained tuned values for depth")
		self.create_settings_file(file_name,"DEPTH")
		print("\t\t> Created settings files for depth")
		self.execute_all(file_name,"DEPTH")
		print("\t\t> Executed Clus for depth")
		#path
		command = "java -jar Clus_v5.jar "+"tune_"+file_name+"_path.s > output_tune"+file_name+"_path.txt"
		subprocess.call(command, shell=True)
		print("\t\t> Tuned path")
		os.remove("tune_"+file_name+"_path.out")
		self.read_tuned_ftest(file_name,"PATH")
		print("\t\t> Obtained tuned values for path")
		self.create_settings_file(file_name,"PATH")
		print("\t\t> Created settings files for path")
		self.execute_all(file_name,"PATH")
		print("\t\t> Executed Clus for path")
		#children
		command = "java -jar Clus_v5.jar "+"tune_"+file_name+"_children.s > output_tune"+file_name+"_children.txt"
		subprocess.call(command, shell=True)
		print("\t\t> Tuned children")
		os.remove("tune_"+file_name+"_children.out")
		self.read_tuned_ftest(file_name,"CHILDREN")
		print("\t\t> Obtained tuned values for children")
		self.create_settings_file(file_name,"CHILDREN")
		print("\t\t> Created settings files for children")
		self.execute_all(file_name,"CHILDREN")
		print("\t\t> Executed Clus for children")
		#depth
		command = "java -jar Clus_v5.jar "+"tune_"+file_name+"_subtree.s > output_tune"+file_name+"_subtree.txt"
		subprocess.call(command, shell=True)
		print("\t\t> Tuned subtree")
		os.remove("tune_"+file_name+"_subtree.out")
		self.read_tuned_ftest(file_name,"SUBTREE")
		print("\t\t> Obtained tuned values for subtree")
		self.create_settings_file(file_name,"SUBTREE")
		print("\t\t> Created settings files for subtree")
		self.execute_all(file_name,"SUBTREE")
		print("\t\t> Executed Clus for subtree")
		#hmc 
		self.create_settings_file(file_name,"HMC")
		print("\t\t> Created settings files for hmc")
		self.execute_all(file_name,"HMC")
		print("\t\t> Executed Clus for hmc")
		self.write_csv(file_name)
	def read_tuned_ftest(self,file_name,data_type):
		lines = open("output_tune"+file_name+"_"+data_type.lower()+".txt",'r').readlines()
		os.remove("output_tune"+file_name+"_"+data_type.lower()+".txt")
		pos = 0
		index = -1
		if data_type == "PATH":
			index = 0
		elif data_type == "SUBTREE":
			index = 1
		elif data_type == "CHILDREN":
			index = 2
		elif data_type == "DEPTH":
			index = 3
		for i in range(0,len(lines)):
			if(lines[i].rstrip()==file_name+"_intD2_"+data_type.lower()+"_train.arff"):
				pos = i
				break
		if not pos == 0:
			self.tuned_ftest[index][0]=float(lines[pos-3].rstrip())
			self.tuned_ftest[index][1]=float(lines[pos-2].rstrip())
			self.tuned_ftest[index][2]=float(lines[pos-1].rstrip())
		else:
			print("\t\t! No tuned values found")
			sys.exit()
	def create_settings_file(self,file_name,data_type):
		index = -1
		if data_type == "PATH":
			index = 0
		elif data_type == "SUBTREE":
			index = 1
		elif data_type == "CHILDREN":
			index = 2
		elif data_type == "DEPTH":
			index = 3
		lines = open("tune_"+file_name+"_"+data_type.lower()+".s",'r').readlines()
		os.remove("tune_"+file_name+"_"+data_type.lower()+".s")
		posFile = 0
		posFTest = 0
		posOptimizeErrorMeasure = 0
		if not data_type.lower() == "hmc":
			for i in range(0,len(lines)):
				if(lines[i].startswith("FTest = ")):
					posFTest = i
					break
				if(lines[i].startswith("File = ")):
					posFile = i
			if not posFile == 0 and not posFTest == 0:
				lines[posFile] = lines[posFile][0:re.search("train",lines[posFile]).end()]+"valid.arff\n"
				lines[posFile+1] = lines[posFile+1][0:re.search("train",lines[posFile+1]).end()]+"valid.arff\n"
				lines[posFile+2] = "%" + lines[posFile+2]
				lines[posFile+3] = lines[posFile+3][1:len(lines[posFile+3])]
				for i in range(0,len(self.tuned_ftest[index])):
					lines[posFTest] = "FTest = "+str(self.tuned_ftest[index][i])+"\n"
					with open("run_"+file_name+"_"+data_type.lower()+"_"+self.tuned[i].lower()+".s", 'w') as output:
						for j in range(0,len(lines)):
							output.write(lines[j])
			else:
				print("\t\t! Couldnt create settings file for "+data_type.lower())
				sys.exit()
		else:
			for i in range(0,len(lines)):
				if(lines[i].startswith("OptimizeErrorMeasure = ")):
					posOptimizeErrorMeasure = i
					break
			if not posOptimizeErrorMeasure == 0:
				for i in range(0,len(self.tuned_ftest[index])):
					lines[posOptimizeErrorMeasure] = "OptimizeErrorMeasure = "+self.tune_names[i]+"\n"
					with open("run_"+file_name+"_"+data_type.lower()+"_"+self.tuned[i].lower()+".s", 'w') as output:
						for j in range(0,len(lines)):
							output.write(lines[j])
			else:
				print("\t\t! Couldnt create settings file for "+data_type.lower())
				sys.exit()

	def execute_all(self,file_name,data_type):
		index = -1
		if data_type == "PATH":
			index = 0
		elif data_type == "SUBTREE":
			index = 1
		elif data_type == "CHILDREN":
			index = 2
		elif data_type == "DEPTH":
			index = 3
		elif data_type == "HMC":
			index = 4
		for i in range(0,len(self.tuned_ftest[index])):
			command = "java -jar Clus_v5.jar run_"+file_name+"_"+data_type.lower()+"_"+self.tuned[i].lower()+".s > temp_"+file_name+".txt"
			subprocess.call(command, shell=True)
			os.remove("temp_"+file_name+".txt")
			os.remove("run_"+file_name+"_"+data_type.lower()+"_"+self.tuned[i].lower()+".s")
			lines = open("run_"+file_name+"_"+data_type.lower()+"_"+self.tuned[i].lower()+".out",'r').readlines()
			os.remove("run_"+file_name+"_"+data_type.lower()+"_"+self.tuned[i].lower()+".out")
			count = 0
			for j in range(0,len(lines)):
				if index == 4:
					if re.search("FTest = ",lines[j]):
						self.tuned_ftest[index][i] = float(re.findall("\d+\.\d+",lines[j])[0])
				if re.search("Induction Time: ",lines[j]):
					self.induction_time[index][i] = float(re.findall("\d+\.\d+",lines[j])[0])
				if re.search("Nodes =",lines[j]):
					self.nodes[index][i] = lines[j][15:len(lines[j])].rstrip()
				if re.search(self.tuned_out_names[i],lines[j].rstrip()):
					count = count+1
				if count==2:
					self.tuned_values[index][i]=float(re.findall("\d+\.\d+",lines[j])[0])
					break
	def write_csv(self,file_name):
		with open("output_"+file_name+"_tuned_ftest.csv",'w') as output:
			output.write(","+self.tuned[0]+","+self.tuned[1]+","+self.tuned[2]+"\n")
			output.write("Path,"+str(self.tuned_ftest[0][0])+","+str(self.tuned_ftest[0][1])+","+str(self.tuned_ftest[0][2])+"\n")
			output.write("Subtree,"+str(self.tuned_ftest[1][0])+","+str(self.tuned_ftest[1][1])+","+str(self.tuned_ftest[1][2])+"\n")
			output.write("Children,"+str(self.tuned_ftest[2][0])+","+str(self.tuned_ftest[2][1])+","+str(self.tuned_ftest[2][2])+"\n")
			output.write("Depth,"+str(self.tuned_ftest[3][0])+","+str(self.tuned_ftest[3][1])+","+str(self.tuned_ftest[3][2])+"\n")
			output.write("HMC,"+str(self.tuned_ftest[4][0])+","+str(self.tuned_ftest[4][1])+","+str(self.tuned_ftest[4][2])+"\n")
		with open("output_"+file_name+"_tuned_values.csv",'w') as output:
			output.write(","+self.tuned[0]+","+self.tuned[1]+","+self.tuned[2]+"\n")
			output.write("Path,"+str(round(self.tuned_values[0][0],3))+","+str(round(self.tuned_values[0][1],3))+","+str(round(self.tuned_values[0][2],3))+"\n")
			output.write("Subtree,"+str(round(self.tuned_values[1][0],3))+","+str(round(self.tuned_values[1][1],3))+","+str(round(self.tuned_values[1][2],3))+"\n")
			output.write("Children,"+str(round(self.tuned_values[2][0],3))+","+str(round(self.tuned_values[2][1],3))+","+str(round(self.tuned_values[2][2],3))+"\n")
			output.write("Depth,"+str(round(self.tuned_values[3][0],3))+","+str(round(self.tuned_values[3][1],3))+","+str(round(self.tuned_values[3][2],3))+"\n")
			output.write("HMC,"+str(round(self.tuned_values[4][0],3))+","+str(round(self.tuned_values[4][1],3))+","+str(round(self.tuned_values[4][2],3))+"\n")
		with open("output_"+file_name+"_induction_time.csv",'w') as output:
			output.write(","+self.tuned[0]+","+self.tuned[1]+","+self.tuned[2]+"\n")
			output.write("Path,"+str(round(self.induction_time[0][0],3))+","+str(round(self.induction_time[0][1],3))+","+str(round(self.induction_time[0][2],3))+"\n")
			output.write("Subtree,"+str(round(self.induction_time[1][0],3))+","+str(round(self.induction_time[1][1],3))+","+str(round(self.induction_time[1][2],3))+"\n")
			output.write("Children,"+str(round(self.induction_time[2][0],3))+","+str(round(self.induction_time[2][1],3))+","+str(round(self.induction_time[2][2],3))+"\n")
			output.write("Depth,"+str(round(self.induction_time[3][0],3))+","+str(round(self.induction_time[3][1],3))+","+str(round(self.induction_time[3][2],3))+"\n")
			output.write("HMC,"+str(round(self.induction_time[4][0],3))+","+str(round(self.induction_time[4][1],3))+","+str(round(self.induction_time[4][2],3))+"\n")
		with open("output_"+file_name+"_nodes.csv",'w') as output:
			output.write(","+self.tuned[0]+","+self.tuned[1]+","+self.tuned[2]+"\n")
			output.write("Path,"+self.nodes[0][0]+","+self.nodes[0][1]+","+self.nodes[0][2]+"\n")
			output.write("Subtree,"+self.nodes[1][0]+","+self.nodes[1][1]+","+self.nodes[1][2]+"\n")
			output.write("Children,"+self.nodes[2][0]+","+self.nodes[2][1]+","+self.nodes[2][2]+"\n")
			output.write("Depth,"+self.nodes[3][0]+","+self.nodes[3][1]+","+self.nodes[3][2]+"\n")
			output.write("HMC,"+self.nodes[4][0]+","+self.nodes[4][1]+","+self.nodes[4][2]+"\n")

class FolderOrganizer:
	def __init__(self,file_name,file_path=os.path.abspath(os.curdir)):
		files = os.listdir(file_path)
		if not os.path.exists(file_path+"/Output"):
			os.makedirs(file_path+"/Output")
		if not os.path.exists(file_path+"/Output/"+file_name):
			os.makedirs(file_path+"/Output/"+file_name)
		if not os.path.exists(file_path+"/Output/"+file_name+"/Measures"):
			os.makedirs(file_path+"/Output/"+file_name+"/Measures")
		if not os.path.exists(file_path+"/Output/"+file_name+"/Datasets"):
			os.makedirs(file_path+"/Output/"+file_name+"/Datasets")

		os.remove("hierarchy.txt")

		for file in files:
			find = file.find(file_name)
			if not find == -1:
				find = file.find("output_")
				if not find == -1:
					os.rename(file_path+"/"+file, file_path+"/Output/"+file_name+"/Measures/"+file)
				else:
					find = file.find(".arff")
					if not find == -1:
						os.rename(file_path+"/"+file, file_path+"/Output/"+file_name+"/Datasets/"+file)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Please give the dataset file name', add_help=True)
	parser.add_argument('-i','--input', dest='inputFile', metavar='inputFile', type=str, help='Dataset', required=True)
	args = parser.parse_args()
	print("\n\n")
	print("> Beginning Execution for Dataset: "+args.inputFile)
	print("\t> DatasetsGenerator...")
	path=os.path.abspath(os.curdir)+"/Datasets/"+args.inputFile
	DatasetsGenerator(file_name = args.inputFile, file_path=path)
	print("\t> Tuner...")
	Tuner(file_name = args.inputFile)
	print("\t> Organizer...")
	FolderOrganizer(file_name=args.inputFile)
	print("> End of Execution for Dataset: "+args.inputFile)