import pandas as pd
import re
import uuid
from datetime import date
from tabulate import tabulate # printing tables
import json

# get list of class methods
# https://www.askpython.com/python/examples/find-all-methods-of-class#:~:text=To%20list%20the%20methods%20for%20this%20class%2C%20one%20approach%20is,and%20properties%20of%20the%20class.



class Application:

	"""Code Summary
	check for required tables
 		create tables if need
   	
	"""
	
	def __init__(self):
		print('__init__Applications()')
		
		self.methods = pd.Series([
			'back'
		])
		print(self.methods)

	## END INIT method ----------------------

	# ------ getters & setters


	def loadSettings(self):
		return self.methods

	## END method ----------------------
	
	def getMethods(self):
		return self.methods

	## END method ----------------------

		
	def formatTable(self,df,headersDf):
		
		for index, row in headersDf.iterrows():
			print(f'idx({index})[{row["dtype"]}] - {row["name"]}')

			dtype = row["dtype"]
			name = row["name"]
			
			if dtype == 'datetime64':
				print('--- datetime64')
				df[name]= pd.to_datetime(df[name])

			elif dtype == 'int':
				print("int")
				df[name] = df[name].astype('int')
				
			elif dtype == 'float':
				print("float")
				df[name] = df[name].astype('float')
				
			elif dtype == 'str':
				print("str")
				df[name] = df[name].astype('str')
			else:
				print("object")
				
		return df

	## END method ----------------------


		
## END Taxes Class ======



class Donations(Application):
	
	def __init__(self,core):
		print('__init__Donations()')

		self.core = core

		# init app parent
		super().__init__()

		filename,df,headersDf = core.loadTableToDf('transactions')
		
		self.filename = filename
		self.tableDf = super().formatTable(df,headersDf)
		self.tableHeaderDf = headersDf

		methods = pd.Series([
			'setup'
		])
		
		# combine parent and app methods
		self.appMethods = methods
		
	## END INIT method ----------------------

	
	def setup(self):
		print('setup()')

		messagePrompt = f'Enter filter (2022-XX): '
		#value = input(messagePrompt)

		#
		#
		filterValue = '2022'

		df = self.tableDf
		
		# list all donation transactions
		# sum donation total

		
		# df = df.loc[df['Expense'] == "Donation"]
		
		# #df = df[df['Transaction Date'].dt.strftime('%Y') == 2022]
		# print(df)

		# groupDf = df.groupby('Expense')['Amount'].sum()
		# print(groupDf)

		
		args = {
			'df': self.tableDf,
			'operations': {
				'filterBy': {
					'column':'Expense',
					'value':'Donation'
				},
				#'print':'default', # all, default, []
				'sum': {
					'groupColumn':'Expense',
					'targetColumn':'Amount'
				}
			}
		}
		

		df = self.core.execAppFeatureOperations(args)
		print(df)

	## END method ----------------------

		
## END Donations Class ======
		


class Finances(Application):

	"""Code Summary
	check for required tables
 		create tables if need
   	
	"""
	
	def __init__(self,core):
		print('__init__Finances()')

		self.core = core

		# init app parent
		super().__init__()

		filename,df,headersDf = core.loadTableToDf('transactions')
		self.filename = filename
		#self.df = df
		self.tableDf = df
		#self.headersDf = headersDf
		self.tableHeaderDf = headersDf
		print(df.info())

		
		for index, row in headersDf.iterrows():
			print(f'idx({index})[{row["dtype"]}] - {row["name"]}')

			dtype = row["dtype"]
			name = row["name"]
			
			if dtype == 'datetime64':
				print('--- datetime64')
				df[name]= pd.to_datetime(df[name])

			elif dtype == 'int':
				print("int")
				df[name] = df[name].astype('int')
				
			elif dtype == 'float':
				print("float")
				df[name] = df[name].astype('float')
				
			elif dtype == 'str':
				print("str")
				df[name] = df[name].astype('str')
			else:
				print("object")
				
		print(df.info())
		
		
		methods = pd.Series([
			'sumGroup', 
			'NAupdateStatus', 
			'sumTotal', 
			'viewTrans', 
			'reviewItem', 
			'filterDateRange',
			'creditImportMacroAmazon',
			'creditImportMacroSapphire',
			'mechanicsImportMacro',
			'snippet',
			'PRIVATEperformImport'
		])
		#print(self.appMethods)

		# combine parent and app methods
		self.appMethods = pd.concat([methods, super().getMethods()], axis=0)
		#print(self.appMethods)

		#self.appMethods = methods

		#self.appMethods()
		
		self.settingsDict = {}

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
		
	## END INIT method ----------------------

	# ------ getters & setters
		
	# getter ------
	@property
	def appMethods(self):
		return self._appMethods
	
	## END method ----------------------

	# setter
	@appMethods.setter
	def appMethods(self, methods):
		print('appMethods(methods)')
		self._appMethods = methods
		
		
	def sumGroup(self):
		print(f'sumGroup()')

		df = self.tableDf
		
		df = df.loc[df['Reviewed'] == 1]

		# filter by selected MONTH
		filterDate = self.settingsDict['transactions']['settings']['dateFilter']
		#df['yearMonth'] = df['Transaction Date'].dt.strftime('%Y-%m')
		
		if bool(filterDate):
			df = df[df['Transaction Date'].dt.strftime('%Y-%m') == filterDate]
			print(f'Filter Month: {filterDate}')
		else:
			print('no date filter')

		print('------')

		
		#set type to float
		#df['Amount'] = pd.to_numeric(df['Amount'])
		
		groupDf = df.groupby('Expense')['Amount'].sum()
		print(groupDf)
			
		total = df['Amount'].sum()
		print(f'Total: {total}')

	## END method ----------------------
		
	def updateStatus(self):
		print('updateStatus()')

	## END method ----------------------
		
	def sumTotal(self):
		print('sumTotal()')
		
		df = self.tableDf

		print(df.head())
		df = df.loc[df['Reviewed'] == 1]

		# filter by selected MONTH
		filterDate = self.settingsDict['transactions']['settings']['dateFilter']
		print(df.head())
			
		if bool(filterDate):
			#df = df[df['yearMonth'] == filterDate]
			df = df[df['Transaction Date'].dt.strftime('%Y-%m') == filterDate]

			print(f'Filter Month: {filterDate}')
		else:
			print('no date filter')

		print('------')
			
			
		groupDf = df.groupby('Account')['Amount'].sum()
		print(groupDf)


	## END method ----------------------

	def viewTrans(self):
		print('viewTrans()')

		df = self.tableDf
		
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

		# get report table columns
		# headersArray = [
		#  'Amount', 'Description', 'Expense', 'Transaction Date', 'Reviewed', 'Card'
		# ]
		headersArray = self.core.getTableDefaultHeaders()
		print(headersArray)

		# print report talbe
		UI = self.core.UI
		UI.printFormattedTable(self,df,headersArray)

		#print(tabulate(df[self.core.getTableDefaultHeaders()], self.core.getTableDefaultHeaders(), tablefmt='psql'))

	## END method ----------------------

	def reviewItem(self):
		print('reviewItem()')

		df = self.tableDf
		UI = self.core.UI
		
		# filter by selected MONTH
		filterDate = self.settingsDict['transactions']['settings']['dateFilter']
		#print(bool(filterDate))
		
		if bool(filterDate):
			# do not save the report df
			reportDf = df[df['Transaction Date'].dt.strftime('%Y-%m') == filterDate]
			print(f'Filter Month: {filterDate}')
		else:
			print('no date filter')
			reportDf = df.copy()

		print('------')

		# sort report 
		reportDf = reportDf.sort_values(by='Transaction Date', ascending=True)
		
		headersArray = [
			"Description", 
			"Account", 
			"Expense", 
			"Transaction Date",
			"Amount", 
			"Reviewed"
		]
		#print(tabulate(reportDf[headersArray], headersArray, tablefmt='psql'))
		
		UI.printFormattedTable(self,reportDf,headersArray)
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
		df.loc[recordIndex, 'modified'] = date.today().strftime("%m/%d/%Y")
		df.loc[recordIndex, 'Reviewed'] = True
		print(df.loc[recordIndex])

		# write new df to file
		self.core.writeTableDftoFile(self.filename,df,self.tableHeaderDf)

	## END method ----------------------

	def filterDateRange(self):
		print('filterDateRange()')
		
		print('--- filterDateRange')

		settingsDict = self.settingsDict
		print(settingsDict)
		
		messagePrompt = f'Enter filter (2022-XX): '
		value = input(messagePrompt)
		
		settingsDict['transactions']['settings']['dateFilter'] = value
		print(settingsDict)
		self.settingsDict = settingsDict


	## END method ----------------------

	def creditImportMacroAmazon(self):
		print('creditImportMacroAmazon()')

		
		testFilename = 'Chase3439.CSV'


		# app feature operations
		args = {
			'filename': testFilename,
			'operations': {
				'readfile': {
					'location':'imports',
					'type':'csv'
				},
				'getAppAttr':'importDf',
				'dropColumn':'Memo',
				'renameColumn': {
					'name':'Type',
					'new':'Kind'
				},
				'addColumn':{'column':'Imported','value':''},
				'addColumn':{'column':'Account','value':''},
				'addColumn':{'column':'Reviewed','value':''},
				'addColumn':{'column':'Expense','value':''},
				'setAppAttr':{'attr':'importDf','value':''},
				'component':{'name':'backUpTable','table':'transactions'}
			}
		}
		

		#self.execAppFeatureOperations(args)


		# OPERATION - readfile
		extension = testFilename.split(".")
		print(extension)

		location = f'imports/{testFilename}'
		print(f'location: {location}')

		# load by extension type
		self.importDf = pd.read_csv(location)

		# OPERATION - getAppAttr
		df = self.importDf

		# OPERATION - dropColumn
		print('drop')
		df.drop('Memo', axis=1, inplace=True)
		
		# OPERATION - renameColumn
		print('rename')
		df.rename(columns={'Type': 'Kind'}, inplace=True)

		# OPERATION - addColumn
		# add reviewed with default false
		print('add')
		df['Imported'] = date.today().strftime("%m/%d/%Y")
		df['Account'] = "Amazon"
		df['Reviewed'] = "0"
		df['Expense'] = ""

		print(df)
		print(df.info())

		# OPERATION - setAppAttr
		self.importDf = df

		# OPERATION - component: backupTable
		compArgs = {'table':'transactions'}
		self.core.backupTable(compArgs)

		# trigger import
		self.performImport()


	## END method ----------------------

	def creditImportMacroSapphire(self):
		print('creditImportMacroSapphire()')


		testFilename = 'Chase9901.CSV'
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
		df['Account'] = "Sapphire"
		df['Reviewed'] = "0"
		df['Expense'] = ""

		print(df)
		print(df.info())

		self.importDf = df

		# trigger import
		self.performImport()


	## END method ----------------------

	def mechanicsImportMacro(self):
		print('mechanicsImportMacro()')

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
		print(self.importDf.columns)

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
		df['Account'] = "Mechanics"
		df['Reviewed'] = "0"
		df['Expense'] = ""

		print(df.info())

		# drop memo
		print('drop')

		dropList = [
			'Transaction Number', 
			'Memo', 
			'Balance', 
			'Check Number', 
			'Amount Debit', 
			'Amount Credit', 
			'Fees  ']

		# loop through list, if exists, drop
		df = self.core.dropColumns(df,dropList)
		#df.drop(dropList, axis=1, inplace=True)

		print(df)
		print(df.info())

		self.importDf = df

		# trigger import
		self.performImport()


	## END method ----------------------

	def snippet(self):
		print('snippet()')
		
		args = {
			'operations': {
				'component':{'name':'backupTable','table':'transactions'}
			}
		}

		self.execAppFeatureOperations(args)


	## END method ----------------------

		
	def execAppFeatureOperations(self,args):
		print('execAppFeatureOperations()')

		print(args)
		print(json.dumps(args, indent=2))

		# loop by operations
			# call components & pass args

		compArgs = {'table':'transactions'}
		
		#Components = self.core.Components
		self.core.backupTable(compArgs)


	## END method ----------------------


	def performImport(self):
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

			for idx, x in enumerate(importColumns):
				print(f'{idx}: {x}')

				rowDict[x] = row[x]

			print(rowDict)

			rowDf = pd.DataFrame(rowDict, index=[0])
			print('rowDf')
			print(rowDf)

			newDf = pd.concat([newDf, rowDf], ignore_index=True)

		print(newDf.head())

		# copy new table to global
		self.tableDf = newDf
		print(self.tableDf.info())

		# --- format headers
		headerDf = self.tableHeaderDf.copy()
		
		df1 = headerDf.apply(self.formatTableColumn, axis=1)
		
		# get headers from new df
		print(self.tableDf.info())

		print(self.tableHeaderDf)
		
		print(self.tableDf)

		
		# --- format headers
		self.core.tableDf = self.tableDf
		self.core.tableHeaderDf = self.tableHeaderDf

		# --- create tables
		print(self.core.selectedDatasetIndex)
		source = self.core.datasetsDf.loc[self.core.selectedDatasetIndex, 'name']
		#filename = f'{source}_{date.today().strftime("%m%d%Y")}.xlsx'
		print(source)

		filename = f'{source}.xlsx'
		
		# write new df to file
		self.core.writeTableDftoFile(filename,self.tableDf,self.tableHeaderDf)

		# return to main menu
		self.promptOptions = self.core.datasetsMethods

		## END method ----------------------

		
	def formatTableColumn(self,row):
		print('formatTableColumn()')

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
	
## END Finances Class ======



class Taxes(Application):

	"""Code Summary
	check for required tables
 		create tables if need
   	
	"""
	
	def __init__(self,core):
		print('__init__Taxes()')

		self.core = core
		
		# init app parent
		super().__init__()
		

		filename,df,headersDf = core.loadTableToDf('transactions')
		
		self.filename = filename
		self.tableDf = super().formatTable(df,headersDf)
		self.tableHeaderDf = headersDf

		self.appMethods = pd.Series([
			'setup',
			'setYear',
			'viewIncome',
			'totalIncome',
		])
		
		
		# optionsList = self.appMethods
		# # show options
		# for idx, x in optionsList.items():
		# 	print(f'{idx}: {x}')
			
		# # get user method select
		# messagePrompt = f'select function: '
		# listIndex = int(input(messagePrompt))
		
		# objAttribute = optionsList.get(listIndex, '')
		# print(objAttribute)

		# getattr(self, objAttribute)(df)

		# settings
		# - dashboard report 
		# - metrics
		# - methods list
		# - 
		
		

		
	## END INIT method ----------------------

		
	# ------ getters & setters
		
	# getter ------
	@property
	def appMethods(self):
		return self._appMethods
	
	## END method ----------------------

	# setter
	@appMethods.setter
	def appMethods(self, methods):
		print('appMethods(methods)')
		self._appMethods = methods

	## END method ----------------------

		
	def setup(self):
		print('setup()')

		messagePrompt = f'Enter filter (2022-XX): '
		#value = input(messagePrompt)

		#
		#
		filterValue = '2022'

		df = self.tableDf


		# ---
		# make form and line object
		# get income metric value
		# assign to class variable by form & line
			# 
		# template spreadsheet
			# form, line, name, value, value type, calc or reference, description
			# value type: reference, metric
		# product report file 


		
		args = {
			'df': self.tableDf,
			'operations': {
				'filterBy': {
					'column':'Expense',
					'value':'Donation'
				},
				#'print':'default', # all, default, []
				'sum': {
					'groupColumn':'Expense',
					'targetColumn':'Amount'
				}
			}
		}
		
		

		df = self.core.execAppFeatureOperations(args)
		print(df)

	## END method ----------------------
		
		
	def setYear(self):
		print(f'setYear()')

	## END method ----------------------
		
	def viewIncome(self):
		print('viewIncome()')

	## END method ----------------------
		
	def totalIncome(self,df):
		print('totalIncome()')

		
		df = df.loc[df['Reviewed'] == 1]
		df = df.loc[df['Expense'] == "Income"]
		
		#df = df[df['Transaction Date'].dt.strftime('%Y') == 2022]
		print(df)

		groupDf = df.groupby('Account')['Amount'].sum()
		print(groupDf)


		# df, grouping column, target column, method
		# 

		# save this as a metric in the app, make accessable by other other apps
		codeStr = """print(df.groupby('Account')['Amount'].sum())"""
  			
		exec(codeStr)

		# name, df, grouping column, target column, method
		params = {
			 'name': 'totalIncomeByYear',
			 'transformations': [
				 """df.loc[df['Reviewed'] == 1]"""
				 """df.loc[df['Expense'] == "Income"]"""
				 """print(df.groupby('Account')['Amount'].sum())"""
				 ],
			 'dtype': 'int'
		}
		#super().defineMetric(params)
		

	## END method ----------------------


		
		
## END Taxes Class ======



