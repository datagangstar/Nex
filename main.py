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
from tabulate import tabulate # printing tables
import numpy as np
import ast # string arrays to array

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
		
		self.appTableDf = pd.DataFrame()
		self.appTableHeaderDf = pd.DataFrame()

		self.settingsDict = {}

		self.datasetsMethods = pd.Series([
			'snippetDatasets',
			'printDatasets',
			'viewDataset',
			'readDataset',  # todo - load dataset, view attributes in list
			'createDataset',
			#'renameDataset',  # not used
			'deleteDataset',
			'runStocksApp',
			'runDonationApp',
			'runBodyFatApp',
			'runTransactionsApplication'
		])

		self.tableMethods = pd.Series([
		 	'printTable',
			'addTableColumn',
			#'renameColumn',
			'dropTableColumn',
			'readRecord',
			'deleteRecord',
			'backToDatasets'
		])

		self.promptOptions = self.datasetsMethods

		## END method ----------------------



	# called externally
	def getPromptOptions(self):
		return self.promptOptions

	# called externally but doing nothing but creating a space
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
	
		
	# -------------
	# datasets init
	# -------------


	# called in init
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

	# called in init
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

			
	# called in createDataset
	def writeTableDftoFile(self, filename, tableDf, tableHeaderDf):
		
		# safe dataset
		tableDf = tableDf.set_index('ID')
		tableHeaderDf = tableHeaderDf.set_index('name')

		with pd.ExcelWriter(f'datasets/{filename}') as writer:
			tableDf.to_excel(writer, sheet_name='data')
			tableHeaderDf.to_excel(writer, sheet_name='headers')

		## END method ----------------------
			

	# -------------
	# datasets methods
	# -------------
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




	
	def snippetDatasets(self):
		print('snippetDatasets()')

		headers = self.datasetsDf.columns
		print(headers)

	## END method ----------------------

	
	def printDatasets(self):
		print('\n')
		print('printDatasets()')
		print('---------')

		# datasets schema
		print(self.datasetsDf.info())

		# head table
		print(self.headersDf)
		
		# show table
		headersArray = [
		 "created", "modified", "name", "source"
		]
		
		#print(tabulate(self.datasetsDf[headersArray], headersArray, tablefmt='psql'))

		self.printFormattedTable(self.datasetsDf,headersArray)

		## END method ----------------------

	
	def printFormattedTable(self,df,headersArray):
		
		print(tabulate(df[headersArray], headersArray, tablefmt='psql'))

		## END method ----------------------

		
	def viewDataset(self):
		print('\n')
		print('viewDataset()')
		print('---------')

		# --- show dataset options
		
		# list dataset options
		for index, row in self.datasetsDf.iterrows():
			print(f'{index}: {row["name"]}')

		# --- selectDataset(): get input, set selected dataset, 

		# get index input
		inputMessagePrompt = f'Select Dataset: '
		indexSelection = int(input(inputMessagePrompt))

		# set state
		self.selectedDatasetIndex = indexSelection

		# build location
		source = self.datasetsDf.loc[indexSelection, 'source']
		location = f'datasets/{source}'
		
		# read to dataframe using helper functions
		self.tableDf = pd.DataFrame(self.readDataToDf(location))
		self.tableHeaderDf = pd.DataFrame(self.readHeadersToDf(location))

		# ---
		
		# get table view headers
		headersArray = self.getTableDefaultHeaders()
		
		# viewHeaders = self.datasetsDf.loc[indexSelection, 'default_table']
		# print(viewHeaders)
		# a_list = ast.literal_eval(viewHeaders)
		#viewheadersArr = viewHeaders[1:-1].split(',')

		self.printFormattedTable(self.tableDf,headersArray)
		
			
		## END method ----------------------

		
	def getTableDefaultHeaders(self):

		viewHeaders = self.datasetsDf.loc[self.selectedDatasetIndex, 'default_table']
		viewHeadersArray = ast.literal_eval(viewHeaders)

		return viewHeadersArray
		
		## END method ----------------------
		
		
	def readDataset(self):
		print('\n')
		print('readDataset()')
		print('---------')

		# --- show dataset options
		
		# list dataset options
		for index, row in self.datasetsDf.iterrows():
			print(f'{index}: {row["name"]}')

		# --- selectDataset(): get input, set selected dataset, 
			
		# get index input
		inputMessagePrompt = f'Select Dataset: '
		indexSelection = int(input(inputMessagePrompt))

		# set state
		self.selectedDatasetIndex = indexSelection

		# build location
		source = self.datasetsDf.loc[indexSelection, 'source']
		location = f'datasets/{source}'
		
		# --- load selected table
		
		# read to dataframe using helper functions
		self.tableDf = pd.DataFrame(self.readDataToDf(location))
		self.tableHeaderDf = pd.DataFrame(self.readHeadersToDf(location))

		# set options state
		self.promptOptions = self.tableMethods

		## END method ----------------------

		
	def createDataset(self):
		print('\n')
		print('createDataset()')
		print('---------')

		# --- get input
		
		# todo - check if "name" already exists
		messagePrompt = f'Name Dataset: '
		resDict = processUserInput(messagePrompt)
		
		# --- build table
		
		if resDict['valid']:
			
			# extract value
			value = str(resDict['value'])
			
			# build filename
			filename = f'{value}.xlsx'

			# todo - value to lowercase, replace spaces with _
			rowDict = {
			 "ID": uuid.uuid4(),
			 "created": date.today().strftime("%m/%d/%Y"),
			 "name": value,
			 "source": filename,
			 "status": 'active'
			}

			# add row to datasets
			self.datasetsDf = self.datasetsDf.append(rowDict, ignore_index=True)


			# build dataset table
			# headDict = pd.Series(['ID','created','modified','name'])
			dataDf = pd.DataFrame({
			 'ID': pd.Series(dtype='int'),
			 'created': pd.Series(dtype='str'),
			 'modified': pd.Series(dtype='str')
			})

			# get new df headers
			headers = dataDf.columns

			# set dtype of each header
			# todo - set dtype based on assignment
			headersDf = pd.DataFrame({
			 'name': pd.Series(dtype='str'),
			 'dtype': pd.Series(dtype='str'),
			 'alias': pd.Series(dtype='str'),
			 'editable': pd.Series(dtype='str')
			})

			# set header edit column
			for idx, x in enumerate(headers):

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

				#headersDf = pd.concat([headersDf, headerRowDict], ignore_index=True)
				headersDf = headersDf.append(headerRowDict, ignore_index=True)

		# --- write table

			# write new df to file
			self.writeTableDftoFile(filename,dataDf,headersDf)

		# --- update datasets
			
			# update datesets file
			with pd.ExcelWriter(f'datasets.xlsx') as writer:
				self.datasetsDf.set_index('ID').to_excel(writer, sheet_name='data')
				self.headersDf.set_index('name').to_excel(writer, sheet_name='headers')

		## END method ----------------------

	
	def renameDataset(self):
		print('\n')
		print('renameDataset()')
		print('---------')

	## END method ----------------------

	
	def deleteDataset(self):
		print('\n')
		print('deleteDataset()')
		print('---------')

		# --- show dataset options
		
		# print options
		for index, row in self.datasetsDf.iterrows():
			print(f'{index}: {row["name"]}')

		# --- remove table files
			
		# get index input
		prompt = f'Index to delete: '
		indexSelection = int(input(prompt))

		# remove file if exists
		source = self.datasetsDf.loc[indexSelection, 'source']
		filename = f'datasets/{source}'
		#print(filename)

		# check exists and remove files
		if os.path.exists(filename):
			os.remove(filename)
		else:
			print("The file does not exist")

		# remove from dataset
		self.datasetsDf = self.datasetsDf.drop(indexSelection)
		#print(self.datasetsDf.head())

		# --- ???
		
		# reindex
		self.datasetsDf = self.datasetsDf.reset_index(drop=True)
		#print(self.datasetsDf.head())

		
		# --- update dataset
		
		# safe dataset.xlsx
		with pd.ExcelWriter(f'datasets.xlsx') as writer:
			self.datasetsDf.set_index('ID').to_excel(writer, sheet_name='data')
			self.headersDf.set_index('name').to_excel(writer, sheet_name='headers')

	## END method ----------------------



	
	def runStocksApp(self):
		print('\n')
		print('deleteDataset()')
		print('---------')

		# --- select table

		# build filename
		index = self.datasetsDf[self.datasetsDf['name'] == 'stocks'].index
		self.selectedDatasetIndex = index[0]

		filename = self.datasetsDf.loc[index[0], 'source']
		print(filename)
		
		location = f'datasets/{filename}'
		print(location)
		
		# read to dataframe using helper functions
		self.tableDf = pd.DataFrame(self.readDataToDf(location))
		df = self.tableDf

		self.tableHeaderDf = pd.DataFrame(self.readHeadersToDf(location))
		headersDf = self.tableHeaderDf
		
		# --- build select options

		features = ['snippet','viewStocks','addStock']

		for idx, x in enumerate(features):
			print(f'{idx}: {x}')

		# --- select options
			
		messagePrompt = f'select feature: '
		index = int(input(messagePrompt))
		print(f'------')

		# --- filter methods
		
		if index == 0:
			print('--- snippet()')
			print('------')

			# df['date'] = pd.to_datetime(df['date'])
			# df['consumption'] = np.where(df['consumption'].isnull(), '0', df['consumption'])

			
			# df['date'] = pd.to_datetime(df['date'])
			# df = df.sort_values(by='date', ascending=True)

			# print('------')

			# headersArray = [
			#  'date', 'excercise', 'consumption', 'fat'
			# ]
			# print(tabulate(df[headersArray], headersArray, tablefmt='psql'))

			# # write new df to file
			# self.writeTableDftoFile(filename,df,headersDf)
			
		elif index == 1:
			print('--- viewStocks()')
			print('------')

			#print(df.info())
			# df['date'] = pd.to_datetime(df['date'])
			# df = df.sort_values(by='date', ascending=True)

			print('------')

			headersArray = [
			 "symbol", "qty"
			]
			
			# get table view headers
			#headersArray = self.getTableDefaultHeaders()
		
			print(tabulate(df[headersArray], headersArray, tablefmt='psql'))
			
		elif index == 2:
			print('--- addStock()')
			print('------')

			requiredColumn = 'symbol'

			
			messagePrompt = f'Name symbol: '
			resDict = processUserInput(messagePrompt)
			
			if resDict['valid']:
				value = str(resDict['value'])
			
			rowDict = {
			 "ID": uuid.uuid4(),
			 "created": date.today().strftime("%m/%d/%Y"),
			 "modified": "",
			 "symbol": value
			}
			
			print(rowDict)

			rowDf = pd.DataFrame(rowDict, index=[0])

			self.tableDf = pd.concat([df, rowDf], ignore_index=True)
			print(self.tableDf)

		else:
			print("--- try again")

	## END method ----------------------


	

	
	def runDonationApp(self):
		print('\n|\n|\n|')
		print('runDonationApp()')

		# build filename
		index = self.datasetsDf[self.datasetsDf['name'] == 'donations'].index
		self.selectedDatasetIndex = index[0]

		filename = self.datasetsDf.loc[index[0], 'source']
		print(filename)
		
		location = f'datasets/{filename}'
		print(location)
		
		# read to dataframe using helper functions
		self.tableDf = pd.DataFrame(self.readDataToDf(location))
		df = self.tableDf

		self.tableHeaderDf = pd.DataFrame(self.readHeadersToDf(location))
		headersDf = self.tableHeaderDf
		

		features = ['snippet','getTotal']

		for idx, x in enumerate(features):
			print(f'{idx}: {x}')

		messagePrompt = f'select feature: '
		index = int(input(messagePrompt))
		print(f'------')

		
		if index == 0:
			print('--- snippet()')
			print('------')

			# df['date'] = pd.to_datetime(df['date'])
			# df['consumption'] = np.where(df['consumption'].isnull(), '0', df['consumption'])

			
			# df['date'] = pd.to_datetime(df['date'])
			# df = df.sort_values(by='date', ascending=True)

			# print('------')

			# headersArray = [
			#  'date', 'excercise', 'consumption', 'fat'
			# ]
			# print(tabulate(df[headersArray], headersArray, tablefmt='psql'))

			# # write new df to file
			# self.writeTableDftoFile(filename,df,headersDf)
			
		elif index == 1:
			print('--- getTotal()')
			print('------')

			# #print(df.info())
			# df['date'] = pd.to_datetime(df['date'])
			# df = df.sort_values(by='date', ascending=True)

			# print('------')

			# # headersArray = [
			# #  "date", "excercise", "consumption", "fat"
			# # ]
			
			# # get table view headers
			# headersArray = self.getTableDefaultHeaders()
		
			# print(tabulate(df[headersArray], headersArray, tablefmt='psql'))
			

		else:
			print("--- try again")

	## END method ----------------------


	
	def runBodyFatApp(self):
		print('\n|\n|\n|')
		print('runBodyFatApp()')

		# get source from name in datasets list

		# build filename
		index = self.datasetsDf[self.datasetsDf['name'] == 'calories'].index
		self.selectedDatasetIndex = index[0]
		#print(index[0])

		
		filename = self.datasetsDf.loc[index[0], 'source']
		print(filename)
		
		location = f'datasets/{filename}'
		print(location)
		
		# read to dataframe using helper functions
		self.tableDf = pd.DataFrame(self.readDataToDf(location))
		df = self.tableDf

		self.tableHeaderDf = pd.DataFrame(self.readHeadersToDf(location))
		headersDf = self.tableHeaderDf
		

		features = ['snippet','viewCalories','reportProgress','updateDay']

		for idx, x in enumerate(features):
			print(f'{idx}: {x}')

		messagePrompt = f'select feature: '
		index = int(input(messagePrompt))
		print(f'------')

		
		if index == 0:
			print('--- snippet()')
			print('------')

			df['date'] = pd.to_datetime(df['date'])
			df['consumption'] = np.where(df['consumption'].isnull(), '0', df['consumption'])

			
			df['date'] = pd.to_datetime(df['date'])
			df = df.sort_values(by='date', ascending=True)

			print('------')

			headersArray = [
			 'date', 'excercise', 'consumption', 'fat'
			]
			print(tabulate(df[headersArray], headersArray, tablefmt='psql'))

			# write new df to file
			self.writeTableDftoFile(filename,df,headersDf)
			
		elif index == 1:
			print('--- viewCalories()')
			print('------')

			# for index, row in df.iterrows():
			# 	print(f'{index}: {row["Amount"]} - {row["Description"]} {row["Category"]}')

			#print(df.info())
			df['date'] = pd.to_datetime(df['date'])
			df = df.sort_values(by='date', ascending=True)

			print('------')

			# headersArray = [
			#  "date", "excercise", "consumption", "fat"
			# ]
			
			# get table view headers
			headersArray = self.getTableDefaultHeaders()
		
			print(tabulate(df[headersArray], headersArray, tablefmt='psql'))
			

		elif index == 2:
			print('--- reportProgress()')
			print('------')

			# setup calcs
			actual = 35000
			df['actual'] = 0
			
			for index, row in df.iterrows():
				#print(f'{index}: {row["excercise"]}')

				# calculate actual
				ex = int(row["excercise"])
				con = int(row["consumption"])
				actual = actual + ex + con
				#print(f'actual: {actual}')

				# insert actual value into df
				df['actual'][index] = actual

			headersArray = [
			 "date", "excercise", "consumption", "fat", "actual"
			]
			print(tabulate(df[headersArray], headersArray, tablefmt='psql'))

		elif index == 3:
			print('--- updateDay()')

			df['date'] = pd.to_datetime(df['date'])
			df = df.sort_values(by='date', ascending=True)

			headersArray = [
			 "date", "excercise", "consumption", "fat"
			]
			print(tabulate(df[headersArray], headersArray, tablefmt='psql'))
			
			# select index
			messagePrompt = f'select record: '
			recordIndex = int(input(messagePrompt))

			print(df.loc[recordIndex])

			# type of input
			actionOptions = ['excercise', 'consumption']

			for idx, x in enumerate(actionOptions):
				print(f'{idx}: {x}')

			messagePrompt = f'select Expense type: '
			actionIndex = int(input(messagePrompt))

			messagePrompt = f'enter value: '
			typeValue = input(messagePrompt)
			
			newValue = ''

			if actionIndex == 0:
				print('excercise')
				df.loc[recordIndex, 'excercise'] = typeValue

			else:
				print('consumption')
				df.loc[recordIndex, 'consumption'] = typeValue
				
			# 
			df.loc[recordIndex,
			                 'modified'] = date.today().strftime("%m/%d/%Y")
			print(df.loc[recordIndex])

			# write new df to file
			self.writeTableDftoFile(filename,df,headersDf)

		else:
			print("--- try again")

	## END method ----------------------



	
			
	def runTransactionsApplication(self):
		print('\n|\n|\n|')
		print('runTransactionsApplication()')

		# get source from name in datasets list

		# build filename
		#print(self.datasetsDf[self.datasetsDf['name'] == 'transactions'])
		index = self.datasetsDf[self.datasetsDf['name'] == 'transactions'].index
		self.selectedDatasetIndex = index[0]
		#print(index[0])
		
		filename = self.datasetsDf.loc[index[0], 'source']
		print(filename)
		
		location = f'datasets/{filename}'
		#print(location)
		
		# read to dataframe using helper functions
		self.tableDf = pd.DataFrame(self.readDataToDf(location))
		
		df = self.tableDf

		# Convert datetime 
		df['Transaction Date']= pd.to_datetime(df['Transaction Date'])

		self.tableHeaderDf = pd.DataFrame(self.readHeadersToDf(location))
		headersDf = self.tableHeaderDf
		
		# df = pd.DataFrame(self.readDataToDf(location))
		# headersDf = pd.DataFrame(self.readHeadersToDf(location))
		#print(df.info())

		

		
		#settings = self.settingsDict['transactions']['settings']['dateFilter']
		
		# check if setting exists
		if len(self.settingsDict) == 0:

			monthTimeDate = date.today().strftime("%Y-%m")
			print(f'Default Filter Month: {monthTimeDate}')
		
			settingsDict = self.settingsDict
			setting = {"dateFilter": ''}
			settings = {"settings": setting}
			settingsDict['transactions'] = settings
			print(settingsDict)
			self.settingsDict = settingsDict
			print(self.settingsDict['transactions']['settings']['dateFilter'])
		else: 
			print('settings not empty')
			print(self.settingsDict)

		
		
	

		# viewTransactions, SumbyType, ReviewItem, SumTotalByCard 
		#features = ['viewTrans', 'sumTotal', 'SumTotalByCard', 'filterDateRange', 'reviewItem', 'reviewItem']

		# todo - make a dictionary of features, actions, and settings
		# thisdict = {
  # 			"viewTrans": "Ford",
		#   	"sumTotal": "Mustang",
		#   	"SumTotalByCard": "Mustang",
		#   	"actions": "reviewItem",
		#   	"settings": "filterDateRange"
		# }

		features = ['sumGroup', 'updateStatus', 'sumTotal', 'viewTrans', 'reviewItem', 'filterDateRange','creditImportMacroAmazon','creditImportMacroSapphire','mechanicsImportMacro']

		for idx, x in enumerate(features):
			print(f'{idx}: {x}')

		messagePrompt = f'select feature: '
		index = int(input(messagePrompt))
		print(f'------')

		
		if index == 0:
			print('sumGroup()')
			print('------')

			# for idx, x in enumerate(df.columns):
			# 	print(f'{idx}: {x}')

			# messagePrompt = f'select column: '
			# index = int(input(messagePrompt))

			#groupDf = df.groupby(df.columns[index]).sum()
			#column = df.columns[index]
			#df = df[df['Reviewed']]
			#df = df.dropna(subset=['Reviewed'])
			df = df.loc[df['Reviewed'] == 1]

			# filter by selected MONTH
			filterDate = self.settingsDict['transactions']['settings']['dateFilter']
			#print(bool(filterDate))
			
			if bool(filterDate):
				df = df[df['Transaction Date'].dt.strftime('%Y-%m') == filterDate]
				print(f'Filter Month: {filterDate}')
			else:
				print('no date filter')

			print('------')

			
			
			groupDf = df.groupby('Expense')['Amount'].sum()
			print(groupDf)
			
			total = df['Amount'].sum()
			print(f'Total: {total}')

		elif index == 1:
			print('--- updateStatus()')
			#print(f'--- {feature[index]}')

			# for idx, x in enumerate(df.columns):
			# 	print(f'{idx}: {x}')

			# messagePrompt = f'select column: '
			# tableHeaderValue = int(input(messagePrompt))
			# columnName = df.columns[tableHeaderValue]

			# for index, row in df.iterrows():
			# 	print(f'{index}: {row}')

			# messagePrompt = f'select row: '
			# tableIndexSelection = int(input(messagePrompt))

			# picklist = [
			#  'Automotive', 'Bills & Utilities', 'Entertainment', 'Fees & Adjustments',
			#  'Food & Drink', 'gas'
			# ]

			# for idx, x in enumerate(picklist):
			# 	print(f'{idx}: {x}')

			# messagePrompt = f'picklist: '
			# pickListIndex = int(input(messagePrompt))
			# picklistValue = picklist[pickListIndex]
			# print(f'picklistValue: {picklistValue}')

			# # set index
			# df.loc[tableIndexSelection, columnName] = picklistValue
			# df.loc[tableIndexSelection,
			#                  'modified'] = date.today().strftime("%m/%d/%Y")
			# print(df)

			# # make change and set modified date
			# # source = self.datasetsDf.loc[self.selectedDatasetIndex, 'source']
			# # location = f'datasets/{source}'
			# # print(f'location: {location}')

			# print(df.loc[tableIndexSelection])

			# # dataDf = df.set_index('ID')
			# # headersDf = headersDf.set_index('name')

			# # write new df to file
			# self.writeTableDftoFile(filename,dataDf,headersDf)

		elif index == 2:
			print('--- sumTotal')
			#print(f'--- {feature[index]}')

			#df = self.tableDf
			#newDf = pd.DataFrame()

			

			
			#df = df[df['Reviewed'] == True]
			#df['Reviewed']
			#df = df[df['Reviewed'] == True]
			df = df.loc[df['Reviewed'] == 1]


			# filter by selected MONTH
			filterDate = self.settingsDict['transactions']['settings']['dateFilter']
			#print(bool(filterDate))
			
			if bool(filterDate):
				df = df[df['Transaction Date'].dt.strftime('%Y-%m') == filterDate]
				print(f'Filter Month: {filterDate}')
			else:
				print('no date filter')

			print('------')
			
			
			groupDf = df.groupby('Card')['Amount'].sum()
			print(groupDf)

		elif index == 3:
			print('--- viewTrans')
			#print(f'--- {feature[index]}')

			# for index, row in df.iterrows():
			# 	print(f'{index}: {row["Amount"]} - {row["Description"]} {row["Category"]}')

			#print(df.info())
			df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
			df = df.sort_values(by='Transaction Date', ascending=True)

			# filter by selected MONTH
			filterDate = self.settingsDict['transactions']['settings']['dateFilter']
			#print(bool(filterDate))
			
			if bool(filterDate):
				df = df[df['Transaction Date'].dt.strftime('%Y-%m') == filterDate]
				print(f'Filter Month: {filterDate}')
			else:
				print('no date filter')

			print('------')

			# headersArray = [
			#  'Amount', 'Description', 'Expense', 'Transaction Date', 'Reviewed', 'Card'
			# ]
			headersArray = self.getTableDefaultHeaders()
			
			print(tabulate(df[headersArray], headersArray, tablefmt='psql'))
			#print(df.info())

		elif index == 4:
			print('--- reviewItem')
			# reviewItem
			
			# loop through records not reviewed,
			#print(f'--- {feature[index]}')

			df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
			df = df.sort_values(by='Transaction Date', ascending=True)

			
			# filter by selected MONTH
			filterDate = self.settingsDict['transactions']['settings']['dateFilter']
			#print(bool(filterDate))
			
			if bool(filterDate):
				reportDf = df[df['Transaction Date'].dt.strftime('%Y-%m') == filterDate]
				print(f'Filter Month: {filterDate}')
			else:
				reportDf = df
				print('no date filter')

			print('------')

			

			headersArray = [
			 "Amount", "Description", "Expense", "Transaction Date",
			 "Reviewed"
			]
			print(tabulate(reportDf[headersArray], headersArray, tablefmt='psql'))
			#print(df.info())

			# select index
			messagePrompt = f'select record: '
			recordIndex = int(input(messagePrompt))

			print(df.loc[recordIndex])

			#
			expenseUniques = pd.Series(df['Expense'].unique())
			#print(expenseUniques)
			expenseTypes = pd.Series([
			 'Transportation', 'Supplies', 'clothes', 'entertainment', 'eating out',
			 'Gas', 'Groceries'
			])
			#print(expenseTypes)

			expenseList = expenseUniques.append(expenseTypes)
			#print(expenseList)

			expenseList = expenseList.drop_duplicates()
			expenseList = expenseList.dropna()
			expenseList.index = range(0, len(expenseList))
			#print(expenseList)

			for idx, x in enumerate(expenseList):
				print(f'{idx}: {x}')

			print('----- select input type')

			# type of input
			actionOptions = ['input new', 'select type']

			for idx, x in enumerate(actionOptions):
				print(f'{idx}: {x}')

			messagePrompt = f'select Expense type: '
			actionIndex = int(input(messagePrompt))

			newValue = ''

			if actionIndex == 0:
				messagePrompt = f'enter type: '
				typeValue = input(messagePrompt)
				print(typeValue)
				newValue = typeValue

			else:

				messagePrompt = f'select Expense id: '
				expenseIndex = int(input(messagePrompt))
				newValue = expenseList[expenseIndex]

			print(f'newValue: {newValue}')

			# update Expense Type
			# set as reviewed
			df.loc[recordIndex, 'Expense'] = newValue
			df.loc[recordIndex,
			                 'modified'] = date.today().strftime("%m/%d/%Y")
			df.loc[recordIndex, 'Reviewed'] = True
			print(df.loc[recordIndex])

			# make change and set modified date
			#source = self.datasetsDf.loc[self.selectedDatasetIndex, 'source']
			# location = f'datasets/{filename}'
			# print(f'location: {location}')


			# write new df to file
			self.writeTableDftoFile(filename,df,headersDf)

			
			# # update dataset
			# with pd.ExcelWriter(location) as writer:
			# 	self.tableDf.set_index('ID').to_excel(writer, sheet_name='data')
			# 	self.tableHeaderDf.set_index('name').to_excel(writer, sheet_name='headers')

		elif index == 5:
			# filterDateRange
			print('--- filterDateRange')

			settingsDict = self.settingsDict
			print(settingsDict)
			
			messagePrompt = f'Enter filter (2022-XX): '
			value = input(messagePrompt)
			
			settingsDict['transactions']['settings']['dateFilter'] = value
			print(settingsDict)
			self.settingsDict = settingsDict
			
		elif index == 6:
			# filterDateRange
			print('--- creditImportMacroAmazon')

			
			testFilename = 'Chase3439.csv'
			extension = testFilename.split(".")
			print(extension)

			location = f'imports/{testFilename}'
			print(f'location: {location}')

			# load by extension type
			self.importDf = pd.read_csv(location)

			# import file
			df = self.importDf
	
			# drop memo
			print('drop')
			df.drop('Memo', axis=1, inplace=True)
			
			print('rename')
			df.rename(columns={'Type': 'Kind'}, inplace=True)
	
			# add reviewed with default false
			print('add')
			df['Imported'] = date.today().strftime("%m/%d/%Y")
			df['Card'] = "1885"
			df['Reviewed'] = "0"
			df['Expense'] = ""
	
			print(df)
			print(df.info())
	
			self.importDf = df

			# trigger import
			self.performImport()
		
		elif index == 7:
			# filterDateRange
			print('--- creditImportMacroSapphire')

			testFilename = 'Chase9901.csv'
			extension = testFilename.split(".")
			print(extension)

			location = f'imports/{testFilename}'
			print(f'location: {location}')

			# load by extension type
			self.importDf = pd.read_csv(location)

			# import file
			df = self.importDf
	
			# drop memo
			print('drop')
			df.drop('Memo', axis=1, inplace=True)
			
			print('rename')
			df.rename(columns={'Type': 'Kind'}, inplace=True)
	
			# add reviewed with default false
			print('add')
			df['Imported'] = date.today().strftime("%m/%d/%Y")
			df['Card'] = "Sapphire"
			df['Reviewed'] = "0"
			df['Expense'] = ""
	
			print(df)
			print(df.info())
	
			self.importDf = df

			# trigger import
			self.performImport()

		elif index == 8:
			# filterDateRange
			print('--- mechanicsImportMacro')

			testFilename = 'Export.csv'
			extension = testFilename.split(".")
			print(extension)

			location = f'imports/{testFilename}'
			print(f'location: {location}')
			
			with open(location, "r+") as f:
				lines = f.readlines()
				f.seek(0)
				for number, line in enumerate(lines):
					print(f'{number}: {line}')
					if int(number) > 2:
						print(f'{number}: {line}')
						f.write(line)
				f.truncate()
				
			# load by extension type
			self.importDf = pd.read_csv(location)

			# import file
			df = self.importDf
			print(df.head())
			print(df.info())

			# combine columns
			cols = ['Amount Debit', 'Amount Credit']
			df['Amount'] = df[cols].sum(1)

			print('rename')
			df.rename(columns={'Date': 'Transaction Date'}, inplace=True)
			#df.rename(columns={'Amount Debit': 'Amount'}, inplace=True)
	
			# add reviewed with default false
			print('add')
			df['Imported'] = date.today().strftime("%m/%d/%Y")
			df['Card'] = "Rabo"
			df['Reviewed'] = "0"
			df['Expense'] = ""

			print(df.info())

			# drop memo
			print('drop')
			df.drop(['Transaction Number', 'Memo', 'Balance', 'Check Number', 'Amount Debit', 'Amount Credit'], axis=1, inplace=True)
	
			print(df)
			print(df.info())
	
			self.importDf = df

			# trigger import
			self.performImport()
		
		else:
			print("--- try again")

		#print(getattr(p1, option, lambda: p1.default)())

	## END method ----------------------


	



		
	# -------------
	# table CRUD
	# -------------

	def printTable(self):
		print('\n|\n|\n|')
		print('printTable()')
		
		print(self.tableDf)
		print(self.tableDf.info())

		# todo - check dataset exists, get total & report

		## END method ----------------------


	def addTableColumn(self):
		print('\n|\n|\n|')
		print('addTableColumn()')

		# --- get input
		
		df = self.tableDf

		#
		messagePrompt = f'column name: '
		newColumn = input(messagePrompt)

		#
		messagePrompt = f'default value if any; "today" for todays date: '
		defaultValue = input(messagePrompt)

		# --- add column
		
		if defaultValue == 'today':
			df[newColumn] = date.today().strftime("%m/%d/%Y")
		else:
			df[newColumn] = defaultValue

		print(df)
		print(df.info())

		# --- build headers
		
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

			tempTableHeaderDf = pd.concat(
			 [tempTableHeaderDf,
			  pd.DataFrame(headerRowDict, index=[0])],
			 ignore_index=True)

		self.tableHeaderDf = tempTableHeaderDf
		print(self.tableHeaderDf)

		# --- update table
		
		# get table location
		source = self.datasetsDf.loc[self.selectedDatasetIndex, 'source']
		print(f'location: {source}')

		dataDf = self.tableDf.set_index('ID')
		headersDf = self.tableHeaderDf.set_index('name')

		with pd.ExcelWriter(f'datasets/{source}') as writer:
			dataDf.to_excel(writer, sheet_name='data')
			headersDf.to_excel(writer, sheet_name='headers')

		## END method ----------------------

	
	def dropTableColumn(self):
		print('\n|\n|\n|')
		print('dropTableColumn()')

		df = self.tableDf

		# --- show column options
		
		for idx, x in enumerate(df.columns):
			print(f'{idx}: {x}')

		# --- get input
			
		#
		messagePrompt = f'column to drop: '
		index = int(input(messagePrompt))

		# --- drop column
		
		df.drop(df.columns[index], axis=1, inplace=True)
		#df.drop(colName, axis=1, inplace=True)

		print(df.head())
		print(df.info())

		# --- build headers
		
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

			tempTableHeaderDf = pd.concat(
			 [tempTableHeaderDf,
			  pd.DataFrame(headerRowDict, index=[0])],
			 ignore_index=True)

		self.tableHeaderDf = tempTableHeaderDf
		print(self.tableHeaderDf)

		# --- update table
		
		# get table location
		source = self.datasetsDf.loc[self.selectedDatasetIndex, 'source']
		print(f'location: {source}')

		dataDf = self.tableDf.set_index('ID')
		headersDf = self.tableHeaderDf.set_index('name')

		with pd.ExcelWriter(f'datasets/{source}') as writer:
			dataDf.to_excel(writer, sheet_name='data')
			headersDf.to_excel(writer, sheet_name='headers')

		# todo - create new file, archive old one in folder by table name; do same for imports

		## END method ----------------------

	
	def readRecord(self):

		# print table name
		name = self.datasetsDf.loc[self.selectedDatasetIndex, 'name']
		print(f'Table: {name}')

		# --- show table
		
		# select record
		for index, row in self.tableDf.iterrows():
			print(f'{index}: {row}')

		# --- get input
			
		# get index input
		prompt = f'Index to read: '
		indexSelection = int(input(prompt))

		# print table name
		# name = self.tableDf.loc[indexSelection, 'name']
		# print(f'Record: {name}')

		# --- set selection
		self.selectedRecordIndex = indexSelection

		# --- loop fields
		
		for index, row in self.tableHeaderDf.iterrows():
			print(f'{row["name"]}: {self.tableDf.loc[indexSelection, row["name"]]}')
			#print(f'{row}: {self.tableDf.loc[indexSelection, row["name"]]}')

		# get table meta, loop through & print each attribute
		#print(self.tableHeaderDf)

		## END method ----------------------


	def deleteRecord(self):
		print('\n|\n|\n|')
		print('deleteRecord()')

		df = self.tableDf

		# print options
		# for index, row in self.tableDf.iterrows():
		# 	print(f'{index}: {row}')

		# --- apply date filter
		
		df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
		df = df.sort_values(by='Transaction Date', ascending=True)

		headersArray = [
		 "Amount", "Description", "Expense", "Transaction Date",
		 "Reviewed"
		]
		
		# --- show options
		
		#print(tabulate(df[headersArray], headersArray, tablefmt='psql'))
		self.printFormattedTable(df,headersArray)
		
		# --- get input
		
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

		# --- drop record
		
		# remove from dataset
		df = df.drop(indexSelection)
		print(df.head())

		# reindex
		df = df.reset_index(drop=True)
		print(df.head())

		self.tableDf = df

		# --- update table
		
		# get table location
		source = self.datasetsDf.loc[self.selectedDatasetIndex, 'source']
		location = f'datasets/{source}'
		print(f'location: {location}')

		#safe dataset.xlsx
		with pd.ExcelWriter(location) as writer:
			self.tableDf.set_index('ID').to_excel(writer, sheet_name='data')
			self.tableHeaderDf.set_index('name').to_excel(writer, sheet_name='headers')

		## END method ----------------------












	# -------------
	# table CRUD - NOT USED
	# -------------

	
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

		df.drop(df.columns[index], axis=1, inplace=True)
		#df.drop(colName, axis=1, inplace=True)

		print(df)
		print(df.info())

		self.importDf = df

		## END method ----------------------

	
	def performImport(self):
		print('\n|\n|\n|')
		print('performImport()')

		# --- get import df
		
		df = self.importDf

		importColumns = df.columns

		# select record
		newDf = pd.DataFrame()
		newDf = self.tableDf

		# --- loop df and build records
		
		for index, row in df.iterrows():
			print(f'{index}: {row}')

			rowDict = dict()

			for index, headRow in self.tableHeaderDf.iterrows():
				print(f'{index}: {headRow["name"]}')
				#rowDict[x] = df.loc[index,x]
				if headRow["name"] == 'ID':
					rowDict[headRow["name"]] = uuid.uuid4()
				elif headRow["name"] == 'created':
					rowDict[headRow["name"]] = date.today().strftime("%m/%d/%Y")
				else:
					rowDict[headRow["name"]] = ''

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

			newDf = pd.concat([newDf, rowDf], ignore_index=True)

		self.tableDf = newDf

		# --- build headers
		
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

			headerRowDict = {"name": x, "dtype": 'str', "alias": x, "editable": 'True'}

			tempTableHeaderDf = tempTableHeaderDf.append(headerRowDict,
			                                             ignore_index=True)

		self.tableHeaderDf = tempTableHeaderDf
		print(self.tableHeaderDf)
		
		print(self.tableDf)

		# --- create tables
		
		# safe dataset
		self.tableDf = self.tableDf.set_index('ID')
		self.tableHeaderDf = self.tableHeaderDf.set_index('name')

		print(self.selectedDatasetIndex)
		source = self.datasetsDf.loc[self.selectedDatasetIndex, 'name']
		filename = f'{source}_{date.today().strftime("%m%d%Y")}.xlsx'
		print(filename)

		with pd.ExcelWriter(f'datasets/{filename}') as writer:
			self.tableDf.to_excel(writer, sheet_name='data')
			self.tableHeaderDf.to_excel(writer, sheet_name='headers')

		# # update datesets

		self.datasetsDf.loc[self.selectedDatasetIndex, 'source'] = filename
		#print(self.datasetsDf.loc[self.selectedDatasetIndex,:])

		# --- update datasets
		
		with pd.ExcelWriter(f'datasets.xlsx') as writer:
			self.datasetsDf.set_index('ID').to_excel(writer, sheet_name='data')
			self.headersDf.set_index('name').to_excel(writer, sheet_name='headers')

		# return to main menu
		self.promptOptions = self.datasetsMethods

		## END method ----------------------


	def renameColumn(self):
		print('\n|\n|\n|')
		print('renameColumn()')

		df = self.tableDf

		columnsArray = pd.array(df.columns)

		for idx, x in enumerate(df.columns):
			print(f'{idx}: {x}')

		#
		messagePrompt = f'column to rename: '
		index = int(input(messagePrompt))

		messagePrompt = f'column name: '
		nameValue = input(messagePrompt)
		print(columnsArray[index])

		# rename column
		df.rename(columns={columnsArray[index]: nameValue}, inplace=True)
		print(df.columns)

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

			tempTableHeaderDf = pd.concat(
			 [tempTableHeaderDf,
			  pd.DataFrame(headerRowDict, index=[0])],
			 ignore_index=True)

		self.tableHeaderDf = tempTableHeaderDf
		print(self.tableHeaderDf)

		# get table location
		source = self.datasetsDf.loc[self.selectedDatasetIndex, 'source']
		print(f'location: {source}')

		dataDf = self.tableDf.set_index('ID')
		headersDf = self.tableHeaderDf.set_index('name')

		with pd.ExcelWriter(f'datasets/{source}') as writer:
			dataDf.to_excel(writer, sheet_name='data')
			headersDf.to_excel(writer, sheet_name='headers')

		# todo - create new file, archive old one in folder by table name; do same for imports

		## END method ----------------------

	def backToDatasets(self):
		print('\n|\n|\n|')
		print('backToDatasets()')

		self.promptOptions = self.datasetsMethods
		## END method ----------------------

	def f(d, a, b):
		d.ix[d[a] == b, 'data1'].sum()





		
	# -------------
	# helper functions - NOT USED
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

		optionsList = p1.getPromptOptions()
		numMethods = int(len(optionsList))
		#print(f'numMethods: {numMethods}')
		print(p1.getNavigation())
		print(f'-----------')
		print(f'Menu')

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
