import pandas as pd
import re

class UI:

	def __init__(self):
		print('__init__UI()')

		
		self.mainMenu = pd.Series([
			'Datasets',
			'Market', 
			'Applications',
			'Components',
			'Mods',
			'Settings'
		])
		self.promptOptions = self.mainMenu
		self.menuSelection = ''
		
		self.datasetsMethods = pd.Series([
			'runSnippet',
			'selectDataset', 
			'createDataset',
			'deleteDataset',
			'runStocksApp',
			'runDonationApp',
			'runBodyFatApp',
			'runTransactionsApplication',
			'runContactsApp',
			'runObjectsApp'
		])

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
					print(f'-----------')
				
					if self.menuSelection == '': 
						print('do menu')
						self.menuSelection = objAttribute
	
					else: 
						print('do core')
						#print(getattr(nex, objAttribute, lambda: nex.default)())
			

			
	def buildOptionsList(self, optionsList):
	
		print(f'\n\n')
		print(f'-----------')
		
		if self.menuSelection == '': 
			print(f'Menu')
		else: 
			print(self.menuSelection)
	
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



class Core:

	def __init__(self):
		print('__init__Core()')

