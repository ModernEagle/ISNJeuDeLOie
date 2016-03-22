#-*- coding: utf-8 -*-
import random
import os
import sys
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
		
		if place1 == 7 :
			lol1 = place1 - 4
			print("Vous glissez sur une plaque de verglas, reculez de 4 cases, la prochaine fois faites attention")
			print("Votre nouvelle place est", lol1)
		if place2 == 7 : 
			lol2 = place2 - 4
			print("Vous glissez sur une plaque de verglas, reculez de 4 cases, la prochaine fois faites attention")
			print("Votre nouvelle place est", lol2)
		if place1 == 13 :
			lol1 = place1 + 4
			print("La température est basse, tu te dépêche d'aller te réchauffer, avance de 4 cases")
			print("Votre nouvelle place est", lol1)
		if place2 == 13 :
			lol2 = place2 + 4
			print("la température est basse, tu te dépêche d'aller te réchauffer, avance de 4 cases")
			print("Votre nouvelle place est", lol2)
		if place1 == 19 :
			lol1 = place1 +11
			print("Tu apperçois uns station de télésiège, ainsi tu évites de monter la pente par    toi-même et donc de te faire mal. Avance de 11 cases.")
			print("Votre nouvelle place est", lol1)
		if place2 == 19 :
			lol2 = place2 +11
			print("Tu apperçois uns station de télésiège, ainsi tu évites de monter la pente par    toi-même et donc de te faire mal. Avance de 11 cases.")
			print("Votre nouvelle place est", lol1)
		if place1 == 24 :
			print("Tu es près d'une crevasse, fait le tour pour ne pas risquer ta vie.")
			action = lancedede()
			if action == 1 :
				lol1 = place1 + 1
			if action == 2 :
				lol1 = place1 + 2
			if action == 3 :
				lol1 =place1 +3
				
				print("Tu es agile, tu avances de", action, "cases") 
				print("Votre nouvelle place est", lol1)
		if place2 == 24 :
		print("Tu es près d'une crevasse, fait le tour pour ne pas risquer ta vie.")
			action = lancedede()
			if action == 1 :
				lol2 = place2 + 1
			if action == 2 :
				lol2 = place2 + 2
			if action == 3 :
				lol2 = place2 +3
				
				print("Tu es agile, tu avances de", action, "cases")
				print("Votre nouvelle place est", lol2) 
		if place1 == 32 :
			action = lancedede()
			if action == 1 :
				lol1 = place1 + 1
			if action == 3 :
				lol1 = place1 + 3
			if action == 5 :
				lol1 = place1 +5
		if place2 == 32 :
			action = lancedede()
			if action == 1 :
				lol2 = place2 + 1
			if action == 3 :
				lol2 = place2 + 3
			if action == 5 :
				lol2 = place2 +5
				
		if place1 == 41 :
			patient = 0
			while patient != 1 :
				os.system("clear")
	
#				while victoire != 1:
#					try: raw_input = input
#					except NameError: pass
#					print(raw_input("Appuyez pour passer au joueur 1"))
#					os.system("clear")	
#					print(raw_input("Joueur 1 : Vous passez votre tour\n"))
#		
#					print(raw_input("\nAppuyez pour passer au joueur 2"))
#					os.system("clear")		
#					print(raw_input("Joueur 2 : Appuyez sur une touche pour lancer le dé"))
#
#					resultat = lancedede()
#					if place2 != 0 :
#						print("Votre place actuelle est ",lol2)
#					print("Le résultat du lancé de dé est ", resultat)
#					place2 = lol2 + resultat
#					lol2 = place2
#					print("Votre place est ",lol2, "\n")
#					if place2 > 65 :
#						trop = lol2 - 65
#						print ("Votre dépassement est de :", trop)
#						print("Votre place est supérieure à 65 !")
#						trop = trop + 1 
#						lol2 = place2 - trop
#						print("Votre nouvelle place est : ", lol2)
#					if place2 == 41 :
#						patient = 1
#						victoire = 1
#						print("Le joueur 2 Libère le 1")
#					if place2 == 65 :
#						print("JOUEUR 2 GAGNE")
#						victoire = 1
#
#		if place2 == 41 :
#			
#			
#		if place1 == 48 :
#			
#			
#		if place2 == 48 :
#
#
		if place1 == 55 : 
			lol1 = place1 + 5
			print ("Vous avez eu de la chance en vous perdant et avez observé de la lumière à travers les arbres de la fôret, avancez de 5 cases")
			print("Votre nouvelle place est", lol1)
		if place2 == 55 :
			lol2 = place2 + 5
			print ("Vous avez eu de la chance en vous perdant et avez observé de la lumière à travers les arbres de la fôret, avancez de 5 cases")
			print ("Votre nouvelle place est", lol2)
#		if place1 == 59 :
#			
#		if place2 == 59 :
#			
#		if place1 == 63 :
#			lol1 = place1 - 63
#			print("Vous êtes tombé dans la crevasse, on vous a rappatrié à la case départ")
#		if place2 == 63 :
#			lol2 = place2 - 63
#			print("Vous êtes tombé dans la crevasse, on vous a rappatrié à la case départ")
deplusieur() 
