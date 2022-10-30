# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from email import header
from typing import Dict
from unicodedata import name
import pandas as pd
import re
import openpyxl
import matplotlib.pyplot as plt
import uuid
from datetime import date
import os

# https://realpython.com/documenting-python-code/#docstrings-background

class Nex:

	def __init__(self):
		print('__init__()')

		# load datasets data & meta
		self.datasetsDf = pd.DataFrame(self.readDataToDf('datasets.xlsx'))
		self.headersDf = pd.DataFrame(self.readHeadersToDf('datasets.xlsx'))
		#self.printDatasets()

		self.selectedDatasetIndex = ''
		self.selectedRecordIndex = ''

		self.tableDf = pd.DataFrame()
		self.tableHeaderDf = pd.DataFrame()
		self.importDf = pd.DataFrame()
		
		self.datasetsMethods = pd.Series([
			'printDatasets', 
			'createDataset', 
			'readDataset', # todo - load dataset, view attributes in list, calculate total
			'renameDataset', # todo - read dataset, delete, create 
			'deleteDataset',  
			'snippetTest'
		])
		
		self.tableMethods = pd.Series([
			'printTable', 
			'addTableColumn',  
			'dropTableColumn', 
			'createRecord', 
			'readRecord',
			'updateRecord',
			'deleteRecord', 
			'importRecords', 
			'tableSnippet',
			'backToDatasets'
		])

		self.promptOptions = self.datasetsMethods

		
		## END method ----------------------

	# -------------
	# datasets init
	# -------------

	def getPromptOptions(self):
		return self.promptOptions
	
	def getNavigation(self):
		str = ''
		# if not self.selectedRecordIndex:
		# 	datasetname = self.datasetsDf.loc[self.selectedDatasetIndex, 'name']
		# 	str = f'Navigation: {datasetname}'
		# else: 
		# 	datasetname = self.datasetsDf.loc[self.selectedDatasetIndex, 'name']
		# 	tablename = self.datasetsDf.loc[self.selectedRecordIndex, 'name']
		# 	str = f'Navigation: {datasetname} / {tablename}'
			
		return str
		## END method ----------------------
		
	def readDataToDf(self, file):
		try:
			data = pd.read_excel(file, sheet_name='data')
			# headers = pd.DataFrame(pd.read_excel(file, sheet_name='headers'))
			return data
			# return {'data':data,'headers':headers}

		except OSError as e:
			print("ERROR: Unable to find or access file:", e)
			pass

		## END method ----------------------

	def readHeadersToDf(self, file):
		try:
			headers = pd.read_excel(file, sheet_name='headers')
			#headers = pd.DataFrame(pd.read_excel(file, sheet_name='headers'))
			# headers = pd.read_excel(file, sheet_name='headers').to_dict()
			return headers

		except OSError as e:
			print("ERROR: Unable to find or access file:", e)
			pass

		## END method ----------------------

	def printDatasets(self):
		print(self.datasetsDf['name'])

		# todo - check dataset exists, get total & report

		## END method ----------------------

	# -------------
	# datasets CRUD
	# -------------

	def createDataset(self):
		print('\n|\n|\n|')
		print('createDataset()')

		# todo - check if "name" already exists
		# get dataset name
		messagePrompt = f'Name Dataset: '
		resDict = processUserInput(messagePrompt)
		#print(resDict)
		if resDict['valid']:
			value = str(resDict['value'])
			filename = f'{value}.xlsx'

			# todo - value to lowercase, replace spaces with _
			rowDict = {
			 "ID": uuid.uuid4(),
			 "created": date.today().strftime("%m/%d/%Y"),
			 "name": value,
			 "source": filename,
			 "status": 'active'
			}
			#print(rowDict)

			# add row to datasets
			self.datasetsDf = self.datasetsDf.append(rowDict, ignore_index=True)

			#print(self.datasetsDf.head())

			# build dataset table
			#headDict = pd.Series(['ID','created','modified','name'])
			dataDf = pd.DataFrame({
			 'ID': pd.Series(dtype='int'),
			 'created': pd.Series(dtype='str'),
			 'modified': pd.Series(dtype='str'),
			 'name': pd.Series(dtype='str')
			})
			#print(dataDf)

			headers = dataDf.columns
			#print(headers)

			headersDf = pd.DataFrame({
			 'name': pd.Series(dtype='str'),
			 'dtype': pd.Series(dtype='str'),
			 'alias': pd.Series(dtype='str'),
			 'editable': pd.Series(dtype='str')
			})

			#headerDict = dict()
			for idx, x in enumerate(headers):
				#print(f'index:{idx},id:{x}')

				if x == 'ID':
					dtypeValue = 'int'
				else:
					dtypeValue = 'str'

				if x == 'name':
					editableValue = 'True'
				else:
					editableValue = 'False'

				headerRowDict = {
				 "name": x,
				 "dtype": dtypeValue,
				 "alias": x,
				 "editable": editableValue
				}

				headersDf = headersDf.append(headerRowDict, ignore_index=True)

			#print(headersDf)

			# safe dataset
			dataDf = dataDf.set_index('ID')
			headersDf = headersDf.set_index('name')

			with pd.ExcelWriter(f'datasets/{filename}') as writer:
				dataDf.to_excel(writer, sheet_name='data')
				headersDf.to_excel(writer, sheet_name='headers')

			# update datesets

			with pd.ExcelWriter(f'datasets.xlsx') as writer:
				self.datasetsDf.set_index('ID').to_excel(writer, sheet_name='data')
				self.headersDf.set_index('name').to_excel(writer, sheet_name='headers')

		#self.datasetsDf.set_index('ID').to_excel("datasets.xlsx", sheet_name='data')
		# todo - update datasets.xlsx
		#self.datasetsDf.to_excel("datasets.xlsx", sheet_name='data')

		## END method ----------------------

	def readDataset(self):
		print('\n|\n|\n|')
		print('readDataset()')

		# get datasets as options
		#self.printDatasets()
		
		for index, row in self.datasetsDf.iterrows():
			print(f'{index}: {row["name"]}')
		
		# get index input
		inputMessagePrompt = f'Select Dataset: '
		indexSelection = int(input(inputMessagePrompt))
		print(f'indexSelection: {indexSelection}')

		self.selectedDatasetIndex = indexSelection
		#self.selectedDataset = self.datasetsDf.loc[indexSelection, 'name']
		
		source = self.datasetsDf.loc[indexSelection, 'source']
		location = f'datasets/{source}'
		print(f'location: {location}')

		self.tableDf = pd.DataFrame(self.readDataToDf(location))
		self.tableHeaderDf = pd.DataFrame(self.readHeadersToDf(location))
		print(self.tableDf)
		print(self.tableHeaderDf)

		# set options
		self.promptOptions = self.tableMethods
			


				
		# read dataset
		# add dataframe to datasets dictionary
		# update dataset report and print
		# show dataset options

		# make select dataset from report

		# try:
		#     data = pd.read_excel(file, sheet_name='data')
		#     # headers = pd.DataFrame(pd.read_excel(file, sheet_name='headers'))
		#     return data
		#     # return {'data':data,'headers':headers}

		# except OSError as e:
		#     print("ERROR: Unable to find or access file:", e)
		#     pass

		## END method ----------------------

	def snippetTest(self):

		headers = self.datasetsDf.columns
		print(headers)

		headerDict = dict()
		for idx, x in enumerate(headers):
			headerDict[idx]['name'] = x
			if x == 'name':
				headerDict[idx]['dtype'] = 'str'
			else:
				headerDict[idx]['dtype'] = 'int'
			headerDict[idx]['alias'] = x
			if x == 'name':
				headerDict[idx]['editable'] = 'True'
			else:
				headerDict[idx]['editable'] = 'False'
			headerDict[idx]['picklist'] = ''

		print(headerDict)

	## END method ----------------------

	def updateDataset(self):
		print('\n|\n|\n|')
		print('updateDataset()')

		## END method ----------------------

	def deleteDataset(self):
		print('\n|\n|\n|')
		print('deleteDataset()')

		# print options
		for index, row in self.datasetsDf.iterrows():
			print(f'{index}: {row["name"]}')

		# get index input
		prompt = f'Index to delete: '
		indexSelection = int(input(prompt))

		# remove file if exists
		source = self.datasetsDf.loc[indexSelection, 'source']
		filename = f'datasets/{source}'
		print(filename)
		if os.path.exists(filename):
			os.remove(filename)
		else:
			print("The file does not exist")

		# remove from dataset
		self.datasetsDf = self.datasetsDf.drop(indexSelection)
		print(self.datasetsDf.head())

		# reindex
		self.datasetsDf = self.datasetsDf.reset_index(drop=True)
		print(self.datasetsDf.head())

		# safe dataset.xlsx
		with pd.ExcelWriter(f'datasets.xlsx') as writer:
			self.datasetsDf.set_index('ID').to_excel(writer, sheet_name='data')
			self.headersDf.set_index('name').to_excel(writer, sheet_name='headers')

		## END method ----------------------

	# -------------
	# dataset table CRUD
	# -------------

	def printTable(self):
		print(self.tableDf)

		# todo - check dataset exists, get total & report

		## END method ----------------------

		## END method ----------------------
	def addTableColumn(self):
		print('\n|\n|\n|')
		print('addTableColumn()')

		df = self.tableDf

		# # 
		# messagePrompt = f'column name: '
		# newColumn = input(messagePrompt)

		# #
		# messagePrompt = f'default value if any; "today" for todays date: '
		# defaultValue = input(messagePrompt)

		# if defaultValue == 'today':
		# 	df[newColumn] = date.today().strftime("%m/%d/%Y")
		# else: 
		# 	df[newColumn] = defaultValue

		# print(df)
		# print(df.info())
		
		# self.importDf = df
		
		
		## END method ----------------------

		
	def dropTableColumn(self):
		print('\n|\n|\n|')
		print('dropTableColumn()')
		
		df = self.tableDf
		
		for idx, x in enumerate(df.columns):
			print(f'{idx}: {x}')
				
		# 
		messagePrompt = f'column to drop: '
		index = int(input(messagePrompt))
		
		df.drop(df.columns[index],axis=1,inplace=True)
		#df.drop(colName, axis=1, inplace=True)
		
		print(df.head())
		print(df.info())
		
		self.tableDf = df
		headers = self.tableDf.columns
		
		# todo - turn into func and prevent ID, created, modified from being edited
		tempTableHeaderDf = pd.DataFrame()
		for idx, x in enumerate(headers):
			print(f'{idx}: {x}')

			editable = ""
			if x == 'ID':
				editable = "FALSE"
			elif x == 'created':
				editable = "FALSE"
			elif x == 'modified':
				editable = "FALSE"
			else:
				editable = "TRUE"

			headerRowDict = {
			 "name": x,
			 "dtype": 'str',
			 "alias": x,
			 "editable": editable
			}

			tempTableHeaderDf = pd.concat([tempTableHeaderDf, pd.DataFrame(headerRowDict, index=[0])], ignore_index = True)

		self.tableHeaderDf = tempTableHeaderDf
		print(self.tableHeaderDf)

		# get table location
		source = self.datasetsDf.loc[self.selectedDatasetIndex, 'source']
		print(f'location: {source}')
		
		with pd.ExcelWriter(f'datasets/{source}') as writer:
			self.tableDf.to_excel(writer, sheet_name='data')
			self.tableHeaderDf.to_excel(writer, sheet_name='headers')

		# todo - create new file, archive old one in folder by table name; do same for imports
		
		## END method ----------------------
		
		
	def createRecord(self):
		print('\n|\n|\n|')
		print('createRecord()')

		# todo - check if "name" already exists
		# get dataset name
		messagePrompt = f'Name Record: '
		resDict = processUserInput(messagePrompt)
		#print(resDict)
		if resDict['valid']:
			value = str(resDict['value'])
			filename = f'{value}.xlsx'

			# todo - value to lowercase, replace spaces with _
			rowDict = {
			 "ID": uuid.uuid4(),
			 "created": date.today().strftime("%m/%d/%Y"),
			 "name": value
			}
			print(rowDict)

			# add row to datasets2
			self.tableDf = self.tableDf.append(rowDict, ignore_index=True)

			# get table location
			source = self.datasetsDf.loc[self.selectedDatasetIndex, 'source']
			location = f'datasets/{source}'
			print(f'location: {location}')

			#safe dataset.xlsx
			with pd.ExcelWriter(location) as writer:
				self.tableDf.set_index('ID').to_excel(writer, sheet_name='data')
				self.tableHeaderDf.set_index('name').to_excel(writer, sheet_name='headers')

		## END method ----------------------

	
	def readRecord(self):
		
		# print table name
		name = self.datasetsDf.loc[self.selectedDatasetIndex, 'name']
		print(f'Table: {name}')
		
		# select record
		for index, row in self.tableDf.iterrows():
			print(f'{index}: {row["name"]}')

		# get index input
		prompt = f'Index to read: '
		indexSelection = int(input(prompt))
				
		# print table name
		name = self.tableDf.loc[indexSelection, 'name']
		print(f'Record: {name}')

		self.selectedRecordIndex = indexSelection
		
		for index, row in self.tableHeaderDf.iterrows():
			print(f'{row["name"]}: {self.tableDf.loc[indexSelection, row["name"]]}')
			#print(f'{row}: {self.tableDf.loc[indexSelection, row["name"]]}')

		# get table meta, loop through & print each attribute
		#print(self.tableHeaderDf)



		
		## END method ----------------------

	
	def updateRecord(self):
		
		# select record
		name = self.datasetsDf.loc[self.selectedDatasetIndex, 'name']
		print(f'Table: {name}')
		
		# select record
		for index, row in self.tableDf.iterrows():
			print(f'{index}: {row["name"]}')

		# get index input
		prompt = f'Select Record: '
		tableIndexSelection = int(input(prompt))
				
		# print table name
		name = self.tableDf.loc[tableIndexSelection, 'name']
		print(f'Record: {name}')
		
		self.tableHeaderDf.replace({'editable': {'TRUE': True, 'FALSE': False}})
		
		for index, row in self.tableHeaderDf.iterrows():
			if row["editable"]:
				print(f'{index}: {row["name"]}, {row["editable"]}')
			
		# select attribute to update

		# get index input
		prompt = f'Column index to update: '
		headerIndexSelection = int(input(prompt))
		print(f'headerIndexSelection: {headerIndexSelection}')

		print(self.tableHeaderDf)
		
		tableHeaderValue = self.tableHeaderDf.loc[headerIndexSelection,'name']
		print(f'{tableIndexSelection}: {tableHeaderValue}')
		
		prompt = f'new value: '
		inputStr = input(prompt)
		print(f'inputStr: {inputStr}')
		
		self.tableDf.loc[tableIndexSelection,tableHeaderValue] = inputStr
		self.tableDf.loc[tableIndexSelection,'modified'] = date.today().strftime("%m/%d/%Y")
		print(self.tableDf)

		# make change and set modified date
		source = self.datasetsDf.loc[self.selectedDatasetIndex, 'source']
		location = f'datasets/{source}'
		print(f'location: {location}')
		
		# update dataset
		with pd.ExcelWriter(location) as writer:
			self.tableDf.set_index('ID').to_excel(writer, sheet_name='data')
			self.tableHeaderDf.set_index('name').to_excel(writer, sheet_name='headers')


		
		## END method ----------------------

	
	def deleteRecord(self):
		print('\n|\n|\n|')
		print('deleteRecord()')

		# print options
		for index, row in self.tableDf.iterrows():
			print(f'{index}: {row["name"]}')

		# get index input
		prompt = f'Index to delete: '
		indexSelection = int(input(prompt))

		# # remove file if exists
		# source = self.tableDf.loc[indexSelection, 'source']
		# filename = f'datasets/{source}'
		# print(filename)
		# if os.path.exists(filename):
		# 	os.remove(filename)
		# else:
		# 	print("The file does not exist")

		# remove from dataset
		self.tableDf = self.tableDf.drop(indexSelection)
		print(self.tableDf.head())

		# reindex
		self.tableDf = self.tableDf.reset_index(drop=True)
		print(self.tableDf.head())

		# get table location
		source = self.datasetsDf.loc[self.selectedDatasetIndex, 'source']
		location = f'datasets/{source}'
		print(f'location: {location}')

		#safe dataset.xlsx
		with pd.ExcelWriter(location) as writer:
			self.tableDf.set_index('ID').to_excel(writer, sheet_name='data')
			self.tableHeaderDf.set_index('name').to_excel(writer, sheet_name='headers')

		## END method ----------------------



	
	def importRecords(self):
		print('\n|\n|\n|')
		print('importRecords()')

		# get import file name
		# messagePrompt = f'Import File Name: '
		# resDict = processUserInput(messagePrompt)
		# #print(resDict)
		# if resDict['valid']:
		# 	filename = str(resDict['value'])

		# 	location = f'imports/{filename}'
		# 	print(f'location: {location}')

			#self.importDf = pd.DataFrame(self.readDataToDf(location))

		print('\n|\n|\n|')
		print('importRecords()')
		"""
		Parameters
		----------
		name : str
			The name of the animal
		sound : str
			The sound the animal makes
		num_legs : int, optional
			The number of legs the animal (default is 4)
		
		Steps
		----------
		- read file to dataframe
		- clean operations
			drop columns
		- map columns to selected dataset
		
		 
		"""
		
		# get import file name
		messagePrompt = f'Import File Name: '
		resDict = processUserInput(messagePrompt)

		self.promptOptions = pd.Series([
			'mapColumn', 
			'addColumn', 
			'dropColumn',
			'performImport', 
			'backToDatasets'
		])
		
		#print(resDict)
		if resDict['valid']:
			testFilename = str(resDict['value'])
		
			# get extension - Chase9901.csv, Export.csv
			#testFilename = 'Chase1885.csv'
			extension = testFilename.split(".")
			print(extension)
			
			location = f'imports/{testFilename}'
			print(f'location: {location}')
		
			# load by extension type
			self.importDf = pd.read_csv(location)
			#pd.options.display.max_rows = 9999
			
			print(self.importDf)
			print(self.importDf.info())
		
		## END method ----------------------



	# -------------
	# import functions
	# -------------


		
	def mapColumn(self):
		print('\n|\n|\n|')
		print('mapColumn()')

		## END method ----------------------
	def addColumn(self):
		print('\n|\n|\n|')
		print('addColumn()')

		df = self.importDf

		# 
		messagePrompt = f'column name: '
		newColumn = input(messagePrompt)

		#
		messagePrompt = f'default value if any; "today" for todays date: '
		defaultValue = input(messagePrompt)

		if defaultValue == 'today':
			df[newColumn] = date.today().strftime("%m/%d/%Y")
		else: 
			df[newColumn] = defaultValue

		print(df)
		print(df.info())
		
		self.importDf = df
		
		
		## END method ----------------------
	def dropColumn(self):
		print('\n|\n|\n|')
		print('dropColumn()')

		df = self.importDf
		
		for idx, x in enumerate(self.importDf.columns):
			print(f'{idx}: {x}')
				
		# 
		messagePrompt = f'column to drop: '
		index = int(input(messagePrompt))
		
		df.drop(df.columns[index],axis=1,inplace=True)
		#df.drop(colName, axis=1, inplace=True)
		
		print(df)
		print(df.info())
		
		self.importDf = df

		## END method ----------------------
	def performImport(self):
		print('\n|\n|\n|')
		print('performImport()')

		df = self.importDf
		
		importColumns = df.columns
		
		# select record
		newDf = pd.DataFrame()
		newDf = self.tableDf

		
		for index, row in df.iterrows():
			print(f'{index}: {row}')

			rowDict = dict()
			
			for index, headRow in self.tableHeaderDf.iterrows():
				print(f'{index}: {headRow["name"]}')
				#rowDict[x] = df.loc[index,x]
				if headRow["name"] == 'ID':
					rowDict[headRow["name"] ] = uuid.uuid4()
				elif headRow["name"] == 'created':
					rowDict[headRow["name"] ] = date.today().strftime("%m/%d/%Y")
				else:
					rowDict[headRow["name"] ] = ''
					
			# rowDict = {
			#  "ID": uuid.uuid4(),
			#  "created": date.today().strftime("%m/%d/%Y"),
			#  "modified": ""
			# }
	
			for idx, x in enumerate(importColumns):
				print(f'{idx}: {x}')
				rowDict[x] = row[x]
	
			
			print(rowDict)
			
			rowDf = pd.DataFrame(rowDict, index=[0])
			print('rowDf')
			print(rowDf)

			newDf = pd.concat([newDf, rowDf], ignore_index = True)
		

		self.tableDf = newDf

		# get headers from new df
		headers = self.tableDf.columns
		print(headers)

		# headersDf = pd.DataFrame({
		#  'name': pd.Series(dtype='str'),
		#  'dtype': pd.Series(dtype='str'),
		#  'alias': pd.Series(dtype='str'),
		#  'editable': pd.Series(dtype='str')
		# })
		print(headers)
		
		# todo - turn into func and prevent ID, created, modified from being edited
		tempTableHeaderDf = pd.DataFrame()
		for idx, x in enumerate(headers):
			print(f'{idx}: {x}')

			headerRowDict = {
			 "name": x,
			 "dtype": 'str',
			 "alias": x,
			 "editable": 'True'
			}

			tempTableHeaderDf = tempTableHeaderDf.append(headerRowDict, ignore_index=True)

		self.tableHeaderDf = tempTableHeaderDf
		print(self.tableHeaderDf)

		# safe dataset
		self.tableDf = self.tableDf.set_index('ID')
		self.tableHeaderDf = self.tableHeaderDf.set_index('name')
		
		source = self.datasetsDf.loc[self.selectedDatasetIndex, 'name']
		filename = f'{source}_{date.today().strftime("%m%d%Y")}.xlsx'
		print(filename)

		with pd.ExcelWriter(f'datasets/{filename}') as writer:
			self.tableDf.to_excel(writer, sheet_name='data')
			self.tableHeaderDf.to_excel(writer, sheet_name='headers')

		# # update datesets

		self.datasetsDf.loc[self.selectedDatasetIndex,'source'] = filename
		#print(self.datasetsDf.loc[self.selectedDatasetIndex,:])
		
		with pd.ExcelWriter(f'datasets.xlsx') as writer:
			self.datasetsDf.set_index('ID').to_excel(writer, sheet_name='data')
			self.headersDf.set_index('name').to_excel(writer, sheet_name='headers')

	

		# return to main menu
		self.promptOptions = self.datasetsMethods
		
		## END method ----------------------



	
	def tableSnippet(self):
		print('\n|\n|\n|')
		print('tableSnippet()')

		df = self.tableDf

		feature = ['sumGroup','updateStatus','sumTotal']

		for idx, x in enumerate(feature):
			print(f'{idx}: {x}')

		messagePrompt = f'select operation: '
		index = int(input(messagePrompt))

		print(f'--- {feature[index]}') 
		if index == 0: 
			
			for idx, x in enumerate(df.columns):
				print(f'{idx}: {x}')
	
			messagePrompt = f'select column: '
			index = int(input(messagePrompt))
		
			#groupDf = df.groupby(df.columns[index]).sum()
			column = df.columns[index]
			groupDf = df.groupby(column)["Amount"].sum()
			print(groupDf.head())

		elif index == 1: 
			print(f'--- {feature[index]}') 


			
		elif index == 2:
			print(f'--- {feature[index]}') 
		else: 
			print("--- try again") 
		
		#print(getattr(p1, option, lambda: p1.default)())
		
		## END method ----------------------

	
		
	
	def backToDatasets(self):
		print('\n|\n|\n|')
		print('backToDatasets()')

		self.promptOptions = self.datasetsMethods
		## END method ----------------------

		



		
	# -------------
	# helper functions
	# -------------
		
	def readCSVtoDataframe(self, location):
		try:
			df = pd.read_csv(location)
			# headers = pd.DataFrame(pd.read_excel(file, sheet_name='headers'))
			return df
			# return {'data':data,'headers':headers}

		except OSError as e:
			print("ERROR: Unable to find or access file:", e)
			pass

		## END method ----------------------
			
	def writeDatasetToExcel(self, file):
		try:
			data = pd.read_excel(file, sheet_name='data')
			# headers = pd.DataFrame(pd.read_excel(file, sheet_name='headers'))
			return data
			# return {'data':data,'headers':headers}

		except OSError as e:
			print("ERROR: Unable to find or access file:", e)
			pass

		## END method ----------------------

	

	# 	## END method ----------------------

	# def getDf(self):
	# 	return self.df

	# 	## END method ----------------------

	# def getSumbyColumn(self):
	# 	column = 'calories'
	# 	return self.df[column].sum()

	# 	## END method ----------------------

	# def printDfInfo(self):
	# 	print(self.df.info())

	# 	## END method ----------------------

	# def printDfHead(self):
	# 	print(self.df.head())

	# 	## END method ----------------------

	# def printList(self):
	# 	return print(self.df[['type', 'calories']])

	# 	## END method ----------------------




		
	#
	# table CRUD
	#

	def addItem(self):
		print('\n|\n|\n|')
		print('addItem()')

		headers = list(self.df)
		print(headers)

		rowDict = dict()
		for x in headers:
			print(x)
			prompt = f'Input value for "{x}": '
			inputValue = input(prompt)
			rowDict[x] = inputValue

		print(rowDict)
		self.df = self.df.append(rowDict, ignore_index=True)
		print(self.df.head())

		# inputMessagePrompt = 'Select option:'
		# optionNumber = int(input(inputMessagePrompt))

		print('------------')
		## END method ----------------------

	def removeItem(self):
		print('\n|\n|\n|')
		print('removeItem()')
		indexDf = self.df.reset_index()

		for index, row in indexDf.iterrows():
			print(f'{index}: {row["type"]}')

		prompt = f'Index to delete: '
		indexSelection = int(input(prompt))

		self.df = self.df.drop(indexSelection)
		# self.df = newDF.reset_index()
		print(self.df.head())

		## END method ----------------------

	def editItem(self):
		print('\n|\n|\n|')
		print('editItem()')
		indexDf = self.df.reset_index()

		print(self.df.head())

		indexPrompt = f'Index to edit: '
		indexSelection = int(input(indexPrompt))

		columns = self.df.columns
		rowDict = dict()
		for idx, x in enumerate(columns):
			print(f'{idx}: {x}')
			rowDict[idx] = x

		columnPrompt = f'Index to edit: '
		columnSelection = int(input(columnPrompt))

		print(f'selected row: {indexSelection}, column: {columnSelection}')

		valuePrompt = f'change to: '
		value = int(input(valuePrompt))

		self.df.iloc[indexSelection,
					 self.df.columns.get_loc(rowDict[columnSelection])] = value

		print(self.df.head())

		## END method ----------------------

	# def returnUserInfo(self, user_id):
	#     # https://pythonguides.com/case-statement-in-python/#:~:text=Switch%20case%20in%20Python%20with%20user%20input,-Let%20us%20see&text=The%20user_id%20is%20passed%20to,in%20the%20switch%20case%20statement.

	#     user_info = {
	#         1001: 'James',
	#         1002: 'Rosy',
	#         1003: 'Ben',
	#         1004: 'John',
	#         1005: 'Mary'
	#     }
	#     return user_info.get(user_id, 'Invalid User ID')

	# def myfunc(self):
	#     print("Hello my name is " + self.name)


# --- END CLASS ------------------------------------------------------------------------ #

p1 = Nex()



# todo - move out of class
def initateUserInput():

	# get current options list from class
	# optionsList = p1.getPromptOptions()
	# numMethods = int(len(optionsList))
	# print(f'numMethods: {numMethods}')

	inputMessagePrompt = 'Select option:'

	while True:

		print(f'-----------')
		optionsList = p1.getPromptOptions()
		numMethods = int(len(optionsList))
		print(f'numMethods: {numMethods}')
		print(p1.getNavigation())
	
		print(f'-----------')
		# show options
		for idx, x in optionsList.items():
			print(f'{idx}: {x}')

		print(f'-----------')

		# strIn = raw_input("Enter text: ");
		resDict = processUserInput(inputMessagePrompt)
		#print(resDict)
		if resDict['valid']:
			optionNumber = int(resDict['value'])
			#print(f'optionNumber: {optionNumber} -- numMethods: {numMethods}')
			if (optionNumber <= numMethods):
				# break;
				option = optionsList.get(optionNumber, '')
				print(f'Selected option: {option}')
				print(f'-----------')
				print(getattr(p1, option, lambda: p1.default)())

	## END method ----------------------

# todo - move out of class
def processUserInput(message):

	# set up return
	retDict = {'valid': True}
	inputValue = input(message)
	# inputValue = inputValue.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+", "")
	inputValue = re.sub('[^a-zA-Z0-9 \n\.]', '', inputValue)

	if inputValue == "":
		retDict['valid'] = False
	else:
		# todo - check type by column name and match type then convert
		retDict['value'] = inputValue

	return retDict


initateUserInput()

