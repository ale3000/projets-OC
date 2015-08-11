"""Fichier lancant le programme"""
from commande import *

nom = raw_input("Votre nom? ")
prenom = raw_input("Votre prenom? ")
try:
	age = int(raw_input("Votre age? "))
except :
	print("Erreur, par defaut: 19")
	age = 19

pers = Programme(nom,prenom,age)

pers.Majeur
