import pandas as pd
import re

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
	
	def __init__(self):
		print('__init__Finances()')

		# init app parent
		super().__init__()
		
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

	def viewTrans(self,df):
		print('viewTrans()')


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
