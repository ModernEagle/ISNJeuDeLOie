#-*- coding: utf-8 -*-
import random
import os
import sys 
def lancedede():
	typD = 6
	nbD = 1
	resultat = (random.randrange(1,(typD+1)))
	return (resultat)

def nbjoueur() :
	try: raw_input = input
	except NameError: pass
	print("Quel est le nombre de joueurs ?\n")
	print("(Tapez 2 ou 3 ou 4 pour définir ce nombre)\n")
	nombre = 2
	choix = input()
	nombre = int(choix)
	print("Choix = ", choix, "Nombre = ", nombre, ) 
	print("Vous avez selectionné ", nombre)
	print(raw_input("\nAppuyez pour continuer"))
	return(nombre)

def deplusieur() :
	os.system("clear")
	victoire = 0
	lol1 = 0
	lol2 = 0
	lol3 = 0
	lol4 = 0
	place1 = 0
	place2 = 0
	place3 = 0
	place4 = 0
	nbjou = nbjoueur()
	while victoire != 1:
		try: raw_input = input
		except NameError: pass
		print(raw_input("Appuyez pour passer au joueur 1"))
		os.system("clear")	
		print(raw_input("Joueur 1 : Appuyez sur une touche pour lancer le dé\n"))
		resultat = lancedede()
		if place1 != 0 :
			print("Votre place actuelle est ",lol1)
		print("Le résultat du lancé de dé est", resultat)
		place1 = lol1 + resultat
		lol1 = place1
		print("Votre place est ",lol1)
		if place1 > 65 :
			trop = lol1 - 65
			print ("Votre dépassement est de :", trop)
			print("Votre place est supérieure à 65 !")
			depa = trop*2
			lol1 = place1 - depa
			print("Votre nouvelle place est :", lol1)
		if place1 == 65 :
			print("JOUEUR 1 GAGNE")
			victoire = 1
			sys.exit()
			
		print(raw_input("\nAppuyez pour passer au joueur 2"))
		os.system("clear")		
		print(raw_input("Joueur 2 : Appuyez sur une touche pour lancer le dé"))

		resultat = lancedede()
		if place2 != 0 :
			print("Votre place actuelle est ",lol2)
		print("Le résultat du lancé de dé est ", resultat)
		place2 = lol2 + resultat
		lol2 = place2
		print("Votre place est ",lol2, "\n")
		if place2 > 65 :
			trop = lol2 - 65
			print ("Votre dépassement est de :", trop)
			print("Votre place est supérieure à 65 !")
			depa = trop*2
			lol2 = place2 - depa
			print("Votre nouvelle place est : ", lol2)
		if place2 == 65 :
			print("JOUEUR 2 GAGNE")
			victoire = 1
			
			
		if nbjou >= 3:
			print(raw_input("\nAppuyez pour passer au joueur 3"))
			os.system("clear")		
			print(raw_input("Joueur 3 : Appuyez sur une touche pour lancer le dé"))
			resultat = lancedede()
			if place3 != 0 :
				print("Votre place actuelle est ",lol3)
			print("Le résultat du lancé de dé est ", resultat)
			place3 = lol3 + resultat
			lol3 = place3
			print("Votre place est ",lol3, "\n")
			if place3 > 65 :
				trop = lol3 - 65
				print ("Votre dépassement est de :", trop)
				print("Votre place est supérieure à 65 !")
				depa = trop*2
				lol3 = place3 - depa
				print("Votre nouvelle place est : ", lol3)
			if place3 == 65 :
				print("JOUEUR 3 GAGNE")
				victoire = 1
				sys.exit()
			
		if nbjou == 4:
			print(raw_input("\nAppuyez pour passer au joueur 4"))
			os.system("clear")		
			print(raw_input("Joueur 4 : Appuyez sur une touche pour lancer le dé"))
			resultat = lancedede()
			if place4 != 0 :
				print("Votre place actuelle est ",lol4)
			print("Le résultat du lancé de dé est ", resultat)
			place4 = lol4 + resultat
			lol4 = place4
			print("Votre place est ",lol4, "\n")
			if place4 > 65 :
				trop = lol3 - 65
				print ("Votre dépassement est de :", trop)
				print("Votre place est supérieure à 65 !")
				depa = trop*2
				lol4 = place4 - depa
				print("Votre nouvelle place est : ", lol4)
			if place4 == 65 :
				print("JOUEUR 4 GAGNE")
				victoire = 1
				sys.exit()


deplusieur() 
