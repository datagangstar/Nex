import pandas as pd
import re

# get list of class methods
# https://www.askpython.com/python/examples/find-all-methods-of-class#:~:text=To%20list%20the%20methods%20for%20this%20class%2C%20one%20approach%20is,and%20properties%20of%20the%20class.

class Finances:

	"""Code Summary
	check for required tables
 		create tables if need
   	
	"""
	
	def __init__(self):
		print('__init__Finances()')

		self.appMethods = pd.Series([
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
		print(self.appMethods)

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