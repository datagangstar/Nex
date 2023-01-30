import pandas as pd
import re
import Nex
from tabulate import tabulate # printing tables
import json
import uuid
from datetime import date
import os


from applications import Donations
from applications import Finances
from applications import Taxes



# create class dynamically
# https://www.geeksforgeeks.org/create-classes-dynamically-in-python/

#core = type('', (), {})()
#apps = type('', (), {})()

class UI:

	def __init__(self):
		print('__init__UI()')

		self.mainMenu = pd.Series([
			'Datasets',
			'Market', 
			'Applications',
			'Metrics',
			'Components',
			'Mods',
			'Settings'
		])

		# set root prompt options
		self._promptOptions = self.mainMenu

		# set empty display list
		self._displayList = ''

		# set table name
		self._tableName = ''
		
		# set table name
		self._appName = ''
		self._appObject = type('', (), {})()
		
		# set record name
		self._recordName = ''
		
		# use property function
		# https://www.geeksforgeeks.org/getter-and-setter-in-python/
		
		self.menuSelection = ''

		# init Nex - TURN OFF WHEN DONE CONVERTING
		#nex = Nex.Nex()
		
		# init Core
		core = Core()

		# init Apps
		apps = Apps()
		
		# init Apps
		metrics = Metrics()

		while True:
		
			# get list of prompt options
			optionsList = self.promptOptions
			
			# product options list
			self.buildOptionsList(optionsList)
			
			# list length to int
			numMethods = int(len(optionsList))
		
			# get option selection
			inputMessagePrompt = 'Select option:'
			resDict = self.processUserInput(inputMessagePrompt)
			
			if resDict['valid']:
				optionNumber = int(resDict['value'])

				if (optionNumber <= numMethods):
					objAttribute = optionsList.get(optionNumber, '')
					print(f'Selected option: {objAttribute}')
					print(f'----------------------')

					
					if self.menuSelection == '': 
						#print('do menu')
						self.menuSelection = objAttribute
						
						if optionNumber == 0:
							print('--- Datasets')
							# get datasets list

							self.displayList = core.getDatasetDf()
							
							# get datasets list options
							self.promptOptions = core.getDatasetMethods()
							
						elif optionNumber == 1:
							print('--- Market')
							# get datasets list options
							
						elif optionNumber == 2:
							print('--- Applications')
							# get datasets list options
							self.displayList = apps.getAppsList()
							
							# get datasets list options
							self.promptOptions = apps.getAppMethods()
							
						elif optionNumber == 3:
							print('--- Metrics')
							# get datasets list options
							self.displayList = metrics.getAppsList()
							
							# get datasets list options
							self.promptOptions = metrics.getAppMethods()
							
						elif optionNumber == 4:
							print('--- Components')
							# get datasets list options
							
						elif optionNumber == 5:
							print('--- Mods')
							# get datasets list options
							
						elif optionNumber == 6:
							print('--- Settings')
							# get datasets list options
							
						else: 
							print('invalid selection')
	
					else: 
						print('\n')
						print('run class methods')
						
						if self.menuSelection == 'Datasets':
							print('--- Datasets')

							# call Core Method
							#print(getattr(nex, objAttribute, lambda: nex.default)())
							print(getattr(core, objAttribute, lambda: core.default)())
							
						elif self.menuSelection == 'Market':
							print('--- Market')
							# get datasets list options
							
						elif self.menuSelection == 'Applications':
							print(f'--- Applications:{objAttribute}()')
							# get applications list options


							if self.appName == '':
								print('no app selected')
								getattr(apps, objAttribute, lambda: apps.default)(self)
							else: 
								print(f'app selected: {self.appName}.{objAttribute}()')
								# if app is selected, 
									# get class menu and display list
									# send selection to application
								#classStr = self.appName
								#classInstance = eval(classStr)()
								#klass = type(classInstance)
								classObj = self.appObject
								#print(classObj)	
								
								getattr(classObj, objAttribute, lambda: classObj.default)()
							

								# send selected method
								
						elif self.menuSelection == 'Metrics':
							print('--- Metrics')
							
							# get datasets list options
							getattr(metrics, objAttribute, lambda: metrics.default)(core)
							
						elif self.menuSelection == 'Components':
							print('--- Components')
							# get datasets list options
							
						elif self.menuSelection == 'Mods':
							print('--- Mods')
							# get datasets list options
							
						elif self.menuSelection == 'Settings':
							print('--- Settings')
							# get datasets list options
							
						else: 
							print('invalid selection')

	## END INIT method ----------------------			

							
	# getter ------
	@property
	def promptOptions(self):
		return self._promptOptions
	
	## END method ----------------------

	# setter
	@promptOptions.setter
	def promptOptions(self, optionsList):
		print('setPromptOptions(setPromptOptions)')
		self._promptOptions = optionsList
		
	## END method ----------------------

	# getter ------
	@property
	def displayList(self):
		return self._displayList
		
	## END method ----------------------

	# setter
	@displayList.setter
	def displayList(self, displayList):
		print('set displayList(displayList)')
		self._displayList = displayList
		
	## END method ----------------------
		
	# getter ------
	@property
	def tableName(self):
		return self._tableName
	
	## END method ----------------------

	# setter
	@tableName.setter
	def tableName(self, name):
		print(f'set tableName({name})')
		self._tableName = name
		
	## END method ----------------------
		
	# getter ------
	@property
	def appName(self):
		return self._appName
	
	## END method ----------------------

	# setter
	@appName.setter
	def appName(self, name):
		print(f'set appName({name})')
		self._appName = name
		
	## END method ----------------------

		
	# getter ------
	@property
	def appObject(self):
		return self._appObject
	
	## END method ----------------------

	# setter
	@appObject.setter
	def appObject(self, object):
		print(f'set appObject({object})')
		self._appObject = object
		
	## END method ----------------------
		
	# getter ------
	@property
	def recordName(self):
		return self._recordName
		
	## END method ----------------------

	# setter
	@recordName.setter
	def recordName(self, name):
		print('set recordName(name)')
		self._recordName = name
		
	## END method ----------------------


		
	def buildOptionsList(self, optionsList):
		print(f'buildOptionsList()')
	
		print(f'\n\n')
		print(f'----------------------')

		# build navigation & build options
		if self.menuSelection == '': 
			print(f'Menu')
		else: 
			print(f'self.menuSelection: {self.menuSelection}')
			#if not self.tableName == '': 
			print(f'self.tableName: {self.tableName}')
			print(f'self.appName: {self.appName}')

		print(f'-----------')
		
		print(self.displayList)
		
		print(f'-----------')
		
		# show options
		for idx, x in optionsList.items():
			print(f'{idx}: {x}')
	
		print(f'-----------')
		
	## END method ----------------------

	
	def processUserInput(self, message):
		print(f'processUserInput()')
	
		# set up return
		retDict = {'valid': True}
		inputValue = input(message)
		# inputValue = inputValue.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+", "")
		inputValue = re.sub('[^a-zA-Z0-9 \n\.]', '', inputValue)
	
		if inputValue == "":
			retDict['valid'] = False
		elif (inputValue == 'esc') and (self.menuSelection == ''):
			print('go back')
			retDict['valid'] = False
		else:
			# todo - check type by column name and match type then convert
			retDict['value'] = inputValue
	
		return retDict
	## END method ----------------------

		
	def printFormattedTable(self,df,headersArray):
		
		print(tabulate(df[headersArray], headersArray, tablefmt='psql'))

	## END method ----------------------
		
## END Class ======



class Core:

	def __init__(self):
		print('__init__Core()')

		self.UI = UI
		self.Components = Components

		self.datasetsMethods = pd.Series([
			'runSnippet',
			'selectDataset',
			'createDataset',
			#'deleteDataset',
			#'runStocksApp',
			#'runDonationApp',
			#'runBodyFatApp',
			#'runTransactionsApplication',
			#'runContactsApp',
			#'runObjectsApp'
		])

		self.tableMethods = pd.Series([
			#'printHeaders',
		 	'printTable',
			#'addTableColumn',
			#'renameColumn',
			#'dropTableColumn',
			'selectRecord',
			'addTableItem',
			#'linkTableItem',
			'deleteRecord',
			#'backToDatasets'
		])
		
		self.selectedDatasetIndex = ''
		self.selectedRecordIndex = ''
		self.selectedObject = {}
		
		# load datasets data & meta
		self.datasetsDf = pd.DataFrame(self.readDataToDf('datasets.xlsx'))

		self.tableDf = pd.DataFrame()
		self.tableHeaderDf = pd.DataFrame()
		
	## END INIT method ----------------------	

		
	# called externally
	def getDatasetMethods(self):
		return self.datasetsMethods

	## END method ----------------------
		
	# called externally
	def getDatasetDf(self):
		return self.datasetsDf
		
	## END method ----------------------
		
	# -------------
	# datasets init
	# -------------


	# called in init
	def readDataToDf(self, file):
		try:
			data = pd.read_excel(file, sheet_name='data')
			#headers = pd.read_excel(file, sheet_name='headers')
			#print(headers.head())
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

	
	def formatTableColumn(self,row):
		#print('\n')
		#print('formatTableColumn()')
		#print(row.dtypes)
		#print(row['name'])
		#print(row['dtype'])

		df = self.tableDf

		colName = row['name']
		dtype = row['dtype']

		# if 
		if dtype == 'datetime64':
			#print('format to datetime')
			df[colName] = pd.to_datetime(df[colName])
		elif  dtype == 'str':
			#print('format to str')
			#df[colName] = pd.to_datetime(df[colName])
			df[colName] = df[colName].astype(str)
		elif  dtype == 'int':
			#print('format to int')
			df[colName] = df[colName].astype('int')
		elif  dtype == 'number':
			#print('format to str')
			#df[colName] = pd.to_datetime(df[colName])
			#df[colName] = df[colName].astype(str)
			df[colName] = pd.to_numeric(df[colName])
		else: 
			print('do nothing')
		
		self.tableDf = df
		
	## END method ----------------------
			
	def loadTableToDf(self,tableName):
		print(f'---> loadTableToDf({tableName})')
	
		# build filename
		index = self.datasetsDf[self.datasetsDf['name'] == tableName].index
		self.selectedDatasetIndex = index[0]

		filename = self.datasetsDf.loc[index[0], 'source']
		location = f'datasets/{filename}'
		print(location)
		
		# read to dataframe using helper functions
		self.tableDf = pd.DataFrame(self.readDataToDf(location))

		self.tableHeaderDf = pd.DataFrame(self.readHeadersToDf(location))
		#print(self.tableHeaderDf)
		#headersDf = self.tableHeaderDf'

		print('set type to table df')
		headerDf = self.tableHeaderDf.copy()

		#print(self.tableDf.info())

		# format columns on load
		df1 = headerDf.apply(self.formatTableColumn, axis=1)

		#print(self.tableDf.info())
		
		#self.tableDf = df
		
		return filename,self.tableDf,self.tableHeaderDf
		
	## END method ----------------------
			
	def getTableDefaultHeaders(self):
		headerArray = []
		for index, row in self.tableHeaderDf.iterrows():
			if row["default_view"]:
				headerArray.append(row["name"])
		
		return headerArray
		
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
	def runSnippet(self):
		print('snippetTest()')

		headers = self.datasetsDf.columns
		print(headers)


	## END method ----------------------


	def selectDataset(self):
		print('selectDataset()')

		# get index input
		inputMessagePrompt = f'Select Index: '
		indexSelection = int(input(inputMessagePrompt))

		# set state
		self.selectedDatasetIndex = indexSelection

		# build location
		source = self.datasetsDf.loc[indexSelection, 'source']
		location = f'datasets/{source}'
		
		name = self.datasetsDf.loc[indexSelection, 'name']
		UI.tableName = name
		print(f'Table: {name}')
		
		# --- load selected table
		
		# read to dataframe using helper functions
		self.tableDf = pd.DataFrame(self.readDataToDf(location))
		self.tableHeaderDf = pd.DataFrame(self.readHeadersToDf(location))

		UI.displayList = self.tableDf
		
		UI.promptOptions = self.tableMethods

		# set options state
		#self.promptOptions = self.tableMethods
		
	## END method ----------------------


	def createDataset(self):
		print('\n')
		print('createDataset()')
		print('---------')

		# --- get input
		
		# todo - check if "name" already exists
		messagePrompt = f'Name Dataset: '
		resDict = UI.processUserInput(self,messagePrompt)
		
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
			print(self.datasetsDf)

			# build dataset table
			# headDict = pd.Series(['ID','created','modified','name'])
			dataDf = pd.DataFrame({
			 'ID': pd.Series(dtype='object'),
			 'created': pd.Series(dtype='datetime64[ns]'),
			 'modified': pd.Series(dtype='datetime64[ns]')
			})

			# get new df headers
			headers = dataDf.columns
			print(headers)

			# set dtype of each header
			# todo - set dtype based on assignment
			headersDf = pd.DataFrame({
			 'name': pd.Series(dtype='str'),
			 'dtype': pd.Series(dtype='str'),
			 'alias': pd.Series(dtype='str'),
			 'editable': pd.Series(dtype='str'),
			 'required': pd.Series(dtype='str'),
			 'default_view': pd.Series(dtype='str')
			})

			# set header edit column
			for idx, x in enumerate(headers):

				if x == 'ID':
					dtypeValue = 'object'
				else:
					dtypeValue = 'datetime64'

				headerRowDict = {
				 'name': x,
				 'dtype': dtypeValue,
				 'alias': x,
				 'editable': 'False',
				 'required': 'False',
				 'default_view': 'False'
				}

				#headersDf = pd.concat([headersDf, headerRowDict], ignore_index=True)
				headersDf = headersDf.append(headerRowDict, ignore_index=True)

		# --- write table
			print(headersDf)

			# write new df to file
			self.writeTableDftoFile(filename,dataDf,headersDf)

		# --- update datasets
			
			# update datesets file
			self.writeDatasetsDftoFile()

		## END method ----------------------

	def writeDatasetsDftoFile(self):
		print('\n')
		print('writeDatasetsDftoFile()')
		print('---------')

		df = self.datasetsDf

		df["created"] = pd.to_datetime(df["created"])
		df["modified"] = pd.to_datetime(df["modified"])
		
		df = self.datasetsDf.astype({
			'ID':'string',
			'created':'string',
			'modified':'string',
			'name':'string',
			'source':'string',
			'status':'string'
		})
		
		# safe dataset.xlsx
		with pd.ExcelWriter('datasets.xlsx') as writer:
			df.set_index('ID').to_excel(writer, sheet_name='data')

		df.to_json(r'datasets.json')

	## END method ----------------------

	
	def dropColumns(self,df,dropList):
		print('dropColumns()')

		for x in dropList:
			print(x)
			if x in df.columns:
				df.drop(x, axis=1, inplace=True)
	
		return df

	## END method ----------------------


	def printTable(self):
		print('\n|\n|\n|')
		print('printTable()')
		
		df = self.tableDf
		
		# df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
		# df = df.sort_values(by='Transaction Date', ascending=True)

		headersArray = self.getTableDefaultHeaders()
		print(headersArray)

		# print report talbe
		UI = self.UI
		UI.printFormattedTable(self,df,headersArray)

	## END method ----------------------
		


	# -------------
	# table CRUD
	# -------------



	def addTableItem(self):
		print('addTableItem()')
		
		print(self.tableDf)
		
		# build filename
		filename = self.datasetsDf.loc[self.selectedDatasetIndex, 'source']
		
		# get input
		df = self.createTableRow(self.tableDf,self.tableHeaderDf)

		# --- write new df to file
		self.writeTableDftoFile(filename,df,self.tableHeaderDf)
		
	## END method ----------------------


	def createTableRow(self,df,headersDf):
		print('createTableRow(df)')

		# get editable headers
		# loop through headers
		# get input by header type
		# build row dictionary
		# concat row into df
		# return df

		# --- get editable headers
		#self.printFormattedTable(df,self.getTableDefaultHeaders())
		
		# --- create default row cells
		rowDict = {
		 "ID": uuid.uuid4(),
		 "created": date.today().strftime("%m/%d/%Y"),
		 "modified": ""
		}
		
		for index, row in headersDf.iterrows():
			#print(f'{index}: {row["editable"]}')

			columnName = row["name"]
			
			if row["required"]:
				#print('get input')
				messagePrompt = f'Select "{row["name"]}":'
				inputValue = ''
				if row["dtype"] == 'str':
					#print('get str')
					inputValue = input(messagePrompt)
					print(f'------')
				elif row["dtype"] == 'int64':
					#print('get int')
					inputValue = int(input(messagePrompt))
					print(f'------')
				elif row["dtype"] == 'float64':
					#print('get float')
					inputValue = pd.to_numeric(input(messagePrompt))
					print(f'------')
				else:
					print('unknown type')

				rowDict[columnName] = inputValue

		print(rowDict)
		
		rowDf = pd.DataFrame(rowDict, index=[0])
		df = pd.concat([df, rowDf], ignore_index=True)
		
		# --- print df by defaults
		UI.printFormattedTable(self,df,self.getTableDefaultHeaders())
		
		return df

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
		self.UI.printFormattedTable(self,df,headersArray)
		
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

		
		# OPERATION - component: backupTable
		compArgs = {'table':'transactions'}
		self.backupTable(compArgs)

		
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
	# components
	# -------------

			
	def execAppFeatureOperations(self,args):
		print('execAppFeatureOperations()')

		print(args)
		print(json.dumps(args['operations'], indent=4))

		df = pd.DataFrame()
		try:
			args["df"]
			print('The key exists in the dictionary')
			df = args['df']
		except KeyError as error:
			print("The key doesn't exist in the dictionary")
			

		operations = args['operations']
		
		# loop by operations
			# call components & pass args
		for method, args in operations.items():
			print(method)
			print(json.dumps(args, indent=4))

			df = getattr(self, method, lambda: self.default)(df,args)
			
		return df
		#compArgs = {'table':'transactions'}
		
		#Components = self.core.Components
		#self.core.backupTable(compArgs)


	## END method ----------------------

	def retTable(self,df,args):	
		print(f'retTable()')
		
		print(json.dumps(args, indent=2))

		tableName = args['name']
		
		# build filename
		index = self.datasetsDf[self.datasetsDf['name'] == tableName].index

		filename = self.datasetsDf.loc[index[0], 'source']
		location = f'datasets/{filename}'
		print(location)
		
		# read to dataframe using helper functions
		df = pd.DataFrame(self.readDataToDf(location))

		return df
		
	## END method ----------------------
		
	def filterBy(self,df,args):	
		print(f'filterBy()')
		
		print(json.dumps(args, indent=2))

		df = df.loc[df[args['column']] == args['value']]

		return df
		
	## END method ----------------------
		
	def sum(self,df,args):	
		print(f'sum()')
		
		print(json.dumps(args, indent=2))

		groupDf = df.groupby(args['groupColumn'])[args['targetColumn']].sum()
		print(groupDf.head())

		#df[df['A'] == 'foo']
		value = groupDf[0]

		#value = df.loc[groupDf.groups[args['groupColumn']]]
		print(value)
		
		return value
		
	## END method ----------------------
		
		
	def backupTable(self,args):	
		print(f'backupTable()')
		
		print(args)
		print(json.dumps(args, indent=2))
		
		tableName = args['table']
		print(tableName)

		# call save df to file in backups
		index = self.datasetsDf[self.datasetsDf['name'] == tableName].index
		#self.selectedDatasetIndex = index[0]

		filename = self.datasetsDf.loc[index[0], 'source']
		location = f'backups/{filename}'
		print(location)
		
		# write new df to file
		#self.writeTableDftoFile(filename,self.tableDf,self.tableHeaderDf)
		
		with pd.ExcelWriter(location) as writer:
			self.tableDf.set_index('ID').to_excel(writer, sheet_name='data')
			self.tableHeaderDf.set_index('name').to_excel(writer, sheet_name='headers')
		
	## END method ----------------------




		
## END Core Class ======




class Apps:

	def __init__(self):
		print('__init__Apps()')

		self.appMethods = pd.Series([
			'runSnippet',
			#'listApps', 
			'selectApp',
			'createApp',
			'deleteApp'
		])
		
		self.appsList = pd.Series([
			'stocks',
			'Donations', 
			#'bodyFat',
			'Finances',
			'Taxes'
			#'contacts',
			#'objects'
		])
		
		self.promptOptions = self.appMethods
		

	## END method ----------------------
		
	# ------ getters & setters

	# called externally
	def getAppsList(self):
		self.promptOptions = self.appMethods
		return self.appsList

	## END method ----------------------
		
	# called externally
	def getAppMethods(self):
		return self.appMethods
		
	## END method ----------------------
		

		
	# ------ methods
		
		
	def runSnippet(self):	
		print(f'runSnippet()')
		
	## END method ----------------------

		
	# called externally
	def selectApp(self,UIClass):
		#print(self.appsList)
		#UI.promptOptions = self.appsList
		#UI.promptOptions(UI, self.appsList)

		# get user input on app from menu list
		"""Code Summary
			get user input
   			init app class 
	  		transfer UI control to app class
		"""
		
		# select index
		messagePrompt = f'select application from list: '
		listIndex = int(input(messagePrompt))

		
		classStr = self.appsList.get(listIndex, '')
		print(f'classStr: {classStr}')

		# set app name in UI class
		UIClass.appName = classStr

		# init app class
		classInstance = eval(classStr)(Core())
		#print(classInstance)
		#klass = type(classInstance)
		#print(UIClass)
		#print(klass)
		#print(classInstance.appMethods)

		# store app class in UI
		UIClass.appObject = classInstance

		# set display list
		UIClass.displayList = []
		
		# get datasets list options
		UIClass.promptOptions = classInstance.appMethods
		
		#klass = type(classInstance, (object,), {'UI': UIClass})
		
		#getattr(classInstance, 'test', lambda: classInstance.default)()
		#print(getattr(core, objAttribute, lambda: core.default)())

	## END method ----------------------

		
	def createApp(self):	
		print(f'createApp()')
		
	## END method ----------------------
		
	def deleteApp(self):	
		print(f'deleteApp()')
		
	## END method ----------------------

		
## END Apps Class ======


class Metrics:

	def __init__(self):
		print('__init__Metrics()')

		self.core = type('', (), {})()

		self.appsList = pd.Series([
			'Donations', 
			'Taxes'
		])
		
		self.appMethods = pd.Series([
			'runSnippet',
			'select'
			#'create',
			#'delete'
		])

		self.metricsDict = {
			'Donations':{
				'total2022':{
					'operations': {
						'retTable': {
							'name':'transactions'
						},
						'filterBy': {
							'column':'Expense',
							'value':'Donation'
						},
						'sum': {
							'groupColumn':'Expense',
							'targetColumn':'Amount'
						}
					}
				}
			},
			'Taxes':{
				'income2022':{
					'operations': {
						'filterBy': {
							'column':'Expense',
							'value':'Donation'
						},
						'sum': {
							'groupColumn':'Expense',
							'targetColumn':'Amount'
						}
					}
				},
				'income2023':{
					'operations': {
						'filterBy': {
							'column':'Expense',
							'value':'Donation'
						},
						'sum': {
							'groupColumn':'Expense',
							'targetColumn':'Amount'
						}
					}
				}
			}
		}

		
		self.promptOptions = self.appMethods

	## END method ----------------------

		
	# ------ getters & setters

	# called externally
	def getAppsList(self):
		self.promptOptions = self.appMethods
		return self.appsList

	## END method ----------------------
		
	# called externally
	def getAppMethods(self):
		return self.appMethods
		
	## END method ----------------------
		
	def runSnippet(self,core):	
		print(f'runSnippet()')
		self.core = core
		metricValue = self.returnMetric('Donations','total2022')
		print(f'metric: {metricValue}')
		
	## END method ----------------------

	
	def select(self,core):
		print(f'select()')

		# get user input on app from menu list
		"""Code Summary
			get user input
   			init app class 
	  		transfer UI control to app class
		"""
		
		# select index
		messagePrompt = f'select metric from list: '
		listIndex = int(input(messagePrompt))

		
		metricStr = self.appsList.get(listIndex, '')
		print(f'metricStr: {metricStr}')

		#print(self.metricsDict[metricStr])


		print(json.dumps(self.metricsDict[metricStr], indent=2))

		
	## END method ----------------------

	def returnMetric(self,app,name):
		print(f'returnMetric({app},{name})')

		print(json.dumps(self.metricsDict[app], indent=2))
		
		retValue = self.core.execAppFeatureOperations(self.metricsDict[app][name])
		return retValue
		
	## END method ----------------------


## END Metrics Class ======



class Components:

	def __init__(self):
		print('__init__Components()')


	## END init method ----------------------

	def backupTable(self,args):	
		print(f'backupTable()')
		
		print(args)
		print(json.dumps(args, indent=2))
		
		print(self)
		print(json.dumps(self, indent=2))
		
	## END method ----------------------

		
## END Components Class ======





