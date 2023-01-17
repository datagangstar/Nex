import Nex
import re
import nexus



# nexus prototype
nexUI = nexus.UI()

# init objct nex r&d
##nex = Nex.Nex()


# todo - move out of class
def initateUserInput():

	# new features
	# - back option
	# - last selected option
	# - 
	
	# - field app


	
	while True:

		# get list of prompt options
		optionsList = nex.getPromptOptions()
		
		# product options list
		buildOptionsList(optionsList)
		
		# list length to int
		numMethods = int(len(optionsList))
	
		# get option selection
		inputMessagePrompt = 'Select option:'
		resDict = processUserInput(inputMessagePrompt)
		
		if resDict['valid']:
			optionNumber = int(resDict['value'])
			
			#print(f'optionNumber: {optionNumber} -- numMethods: {numMethods}')
			if (optionNumber <= numMethods):
				# break;
				objAttribute = optionsList.get(optionNumber, '')
				print(f'Selected option: {objAttribute}')
				print(f'-----------')
				print(getattr(nex, objAttribute, lambda: nex.default)())
				#print(getattr(p1, objAttribute, 'test default'))

				
	## END method ----------------------

# scenarios
# 1 printDataSets
# 2 viewDataset, 3 stocks


def buildOptionsList(optionsList):

	print(f'-----------')
	print(nex.getNavigation())
	print(f'Menu')

	print(f'-----------')
	
	
	# show options
	for idx, x in optionsList.items():
		print(f'{idx}: {x}')

	print(f'-----------')
	
	## END method ----------------------

	

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


# start user input -proof of concept Nex
##initateUserInput()


# test adding dataset



# def get_country(location):
#     try:
#         return location['country']
#     except Exception:
#         return 'n/a'
