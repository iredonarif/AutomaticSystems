import guichetActions;

def chooseAnAction():
	response = input("\n À quelle action voulez-vous proceder :\n (s) Consulter votre solde \n " + 
	 "(r) Faire un retrait\n (d) Faire un dépôt\n (c) Créer un compte\n (q) ou quitter\n")

	validity = len(response) == 1 and response[0].capitalize() in 'SRDCQ'
	return (validity, response)

def getCorrectAction():
	choice = chooseAnAction()
	while not choice[0] :
		choice = chooseAnAction()
	return choice[1].capitalize()

def processTheChoice():
	action = getCorrectAction()
	while action != 'Q':
		theActions[action]()
		action = processTheChoice()
	exit()

def balance():
	guichetActions.balance()

def withdrawal():
	guichetActions.withdrawal()

def deposit():
	guichetActions.deposit()

def createAccount():
	guichetActions.createAccount()

def guichetAuto():
	print('=================================================', '\n')
	print('BIENVENUE SUR NOTRE SYSTEME GUICHET AUTOMATIQUE', '\n')
	print('=================================================')

	processTheChoice()

theActions = { 'S': balance, 'R': withdrawal, 'D': deposit, 'C': createAccount }


if __name__ == '__main__':
	guichetAuto()
