import os
import sys
import re
import argparse
import subprocess
import pandas as pd
from pathlib import Path


class Dataset:
	def __init__(self,file_name='',data_type=''):
		self.file_name = file_name
		self.data_type = data_type
		self.intD1 = ''
		self.intD2_path = ''
		self.intD2_depth = ''
		self.intD2_subtree = ''
		self.intD2_regular = ''
		self.header = ''
		self.intD1_attr_names = ''
		self.intD1_labels_names = ''
		self.intD2_path_attr_names = ''
		self.intD2_depth_attr_names = ''
		self.intD2_subtree_attr_names = ''
		self.intD2_regular_attr_names = ''
		self.intD2_path_labels_names = ''
		self.intD2_depth_labels_names = ''
		self.intD2_subtree_labels_names = ''
		self.intD2_regular_labels_names = ''
		self.target_begin = 0
		self.target_end = 0
	def set_intD1(self,intD1):
		self.intD1 = intD1
	def set_intD2_path(self,intD2):
		self.intD2_path = intD2
	def set_intD2_depth(self,intD2):
		self.intD2_depth = intD2
	def set_intD2_subtree(self,intD2):
		self.intD2_subtree = intD2
	def set_intD2_regular(self,intD2):
		self.intD2_regular = intD2
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
	def set_intD2_subtree_attr_names(self,attr_names):
		self.intD2_subtree_attr_names = attr_names
	def set_intD2_regular_attr_names(self,attr_names):
		self.intD2_regular_attr_names = attr_names
	def set_intD2_path_labels_names(self,labels_names):
		self.intD2_path_labels_names = labels_names
	def set_intD2_depth_labels_names(self,labels_names):
		self.intD2_depth_labels_names = labels_names
	def set_intD2_subtree_labels_names(self,labels_names):
		self.intD2_subtree_labels_names = labels_names
	def set_intD2_regular_labels_names(self,labels_names):
		self.intD2_regular_labels_names = labels_names
	def set_intD2_attr_names(self,attr_names,approach):
		approach = approach.upper()
		if approach == "PATH":
			self.intD2_path_attr_names = attr_names
		elif approach == "DEPTH":
			self.intD2_depth_attr_names = attr_names
		elif approach == "SUBTREE":
			self.intD2_subtree_attr_names = attr_names
		elif approach == "REGULAR":
			self.intD2_regular_attr_names = attr_names
		else:
			print("\t\t! Unknown approach in set_intD2_attr_names: "+approach)
			sys.exit()
	def set_intD2_labels_names(self,labels_names,approach):
		approach = approach.upper()
		if approach == "PATH":
			self.intD2_path_labels_names = labels_names
		elif approach == "DEPTH":
			self.intD2_depth_labels_names = labels_names
		elif approach == "SUBTREE":
			self.intD2_subtree_labels_names = labels_names 
		elif approach == "REGULAR":
			self.intD2_regular_labels_names = labels_names
		else:
			print("\t\t! Unknown approach in set_intD2_labels_names: "+approach)
			sys.exit()
	def set_intD2(self,data_frame,approach):
		approach = approach.upper()
		if approach == "PATH":
			self.intD2_path = data_frame
		elif approach == "DEPTH":
			self.intD2_depth = data_frame
		elif approach == "SUBTREE":
			self.intD2_subtree = data_frame 
		elif approach == "REGULAR":
			self.intD2_regular = data_frame
		else:
			print("\t !Unknown approach in set_intD2: "+approach)
			sys.exit()
	def get_file_name(self):
		return self.file_name
	def get_intD2_path(self):
		return self.intD2_path
	def get_intD2_depth(self):
		return self.intD2_depth
	def get_intD2_subtree(self):
		return self.intD2_subtree
	def get_intD2_regular(self):
		return self.intD2_regular
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
	def get_intD2_subtree_attr_names(self):
		return self.intD2_subtree_attr_names
	def get_intD2_regular_attr_names(self):
		return self.intD2_regular_attr_names	
	def get_intD2_path_labels_names(self):
		return self.intD2_path_labels_names
	def get_intD2_depth_labels_names(self):
		return self.intD2_depth_labels_names
	def get_intD2_subtree_labels_names(self):
		return self.intD2_subtree_labels_names
	def get_intD2_regular_labels_names(self):
		return self.intD2_regular_labels_names
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
		elif approach == "SUBTREE":
			return self.intD2_subtree_attr_names
		elif approach == "REGULAR":
			return self.intD2_regular_attr_names
		else:
			print("\t\t! Unknown approach in get_intD2_attr_names: "+approach)
			sys.exit()
	def get_intD2_labels_names(self,approach):
		approach = approach.upper()
		if approach == "PATH":
			return self.intD2_path_labels_names
		elif approach == "DEPTH":
			return self.intD2_depth_labels_names
		elif approach == "SUBTREE":
			return self.intD2_subtree_labels_names
		elif approach == "REGULAR":
			return self.intD2_regular_labels_names
		else:
			print("\t\t! Unknown approach in get_intD2_labels_names: "+approach)
			sys.exit()
	def get_intD2(self,approach):
		approach = approach.upper()
		if approach == "PATH":
			return self.intD2_path
		elif approach == "DEPTH":
			return self.intD2_depth
		elif approach == "SUBTREE":
			return self.intD2_subtree
		elif approach == "REGULAR":
			return self.intD2_regular
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
	# returns subtree from a given node and a given array of labels
	# input: node = 001/003/01 labels = [001,001/003,001/002,001/003/01,001/003/01/40,002,002/50,004]
	# return: [001/003/01/40]
	def subTreeComplete(self):
		if self.node == '':
			print("\t\t! Can't obtain subTreeComplete for node = empty")
			sys.exit()
		if self.labels == '':
			print("\t\t! Can't obtain subTreeComplete for labels = empty")
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
	# h_train = execute for train dataset?, by default = True
	# h_valid = execute for validation dataset?, by default = True
	# h_test = execute for test dataset?, by default = True
	# g_path = create path dataset?, by default = True
	# g_subtree = create subtree dataset?, by default = True
	# g_depth = create depth dataset?, by default = True
	# g_regular = create regular dataset?, by default = True
	train = ''
	valid = ''
	trainvalid = ''
	test = ''
	def __init__(self, file_name, file_path=os.path.abspath(os.curdir), h_train = True, h_valid = True, h_test = True, 
		g_path = True, g_subtree = True, g_depth = True, g_regular = True):
		
		if h_train:
			self.train = Dataset(file_name,"train")
		if h_valid:
			self.valid = Dataset(file_name,"valid")
			if h_train:
				self.trainvalid = Dataset(file_name,"trainvalid")
		if h_test:
			self.test = Dataset(file_name,"test")

		# read all datasets
		self.read_datasets(file_path, file_name, h_train, h_valid, h_test)
		# get interaction datasets (intD2)
		self.get_interaction_datasets(h_train,h_valid, g_path, g_depth, g_subtree, g_regular)
		# write datasets
		if h_train:
			self.write_arff(self.train,"intD1",file_name+"_intD1_train.arff")
			print("\t\t> Wrote intD1_train")
			if g_path:
				self.write_arff(self.train,"path",file_name+"_intD2_path_train.arff")
				print("\t\t> Wrote intD2_path_train")
				self.create_settings_file(self.train,"Path")
				print("\t\t> Created settings file for path")
			if g_depth:
				self.write_arff(self.train,"depth",file_name+"_intD2_depth_train.arff")
				print("\t\t> Wrote intD2_depth_train")
				self.create_settings_file(self.train,"Depth")
				print("\t\t> Created settings file for depth")
			if g_subtree:
				self.write_arff(self.train,"subtree",file_name+"_intD2_subtree_train.arff")
				print("\t\t> Wrote intD2_subtree_train")
				self.create_settings_file(self.train,"Subtree")
				print("\t\t> Created settings file for subtree")
			if g_regular:
				self.write_arff(self.train,"regular",file_name+"_intD2_regular_train.arff")
				print("\t\t> Wrote intD2_regular_train")
				self.create_settings_file(self.train,"Regular")
				print("\t\t> Created settings file for regular")
		if h_valid:
			self.write_arff(self.valid,"intD1",file_name+"_intD1_valid.arff")
			print("\t\t> Wrote intD1_valid")
			if h_train:
				self.write_arff(self.trainvalid,"intD1",file_name+"_intD1_trainvalid.arff")
				print("\t\t> Wrote intD1_trainvalid")
		if h_test:
			self.write_arff(self.test,"intD1",file_name+"_intD1_test.arff")
			print("\t\t> Wrote intD1_test")
	def read_datasets(self, file_path, file_name, h_train, h_valid, h_test):
		#read train
		if(h_train):
			file = self.check_file_exists(file_path, file_name, "train")
			self.extract_dataset_info(file,self.train)
			print("\t\t> Read train dataset and created intD1_train")
		#read valid
		if(h_valid):
			file = self.check_file_exists(file_path, file_name, "valid")
			self.extract_dataset_info(file,self.valid)
			print("\t\t> Read valid dataset and created intD1_valid")
			if(h_train):
				self.trainvalid.set_intD1(self.train.get_intD1().append(self.valid.get_intD1(), ignore_index = True))
				self.trainvalid.set_intD1_attr_names(self.train.get_intD1_attr_names())
				self.trainvalid.set_intD1_labels_names(self.train.get_intD1_labels_names())
				print("\t\t> Created intD1_trainvalid")
		#read test
		if(h_test):
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
				if "numeric" in line.lower():
					attr_names.append(line[len("@ATTRIBUTE")+1:len(line)-len("numeric")-1])
				elif "{" in line:
					attr_names.append(line[len("@ATTRIBUTE")+1:line.rfind('{')-1])
				elif "class hierarchical" in line.lower():
					labels_names = line[len("@ATTRIBUTE class hierarchical "):len(line)].split(",")
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
	def get_interaction_datasets(self,h_train,h_valid, g_path, g_depth, g_subtree, g_regular):
		if h_train:
			nbRows = len(self.train.get_intD1_labels_names())
			labels = self.train.get_intD1_labels_names()
			if g_path:
				path_dataframe = pd.DataFrame(columns=labels)
			if g_depth:
				hier = Hierarchy(labels=self.train.get_intD1_labels_names())
				levels = [str(x) for x in range(0,hier.nbLevels())]
				depth_dataframe = pd.DataFrame(columns=levels)
			if g_subtree:
				subtree_dataframe = pd.DataFrame(columns=labels)
			if g_regular:
				hier = Hierarchy(labels=labels)
				firstLevel = hier.nodesFirstLevel()
				regular_dataframe = pd.DataFrame(columns=firstLevel)
			for i in range(0,nbRows):
				if g_path:
					attr_values = [0]*path_dataframe.shape[1]
					hier = Hierarchy(node=labels[i])
					ancestors = hier.ancestorsComplete()
					for item in ancestors:
						attr_values[labels.index(item)]=1
					path_dataframe.loc[path_dataframe.shape[0]] = attr_values
				if g_depth:
					attr_values = [0]*depth_dataframe.shape[1]
					hier = Hierarchy(node=labels[i])
					nodeLevels = hier.nodeLevels()
					for item in nodeLevels:
						attr_values[levels.index(item)]=1
					depth_dataframe.loc[depth_dataframe.shape[0]] = attr_values
				if g_subtree:
					attr_values = [0]*subtree_dataframe.shape[1]
					hier = Hierarchy(node=labels[i],labels=labels)
					subTree = hier.subTreeComplete()
					for item in subTree:
						attr_values[labels.index(item)]=1
					subtree_dataframe.loc[regular_dataframe.shape[0]] = attr_values
				if g_regular:
					attr_values = [0]*regular_dataframe.shape[1]
					hier = Hierarchy(node=labels[i])
					first = hier.nodesFirstLevel()
					attr_values[firstLevel.index(first)]=1
					regular_dataframe.loc[regular_dataframe.shape[0]] = attr_values
			if g_path:
				self.save_interaction_datasets(self.train,path_dataframe,"PATH",self.train.get_intD1_labels_names())
				print("\t\t> Created intD2_path_train")
				if h_valid:
					self.save_interaction_datasets(self.trainvalid,path_dataframe,"PATH",self.trainvalid.get_intD1_labels_names())
					print("\t\t> Created intD2_path_trainvalid")
			if g_depth:
				self.save_interaction_datasets(self.train,depth_dataframe,"DEPTH",["Level"+str(x) for x in range(0,len(levels))])
				print("\t\t> Created intD2_depth_train")
				if h_valid:
					self.save_interaction_datasets(self.trainvalid,depth_dataframe,"DEPTH",["Level"+str(x) for x in range(0,len(levels))])
					print("\t\t> Created intD2_depth_trainvalid")
			if g_subtree:
				self.save_interaction_datasets(self.train,subtree_dataframe,"SUBTREE",self.train.get_intD1_labels_names())
				print("\t\t> Created intD2_subtree_train")
				if h_valid:
					self.save_interaction_datasets(self.trainvalid,subtree_dataframe,"SUBTREE",self.trainvalid.get_intD1_labels_names())
					print("\t\t> Created intD2_subtree_trainvalid")
			if g_regular:
				self.save_interaction_datasets(self.train,regular_dataframe,"REGULAR",firstLevel)
				print("\t\t> Created intD2_regular_train")
				if h_valid:
					self.save_interaction_datasets(self.trainvalid,regular_dataframe,"REGULAR",firstLevel)
					print("\t\t> Created intD2_regular_trainvalid")
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

class Tuner:
	tuned = ["AUPRC","Weighted","Pooled"]
	tuned_values = [0,0,0]
	tuned_out_file = ["Average AUPRC:","Average AUPRC \\(weighted\\):","Pooled AUPRC:"]
	tuned_out_predicted = [0,0,0]
	def __init__(self,file_name,g_path=True,g_depth=True,g_subtree=True,g_regular=True):
		path = os.path.abspath(os.curdir)
		if g_path:
			command = "java -jar Clus_v5.jar "+"tune_"+file_name+"_path.s > output_tune_path.txt"
			print("\t\t> Tuned path")
			subprocess.call(command, shell=True)
			os.remove("tune_"+file_name+"_path.out")
			self.read_tuned_out_values(file_name,"PATH")
			print("\t\t> Obtained tuned values for path")
			self.create_settings_file(file_name,"PATH")
			print("\t\t> Created settings files for path")
			self.execute_all(file_name,"PATH")
			print("\t\t> Executed Clus for path")
		if g_depth:
			command = "java -jar Clus_v5.jar "+"tune_"+file_name+"_depth.s > output_tune_depth.txt"
			print("\t\t> Tuned depth")
			subprocess.call(command, shell=True)
			os.remove("tune_"+file_name+"_depth.out")
			self.read_tuned_out_values(file_name,"DEPTH")
			print("\t\t> Obtained tuned values for depth")
			self.create_settings_file(file_name,"DEPTH")
			print("\t\t> Created settings files for depth")
			self.execute_all(file_name,"DEPTH")
			print("\t\t> Executed Clus for depth")
		if g_subtree:
			command = "java -jar Clus_v5.jar "+"tune_"+file_name+"_subtree.s > output_tune_subtree.txt"
			print("\t\t> Tuned subtree")
			subprocess.call(command, shell=True)
			os.remove("tune_"+file_name+"_subtree.out")
			self.read_tuned_out_values(file_name,"SUBTREE")
			print("\t\t> Obtained tuned values for subtree")
			self.create_settings_file(file_name,"SUBTREE")
			print("\t\t> Created settings files for subtree")
			self.execute_all(file_name,"SUBTREE")
			print("\t\t> Executed Clus for subtree")
		if g_regular:
			command = "java -jar Clus_v5.jar "+"tune_"+file_name+"_regular.s > output_tune_regular.txt"
			print("\t\t> Tuned regular")
			subprocess.call(command, shell=True)
			os.remove("tune_"+file_name+"_regular.out")
			self.read_tuned_out_values(file_name,"REGULAR")
			print("\t\t> Obtained tuned values for regular")
			self.create_settings_file(file_name,"REGULAR")
			print("\t\t> Created settings files for regular")
			self.execute_all(file_name,"REGULAR")
			print("\t\t> Executed Clus for regular")
	def read_tuned_out_values(self,file_name,data_type):
		lines = open("output_tune_"+data_type.lower()+".txt",'r').readlines()
		os.remove("output_tune_"+data_type.lower()+".txt")
		pos = 0
		for i in range(0,len(lines)):
			if(lines[i].rstrip()==file_name+"_intD2_"+data_type.lower()+"_train.arff"):
				pos = i
				break
		if not pos == 0:
			self.tuned_values[0]=float(lines[pos-3].rstrip())
			self.tuned_values[1]=float(lines[pos-2].rstrip())
			self.tuned_values[2]=float(lines[pos-1].rstrip())
		else:
			print("\t\t! No tuned values found")
			sys.exit()
	def create_settings_file(self,file_name,data_type):
		lines = open("tune_"+file_name+"_"+data_type.lower()+".s",'r').readlines()
		os.remove("tune_"+file_name+"_"+data_type.lower()+".s")
		pos = 0
		for i in range(0,len(lines)):
			if(lines[i].startswith("FTest = ")):
				pos = i
				break
		if not pos == 0:
			for i in range(0,len(self.tuned_values)):
				lines[pos] = "FTest = "+str(self.tuned_values[i])+"\n"
				with open("run_"+file_name+"_"+data_type.lower()+"_"+self.tuned[i].lower()+".s", 'w') as output:
					for j in range(0,len(lines)):
						output.write(lines[j])
		else:
			print("\t\t! Couldnt create settings file for "+data_type.lower())
			sys.exit()
	def execute_all(self,file_name,data_type):
		for i in range(0,len(self.tuned_values)):
			command = "java -jar Clus_v5.jar run_"+file_name+"_"+data_type.lower()+"_"+self.tuned[i].lower()+".s > temp.txt"
			subprocess.call(command, shell=True)
			os.remove("temp.txt")
			os.remove("run_"+file_name+"_"+data_type.lower()+"_"+self.tuned[i].lower()+".s")
			lines = open("run_"+file_name+"_"+data_type.lower()+"_"+self.tuned[i].lower()+".out",'r').readlines()
			os.remove("run_"+file_name+"_"+data_type.lower()+"_"+self.tuned[i].lower()+".out")
			count = 0
			for j in range(0,len(lines)):
				print
				if re.search(self.tuned_out_file[i],lines[j].rstrip()):
					count = count+1
				if count==2:
					self.tuned_out_predicted[i]=float(re.findall("\d+\.\d+",lines[j])[0])
					break
		with open("output_"+file_name+"_"+data_type.lower()+".txt",'w') as output:
			output.write(file_name+"\n\n")
			for i in range(0,len(self.tuned_values)):
				output.write(str(self.tuned_values[i])+"\n")
			output.write("\n\n")
			for i in range(0,len(self.tuned_values)):
				output.write(str(self.tuned_out_predicted[i])+"\n")

class FolderOrganizer:
	def __init__(self,file_name,file_path=os.path.abspath(os.curdir)):
		files = os.listdir(file_path)
		if not os.path.exists(file_path+"/Output"):
			os.makedirs(file_path+"/Output")
		if not os.path.exists(file_path+"/Output/"+file_name):
			os.makedirs(file_path+"/Output/"+file_name)
		if not os.path.exists(file_path+"/Output/"+file_name+"/Measures"):
			os.makedirs(file_path+"/Output/"+file_name+"/Measures")
		if not os.path.exists(file_path+"/Output/"+file_name+"/IntDatasets"):
			os.makedirs(file_path+"/Output/"+file_name+"/IntDatasets")
		if not os.path.exists(file_path+"/Output/"+file_name+"/OrgDatasets"):
			os.makedirs(file_path+"/Output/"+file_name+"/OrgDatasets")

		for file in files:
			find = file.find(file_name)
			if not find == -1:
				find = file.find("output_")
				if not find == -1:
					os.rename(file_path+"/"+file, file_path+"/Output/"+file_name+"/Measures/"+file)
				else:
					find = file.find("intD")
					if not find == -1:
						os.rename(file_path+"/"+file, file_path+"/Output/"+file_name+"/IntDatasets/"+file)
					else:
						os.rename(file_path+"/"+file, file_path+"/Output/"+file_name+"/OrgDatasets/"+file)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Please give the dataset file name', add_help=True)
	parser.add_argument('-i','--input', dest='inputFile', metavar='inputFile', type=str, help='Dataset', required=True)
	args = parser.parse_args()
	print("\n\n")
	print("> Beginning Execution for Dataset: "+args.inputFile)
	print("\t> DatasetsGenerator...")
	DatasetsGenerator(file_name = args.inputFile)
	print("\t> Tuner...")
	Tuner(file_name = args.inputFile)
	print("\t> Organizer...")
	FolderOrganizer(file_name=args.inputFile)
	print("> End of Execution for Dataset: "+args.inputFile)