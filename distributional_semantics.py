#!/usr/bin/python3
# -*- coding:utf-8 -*-

#Pour tout ce qui est calcul matriciel on importe numpy
import numpy as np

class DistributionalSemantics :
	'''Classe contenant de Semantique Distributionnelle
	Attributs :
		
	'''
	
	def __init__(self) :
		'''Constructeur de la classe
		En entrée :
		
		'''
		
		#Définion des attributs
		W = {} #Dictionnaire des Wr ou les clés sont des pairs de tags
		
	def calcul_Wr(self,corpus) :
		'''Méthode qui calcule, selon un corpus de forme mot/tag, les différents Wr possibles
		En entrée :
			corpus : 
		En sortie :
		'''
		
		#Le corpus est une liste de paires mots/tags
		#Parcours de la liste mot tag à la recherche de nouvelles paire de tags de suite
		for i in range(0,len(corpus)-1) :
			tag1 = corpus[i][1] #Le ième tag
			tag2 = corpus[i+1][1] #Le ième +1 tag
			if !((tag1,tag2) in W.keys()):
				#On ajoute la paire dans le dictionnaire
				
				#On parcours tout le corpus à la recherche des paires de tags tag1 tag2
				for j in range(0,len(corpus)-1):
					
		
	def composition(self,u,v) :
		'''Méthode de compoistion de vecteurs de sens pour former de plus grands vecteurs
		En entrée :
			u : 
			v :
		En sortie :
			p :
		'''
		#Pour la composition nous avons besoin de déterminer la bonne matrice Wr à utiliser
		Wr = #Voir la forme qu'on va donner à un dico de Wr
		
		#Concaténation verticale des vecteurs de u et de v
		uv = np.hstack((u,v))
		p = np.linalg.dot(uv,Wr)
		return p
		
	def decomposition_unitaire_corpus(self,p) :
		'''Méthode de décomposition de vecteurs de sens de phrases en deux vecteurs de sens
		Cette méthode se base du un Wr connu de l'objet de la classe.
		
		IMPORTANT : À utiliser si le but est d'inverser purement une composition comme pour une traduction.
		
		En entrée :
			p :
		En sortie
			u :
			v :
		'''
				
		#Transformer P en UV connaissant la fonction de composition adéquate
		uv = np.dot(p,W)
	
	def decomposition_unitaire_inverse(self,p)
		'''Méthode de décomposition de vecteurs de sens de phrases en deux vecteurs de sens
		Cette méthode méthode se base sur un Wr' calculé sur un corpus
		
		IMPORTANT : à utiliser pour bien appréhender les mots qui changent de sens selon le context.
		
		En entrée :
			p :
		En sortie
			u :
			v :
		'''
		
	
