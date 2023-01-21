import pandas as pd
import re
from datetime import date
from tabulate import tabulate # printing tables

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

	
	def getMethods(self):
		return self.methods

		
		
## END Taxes Class ======


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
		self.df = df
		self.headersDf = headersDf
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
			'updateStatus', 
			'sumTotal', 
			'viewTrans', 
			'reviewItem', 
			'filterDateRange',
			'creditImportMacroAmazon',
			'creditImportMacroSapphire',
			'mechanicsImportMacro',
			'snippet'
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

	## END method ----------------------
		
	def updateStatus(self):
		print('updateStatus()')

	## END method ----------------------
		
	def sumTotal(self,df):
		print('sumTotal()')


	## END method ----------------------

	def viewTrans(self):
		print('viewTrans()')

		df = self.df
		
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

	def reviewItem(self,df):
		print('reviewItem()')


	## END method ----------------------

	def filterDateRange(self,df):
		print('filterDateRange()')


	## END method ----------------------

	def creditImportMacroAmazon(self,df):
		print('creditImportMacroAmazon()')


	## END method ----------------------

	def creditImportMacroSapphire(self,df):
		print('creditImportMacroSapphire()')


	## END method ----------------------

	def mechanicsImportMacro(self,df):
		print('mechanicsImportMacro()')


	## END method ----------------------

	def snippet(self,df):
		print('snippet()')


	## END method ----------------------
		
## END Taxes Class ======



class Taxes(Application):

	"""Code Summary
	check for required tables
 		create tables if need
   	
	"""
	
	def __init__(self,core):
		print('__init__Taxes()')

		self.appMethods = pd.Series([
			'setYear',
			'viewIncome',
			'totalIncome',
		])
		
		# init Core
		#core = Core()
		
		# --- check table
		tableName = 'transactions'
		print(tableName)
		filename,df,headersDf = core.loadTableToDf(tableName)
		print(df.head())
		print(filename)


		# create dataset if needed

		
		# init Apps
		#apps = Apps()
		
		#UI.displayList = self.methods
		#UI.promptOptions = self.methods
		#ui = UI()
		#UI.buildOptionsList(self.methods)

		optionsList = self.appMethods
		# show options
		for idx, x in optionsList.items():
			print(f'{idx}: {x}')
			
		# get user method select
		messagePrompt = f'select function: '
		listIndex = int(input(messagePrompt))
		
		objAttribute = optionsList.get(listIndex, '')
		print(objAttribute)

		getattr(self, objAttribute)(df)

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
