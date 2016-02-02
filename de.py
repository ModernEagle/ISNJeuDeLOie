#-*- coding: utf-8 -*-
import random
import os
os.system("color F")
 
print("Cette superbe phrase est de couleur blanche !")
def lancedede():
	typD = 6
	nbD = 1
	resultat = (random.randrange(1,(typD+1)))
	return (resultat)
	

lol = 0
place = 0
while place != 65 :
	resultat = lancedede()
	print("Le résultat du lancé de dé est ", resultat)
	place = lol + resultat
	lol = place
	print("Votre place est ",lol)
	if place > 65 :
		"""trop = 65 - lol"""
		print("Votre place est supérieure à 65 !")
		lol = place - resultat
		print("Votre nouvelle place est :", lol)
	if place == 65 :
		print("VOUS AVEZ GAGNE")
		
	try: input = raw_input
	except NameError: pass
	print(input("Appuyez sur une touche pour relancer le dé"))


