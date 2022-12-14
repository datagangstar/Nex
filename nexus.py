import pandas as pd
import re
import Nex

class UI:

	def __init__(self):
		print('__init__UI()')

		
		self.mainMenu = pd.Series([
			'Datasets',
			#'Market', 
			'Applications',
			#'Components',
			#'Mods',
			'Settings'
		])

		# set root prompt options
		self._promptOptions = self.mainMenu

		# set empty display list
		self._displayList = ''

		# set table name
		self._tableName = ''
		
		# set record name
		self._recordName = ''
		
		# use property function
		# https://www.geeksforgeeks.org/getter-and-setter-in-python/
		
		self.menuSelection = ''

		# init Nex - TURN OFF WHEN DONE CONVERTING
		nex = Nex.Nex()
		
		# init Core
		core = Core()

		# init Apps
		apps = Apps()
		

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
							
							# get datasets list options
							self.promptOptions = apps.getAppMethods()
							
						elif optionNumber == 3:
							print('--- Components')
							# get datasets list options
							
						elif optionNumber == 4:
							print('--- Mods')
							# get datasets list options
							
						elif optionNumber == 5:
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

							print(getattr(apps, objAttribute, lambda: apps.default)())
							
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
		print('set tableName(name)')
		self._tableName = name
		
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
	
		print(f'\n\n')
		print(f'----------------------')

		# build navigation & build options
		if self.menuSelection == '': 
			print(f'Menu')
		else: 
			print(self.menuSelection)
			#if not self.tableName == '': 
			print(self.tableName)

		print(f'-----------')
		
		print(self.displayList)
		
		print(f'-----------')
		
		# show options
		for idx, x in optionsList.items():
			print(f'{idx}: {x}')
	
		print(f'-----------')
		
		## END method ----------------------

	
	def processUserInput(self, message):
	
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

		
		
## END Class ======



class Core:

	def __init__(self):
		print('__init__Core()')

		self.datasetsMethods = pd.Series([
			'runSnippet',
			'selectDataset'
			#'createDataset',
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
		 	#'printTable',
			#'addTableColumn',
			#'renameColumn',
			#'dropTableColumn',
			'selectRecord',
			#'addTableItem',
			#'linkTableItem',
			#'deleteRecord',
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

	# called externally
	def getDatasetDf(self):
		return self.datasetsDf
		
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
		inputMessagePrompt = f'Select Dataset: '
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





	# -------------
	# table CRUD
	# -------------


		
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



		
## END Class ======




class Apps:

	def __init__(self):
		print('__init__Apps()')

		self.appMethods = pd.Series([
			'runSnippet',
			'listApps', 
			'selectApp',
			'createApp',
			'deleteApp'
		])
		#self.promptOptions = self.appMethods

		self.appsList = pd.Series([
			'stocks',
			'donations', 
			'bodyFat',
			'transactions',
			'taxes',
			'contacts',
			'objects'
		])
		

	# called externally
	def getAppMethods(self):
		return self.appMethods
		
	# called externally
	def listApps(self):
		return self.appsList
	
	# called externally
	def selectApp(self):
		#print(self.appsList)
		UI.promptOptions = self.appsList
		#UI.promptOptions(UI, self.appsList)

	
	def taxes(self):
		print('\n')
		print('taxes()')
		print('---------')

		# --- select table
		tableName = 'transactions'
		#filename,df,headersDf = core.loadTableToDf(tableName)
		
		# --- build select options
		print('---------')

		# selectedMethod = 'selectObj'
		
		# -- select object
		# if bool(self.selectedObject):
		# 	selectedMethod = 'clearObj'

		# index = core.promptAppFeatures([
		# 	'snippet',
		# 	'viewObjects',
		# 	'addObject',
		# 	'deleteObject',
		# 	'selectedMethod',
		# 	'addObjectItem'
		# ])

		# --- filter methods
		
		if index == 0:
			print('--- snippet()')
			print('------')
			
		else:
			print("--- try again")
		
## END Class ======
