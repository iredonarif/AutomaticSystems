def demanderPrix(num):
	prix = input('Quel est le prix du produit n° '+ str(num)+ ' ? ')
	if prix.isnumeric(): return int(prix)
	else:
		print('Attention prix incorecte !!!')
		return demanderPrix(num)

def billetOuPiece(n):
	return "billet" if n >=500 else "pièce"

def demanderLesPrix():
	n, somme = 1, 0
	prix = demanderPrix(n)
	somme += prix
	while prix !=0:
		n += 1
		prix = demanderPrix(n)
		print(somme, prix)
		somme += prix
	return somme

def rendreMonnaie(somme):
	billets_pieces = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
	for i in billets_pieces:
		if somme >= i:
			n = somme // i
			somme -= n * i
			print(n, billetOuPiece(i), ' de ', str(i), 'FCFA')

def sommeClientCorrecte(prixApayer, message = 'Quel somme a donné le client ? '):
	somme = int(input(message))
	return somme if somme >= prixApayer else sommeClientCorrecte(prixApayer, 'Somme inférieure. Veuillez renseigner une somme correcte : ')

def caisseAuto():
	messageBienvenue();

	prix_a_payer = demanderLesPrix()
	print('Prix à payer ', prix_a_payer)
	sommeClient = sommeClientCorrecte(prix_a_payer)
	somme_a_rendre = sommeClient - prix_a_payer
	print('Somme à rendre : ', somme_a_rendre)
	print('Il faut rendre :')
	rendreMonnaie(somme_a_rendre)

def messageBienvenue():
	print('==============================================')
	print('BIENVENUE DANS LE SYSTEME CAISSE AUTOMATIQUE')
	print('==============================================', '\n')

caisseAuto()
