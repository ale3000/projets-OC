"""Ceci est le premier fichier Python (3.x)"""
class Programme :
	"""Classe pour notre programme"""
	def __init__(self,nom,prenom,age):
		self.nom = nom
		self.prenom = prenom
		self.age = age
	
	def Majeur(self) :
		if self.age > 18 and self.< 21 :
			print("Oui et non... :/")
		elif self.age > 21 :
			print("Oui et oui ;)")
		else :
			print("non :(")
