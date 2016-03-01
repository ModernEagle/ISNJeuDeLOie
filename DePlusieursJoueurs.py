#-*- coding: utf-8 -*-
import random
import os
def lancedede():
	typD = 6
	nbD = 1
	resultat = (random.randrange(1,(typD+1)))
	return (resultat)

def deplusieur() :
	os.system("clear")
	victoire = 0
	lol1 = 0
	lol2 = 0
	place1 = 0
	place2 = 0
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
			trop = trop + 1 
			lol1 = place1 - trop
			print("Votre nouvelle place est :", lol1)
		if place1 == 65 :
			print("JOUEUR 1 GAGNE")
			victoire = 1
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
			trop = trop + 1 
			lol2 = place2 - trop
			print("Votre nouvelle place est : ", lol2)
			
		if place2 == 65 :
			print("JOUEUR 2 GAGNE")
			victoire = 1
		


deplusieur() 
