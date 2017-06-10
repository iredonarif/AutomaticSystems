import string
import random
from datetime import date
from user import User

"""This module contains the different use cases of the 'Guichet automatic system' """

#To make a deposit
def deposit():
	identifier = getCorrectAttribute('Entrez votre identifiant : ', analyseStringResponse)

	user = getUserById(identifier)
	if(user):
		amount = getCorrectAttribute('Entrez la somme à déposer : ', analyseIntegerResponse)
		newBalance = int(user.balance) + int(amount)
		replaceLine(int(user.id[-1]), '{};{};{};{};{};{}'.
			format(user.id, user.lastName, user.firstName, newBalance, user.code, user.createdAt))

		print('Dépôt effectué avec succès. Votre nouveau solde est :', newBalance, 'FCFA')
	else:
		print('Cet identifiant n\'existe pas.')

#To get the balance
def balance():
	identifier = getCorrectAttribute('Entrez votre identifiant : ', analyseStringResponse)

	user = getUserById(identifier)
	if(user):
		if(getUserCode(user)):
			print('Votre solde est : ' + user.balance + 'FCFA')
	else:
		print('Cet identifiant n\'existe pas.')

#To make a withdrawal
def withdrawal():
	identifier = getCorrectAttribute('Entrez votre identifiant : ', analyseStringResponse)

	user = getUserById(identifier)
	if(user):
		if(getUserCode(user)):
			amount = int(getCorrectAttribute('Entrez la somme à retirer : ', analyseIntegerResponse))
			if(amount > int(user.balance)):
				print('Votre solde est insuffisant pour effectuer ce retrait')
			else:
				newBalance = int(user.balance) - amount
				replaceLine(int(user.id[-1]), '{};{};{};{};{};{}'.
					format(user.id, user.lastName, user.firstName, newBalance, user.code, user.createdAt))

				print('Retrait effectué avec succès. Votre nouveau solde est :', newBalance, 'FCFA')
	else:
		print('Cet identifiant n\'existe pas.')

#To create a user account. The user specified is lastname, firstname and is secret code (4digits)
def createAccount():
	lastName = getCorrectAttribute('Entrez votre nom : ', analyseStringResponse)
	firstName = getCorrectAttribute('Entrez votre prénom : ', analyseStringResponse)
	code = getCorrectAttribute('Entrez votre code secret (4 chiffres) : ', analyseIntegerResponse)
	identifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(5)) + str(countUsers() + 1)

	user = User(identifier, lastName, firstName, 0, code, date.today())

	if confirmation() == 'O':
		saveUser(user)
	else:
		print('Compte non créé !!!')

#To save the user
def saveUser(user):
	try:
		userFile = open('users.txt', 'a')
		userFile.write('{}; {}; {}; {}; {}; {}\n'.format(user.id, user.lastName, user.firstName, user.balance, user.code, user.createdAt))
		userFile.close()
		print('Compte créé avec succès. \n Votre identifiant est : ' + user.id)
	except:
		print('Erreur Fichier introuvable !!!')

#Get a user by id. Return none if the id dont match any user
def getUserById(identifier):
	file = None
	user = None

	try: file = open('users.txt')
	except: file = None

	if(file):
		for line in file:
			if line != "\n":
				u = line.split(';')
				if u[0] == identifier :
					user = User(u[0], u[1], u[2], u[3], u[4], u[5])
					break
		file.close()
	return user

#Ask the secret code of the specified user. Return True if the entered code match the user's code
def getUserCode(user):
	code = getCorrectAttribute('Entrez votre code secret : ', analyseIntegerResponse)
	return True if user.code.strip() == str(code) else getUserCode(user)
		
def confirmation():
	choice = input('\nÊtes-vous sûr de vouloir enregistrer(o/n) ? ').capitalize()
	validity = len(choice) == 1 and choice in 'ON'

	if validity: return choice
	else : confirmation()

#Ask an attribute value to the user. It takes a question(string) as parameter
def askAttribute(question):
	return input(question)

#Get the correct value of a attribute. It takes two parameters a question(string) and a function name; this function checks if the value is correct
def getCorrectAttribute(question, analyseParticularAttributeResponse):
	response = askAttribute(question)
	validityAndAttribute = analyseParticularAttributeResponse(response)
	if validityAndAttribute[0]: return validityAndAttribute[1]
	else: return getCorrectAttribute(question, analyseParticularAttributeResponse) 

#Checks if a string value is valid/correct
def analyseStringResponse(response):
	validity = None
	try: int(response)
	except: validity = len(response) >= 2
	return validity, response

#Checks if an integer value is valid/correct
def analyseIntegerResponse(response):
	integer = None
	validity = None
	try: 
		integer = int(response)
		validity = True
	except : validity = False
	return validity, integer

#Return the number of users
def countUsers():
	file = None
	try: file = open('users.txt')
	except: file = None

	numUsers = 0
	if(file):
		for line in file:
			if line != "\n": numUsers += 1
		file.close()

	return numUsers

#To replace a specific line in a the user file. Can be used to edit a user.
def replaceLine(lineNum, text):
	try:
		lines = open('users.txt', 'r').readlines()
		lines[lineNum - 1] = text

		file = open('users.txt', 'w')
		file.writelines(lines)
		file.close()

	except:
		print('Erreur Fichier introuvable !!!')