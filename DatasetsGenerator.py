import os
import sys
import re
import argparse
import pandas as pd
from pathlib import Path

class Hierarchy:
	def __init__(self,node='',labels=''):
		self.node = node
		self.labels = labels

	# returns all ancestors of a node
	# input: node = 001/003/01
	# return: [001/003,001]
	def ancestorsComplete(self):
		if self.node == '':
			print("Can't obtain ancestorsComplete for node = empty")
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
			print("Can't obtain nbLevels for labels = empty")
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
			print("Can't obtain nodeLevel for node = empty")
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
			print("Can't obtain nodesFirstLevel for node != empty and labels != empty")
			sys.exit()

	# returns subtree from a given node and a given array of labels
	# input: node = 001/003/01 labels = [001,001/003,001/002,001/003/01,001/003/01/40,002,002/50,004]
	# return: [001/003/01/40]
	def subTreeComplete(self):
		if self.node == '':
			print("Can't obtain subTreeComplete for node = empty")
			sys.exit()
		if self.labels == '':
			print("Can't obtain subTreeComplete for labels = empty")
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
			print("Can't obtain cleanLabels for labels = empty")
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
	def __init__(self, file_name, file_path=os.path.dirname(os.path.abspath(__file__)), h_train = True, h_valid = False, h_test = False, 
		g_path = True, g_subtree = True, g_depth = True, g_regular = True):
		train_intD1 = '' 
		test_intD1 = ''
		valid_intD1 = ''
		trainvalid_intD1 = ''

		train_intD2_path = ''
		train_intD2_depth = ''
		train_intD2_subtree = ''
		train_intD2_regular = ''

		trainvalid_intD2_path = ''
		trainvalid_intD2_depth = ''
		trainvalid_intD2_subtree = ''
		trainvalid_intD2_regular = ''

		train_header = ''
		test_header = ''
		valid_header = ''
		trainvalid_header = ''

		train_attr_names = ''
		test_attr_names = ''
		valid_attr_names = ''
		trainvalid_attr_names = ''

		train_intD2_path_attr_names = ''
		train_intD2_depth_attr_names = ''
		train_intD2_subtree_attr_names = ''
		train_intD2_regular_attr_names = ''

		trainvalid_intD2_path_attr_names = ''
		trainvalid_intD2_depth_attr_names = ''
		trainvalid_intD2_subtree_attr_names = ''
		trainvalid_intD2_regular_attr_names = ''

		train_intD2_labels_names = ''
		trainvalid_intD2_labels_names = ''

		train_labels_names = ''
		test_labels_names = ''
		valid_labels_names = ''
		trainvalid_labels_names = ''
		
		# read all datasets
		self.read_datasets(file_path, file_name, h_train, h_valid, h_test)
		# get interaction datasets (intD2)
		self.get_interaction_datasets(h_train,h_valid, g_path, g_depth, g_subtree, g_regular)
		# write datasets
		if h_train:
			self.write_arff(self.train_header,self.train_intD1,self.train_labels_names,file_name+"_intD1.arff")
			print("Wrote intD1_train")
			if g_path:
				self.write_arff('',self.train_intD2_path,self.train_intD2_labels_names,file_name+"_intD2_path.arff",data_attr_names=self.train_intD2_path_attr_names)
				print("Wrote intD2_path_train")
			if g_depth:
				self.write_arff('',self.train_intD2_depth,self.train_intD2_labels_names,file_name+"_intD2_depth.arff",data_attr_names=self.train_intD2_depth_attr_names)
				print("Wrote intD2_depth_train")
			if g_subtree:
				self.write_arff('',self.train_intD2_subtree,self.train_intD2_labels_names,file_name+"_intD2_subtree.arff",data_attr_names=self.train_intD2_subtree_attr_names)
				print("Wrote intD2_subtree_train")
			if g_regular:
				self.write_arff('',self.train_intD2_regular,self.train_intD2_labels_names,file_name+"_intD2_regular.arff",data_attr_names=self.train_intD2_regular_attr_names)
				print("Wrote intD2_regular_train")

	def read_datasets(self, file_path, file_name, h_train, h_valid, h_test):
		#read train
		if(h_train):
			file = self.check_file_exists(file_path, file_name, "train")
			self.train_intD1, self.train_attr_names, self.train_labels_names, self.train_header = self.extract_dataset_info(file)
			print("Read Train Dataset and Created intD1_train")
		#read valid
		if(h_valid):
			file = self.check_file_exists(file_path, file_name, "valid")
			self.valid_intD1, self.valid_attr_names, self.valid_labels_names = self.extract_dataset_info(file)
			print("Read Valid Dataset and Created intD1_valid")
			if(h_train):
				if self.valid_intD1.columns.values == self.train_intD1.columns.values:
					self.trainvalid_intD1 = self.train_intD1.append(self.valid_intD1, ignore_index = True)
					self.trainvalid_attr_names = self.train_attr_names
					self.trainvalid_attr_types = self.train_attr_types
					self.trainvalid_labels_names = self.train.labels_names
					print("Read Valid Dataset and Created intD1_trainvalid")
				else:
					print("Cannot append train to valid, different attributes or labels")
					sys.exit()
		#read test
		if(h_test):
			file = self.check_file_exists(file_path, file_name, "test")
			self.test_intD1, self.test_attr_names, self.test_labels_names = self.extract_dataset_info(file)
			print("Read Test Dataset and Created intD1_test")

	def check_file_exists(self, file_path, file_name, file_type):
		file = Path(file_path+"/"+file_name+"."+file_type+".arff")
		if not file.is_file():
			file = Path(file_path+"/"+file_name+"_"+file_type+".arff")
			if not file.is_file():
				print("No file found: "+file_type)
				sys.exit()
		return file

	def extract_dataset_info(self, file):
		attr_names = []
		attr_types = []
		labels_names = []
		header = []
		count = 0
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
				else:
					print("Unknown attribute type: "+line)
					sys.exit()
			count += 1
		intD1 = pd.DataFrame(columns=attr_names+labels_names)
		for i in range(count+1,len(data)-1):
			line = data[i].rstrip()
			if "%" in line:
				line = line[0:line.rfind('%')-1]
			attr_values = line.split(",")
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
		return intD1, attr_names, labels_names, header

	def get_interaction_datasets(self,h_train,h_valid, g_path, g_depth, g_subtree, g_regular):
		if h_train:
			nbRows = len(self.train_labels_names)
			if g_path:
				path_dataframe = pd.DataFrame(columns=self.train_labels_names)
			if g_depth:
				hier = Hierarchy(labels=self.train_labels_names)
				levels = [str(x) for x in range(0,hier.nbLevels())]
				depth_dataframe = pd.DataFrame(columns=levels)
			if g_subtree:
				subtree_dataframe = pd.DataFrame(columns=self.train_labels_names)
			if g_regular:
				hier = Hierarchy(labels=self.train_labels_names)
				firstLevel = hier.nodesFirstLevel()
				regular_dataframe = pd.DataFrame(columns=firstLevel)
			for i in range(0,nbRows):
				if g_path:
					attr_values = [0]*path_dataframe.shape[1]
					hier = Hierarchy(node=self.train_labels_names[i])
					ancestors = hier.ancestorsComplete()
					for item in ancestors:
						attr_values[self.train_labels_names.index(item)]=1
					path_dataframe.loc[path_dataframe.shape[0]] = attr_values
				if g_depth:
					attr_values = [0]*depth_dataframe.shape[1]
					hier = Hierarchy(node=self.train_labels_names[i])
					nodeLevels = hier.nodeLevels()
					for item in nodeLevels:
						attr_values[levels.index(item)]=1
					depth_dataframe.loc[depth_dataframe.shape[0]] = attr_values
				if g_subtree:
					attr_values = [0]*subtree_dataframe.shape[1]
					hier = Hierarchy(node=self.train_labels_names[i],labels=self.train_labels_names)
					subTree = hier.subTreeComplete()
					for item in subTree:
						attr_values[self.train_labels_names.index(item)]=1
					subtree_dataframe.loc[regular_dataframe.shape[0]] = attr_values
				if g_regular:
					attr_values = [0]*regular_dataframe.shape[1]
					hier = Hierarchy(node=self.train_labels_names[i])
					first = hier.nodesFirstLevel()
					attr_values[firstLevel.index(first)]=1
					regular_dataframe.loc[regular_dataframe.shape[0]] = attr_values
			if g_path:
				self.train_intD2_path_attr_names = self.train_labels_names
				self.train_intD2_path = self.train_intD1.drop(columns = self.train_attr_names)
				self.train_intD2_path = self.train_intD2_path.transpose()
				self.train_intD2_labels_names = ["Protein"+str(x) for x in range(0,self.train_intD2_path.shape[1])]
				self.train_intD2_path = pd.concat([path_dataframe.reset_index(),self.train_intD2_path.reset_index()],axis=1)
				self.train_intD2_path = self.train_intD2_path.drop(columns = self.train_intD2_path.columns.values[0]) # drop index column
				print("Created intD2_path_train")
				if h_valid:
					self.trainvalid_intD2_path_attr_names = self.trainvalid_labels_names
					self.trainvalid_intD2_path = self.trainvalid_intD1.drop(columns = self.trainvalid_attr_names)
					self.trainvalid_intD2_path = self.trainvalid_intD2_path.T
					self.trainvalid_intD2_labels_names = ["Protein"+str(x) for x in range(0,self.trainvalid_intD2_path.shape[1])]
					self.trainvalid_intD2_path = pd.concat([path_dataframe.reset_index(),self.trainvalid_intD2_path.reset_index()],axis=1)
					self.trainvalid_intD2_path = self.trainvalid_intD2_path.drop(columns = self.trainvalid_intD2_path.columns.values[0]) # drop index column
					print("Created intD2_path_trainvalid")
			if g_depth:
				self.train_intD2_depth_attr_names = ["Level"+str(x) for x in range(0,len(levels))]
				self.train_intD2_depth = self.train_intD1.drop(columns = self.train_attr_names)
				self.train_intD2_depth = self.train_intD2_depth.transpose()
				self.train_intD2_labels_names = ["Protein"+str(x) for x in range(0,self.train_intD2_depth.shape[1])]
				self.train_intD2_depth = pd.concat([depth_dataframe.reset_index(),self.train_intD2_depth.reset_index()],axis=1)
				self.train_intD2_depth = self.train_intD2_depth.drop(columns = self.train_intD2_depth.columns.values[0]) # drop index column
				print("Created intD2_depth_train")
				if h_valid:
					self.trainvalid_intD2_depth_attr_names = self.train_intD2_depth_attr_names
					self.trainvalid_intD2_depth = self.trainvalid_intD1.drop(columns = self.trainvalid_attr_names)
					self.trainvalid_intD2_depth = self.trainvalid_intD2_depth.T
					self.trainvalid_intD2_labels_names = ["Protein"+str(x) for x in range(0,self.trainvalid_intD2_depth.shape[1])]
					self.trainvalid_intD2_depth = pd.concat([depth_dataframe.reset_index(),self.trainvalid_intD2_depth.reset_index()],axis=1)
					self.trainvalid_intD2_depth = self.trainvalid_intD2_depth.drop(columns = self.trainvalid_intD2_depth.columns.values[0]) # drop index column
					print("Created intD2_depth_trainvalid")
			if g_subtree:
				self.train_intD2_subtree_attr_names = self.train_labels_names
				self.train_intD2_subtree = self.train_intD1.drop(columns = self.train_attr_names)
				self.train_intD2_subtree = self.train_intD2_subtree.transpose()
				self.train_intD2_labels_names = ["Protein"+str(x) for x in range(0,self.train_intD2_subtree.shape[1])]
				self.train_intD2_subtree = pd.concat([subtree_dataframe.reset_index(),self.train_intD2_subtree.reset_index()],axis=1)
				self.train_intD2_subtree = self.train_intD2_subtree.drop(columns = self.train_intD2_subtree.columns.values[0]) # drop index column
				print("Created intD2_subtree_train")
				if h_valid:
					self.trainvalid_intD2_subtree_attr_names = self.train_labels_names
					self.trainvalid_intD2_subtree = self.trainvalid_intD1.drop(columns = self.trainvalid_attr_names)
					self.trainvalid_intD2_subtree = self.trainvalid_intD2_subtree.T
					self.trainvalid_intD2_labels_names = ["Protein"+str(x) for x in range(0,self.trainvalid_intD2_subtree.shape[1])]
					self.trainvalid_intD2_subtree = pd.concat([subtree_dataframe.reset_index(),self.trainvalid_intD2_subtree.reset_index()],axis=1)
					self.trainvalid_intD2_subtree = self.trainvalid_intD2_subtree.drop(columns = self.trainvalid_intD2_subtree.columns.values[0]) # drop index column
					print("Created intD2_subtree_trainvalid")
			if g_regular:
				self.train_intD2_regular_attr_names = firstLevel
				self.train_intD2_regular = self.train_intD1.drop(columns = self.train_attr_names)
				self.train_intD2_regular = self.train_intD2_regular.transpose()
				self.train_intD2_labels_names = ["Protein"+str(x) for x in range(0,self.train_intD2_regular.shape[1])]
				self.train_intD2_regular = pd.concat([regular_dataframe.reset_index(),self.train_intD2_regular.reset_index()],axis=1)
				self.train_intD2_regular = self.train_intD2_regular.drop(columns = self.train_intD2_regular.columns.values[0]) # drop index column
				print("Created intD2_regular_train")
				if h_valid:
					self.trainvalid_intD2_regular_attr_names = firstLevel
					self.trainvalid_intD2_regular = self.trainvalid_intD1.drop(columns = self.trainvalid_attr_names)
					self.trainvalid_intD2_regular = self.trainvalid_intD2_regular.T
					self.trainvalid_intD2_labels_names = ["Protein"+str(x) for x in range(0,self.trainvalid_intD2_regular.shape[1])]
					self.trainvalid_intD2_regular = pd.concat([regular_dataframe.reset_index(),self.trainvalid_intD2_regular.reset_index()],axis=1)
					self.trainvalid_intD2_regular = self.trainvalid_intD2_regular.drop(columns = self.trainvalid_intD2_regular.columns.values[0]) # drop index column
					print("Created intD2_regular_trainvalid")

	def write_arff(self,header,data,data_labels,output_file,data_attr_names=''):
		with open(output_file, 'w') as file:
			if not header == '':
				for i in range(0,len(header)):
					file.write(header[i])
				for i in range(0,len(data_labels)):
					file.write("@ATTRIBUTE "+data_labels[i]+" numeric\n")
			else:
				file.write("@RELATION intD2")
				file.write('\n\n')
				for i in range(0,len(data_attr_names)):
					file.write("@ATTRIBUTE "+data_attr_names[i]+" numeric\n")
				for i in range(0,len(data_labels)):
					file.write("@ATTRIBUTE "+data_labels[i]+" numeric\n")
			file.write('\n')
			file.write("@DATA\n")
			vals = data.to_string(header=False,index=False,index_names=False).split('\n')
			vals = [','.join(item.split()) for item in vals]
			for i in range(0,len(vals)):
				file.write(vals[i]+'\n')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Please give the dataset file name', add_help=True)
	parser.add_argument('-i','--input', dest='inputFile', metavar='inputFile', type=str, help='Dataset', required=True)
	args = parser.parse_args()
	print("Dataset: "+args.inputFile)
	teste = DatasetsGenerator(file_name = args.inputFile, h_valid = False, h_test = False)