# -*- coding: utf-8 -*-
"""
Classe représentant un attribut de la dataset
@author: yawoumihani Hassani
"""

import numpy as np
eps = np.finfo(float).eps

class Attribut:
    def __init__(self,nomAttribut):
        self.liste_valeurs = {}
        self.nomAttribut = nomAttribut
    
    # getter method
    def get_liste_valeurs(self):
        return self.liste_valeurs
    
    # getter method
    def get_nomAttribut(self):
        return self.nomAttribut
    
    # setter method
    def set_liste_valeurs(self, liste_valeurs):
        self.liste_valeurs = liste_valeurs
        
    # Fonction qui calcule et retourne l'enthropie d'un attribut    
    def enthropieAttribut(self, d):
        attribut = self.get_nomAttribut()
        variables_cibles = d.play.unique()  #Retourne tous les 'Yes' and 'No'
        variables = d[attribut].unique()    #Retourne les variables possibles de cet attribut

        enthropie = 0
        for variable in variables:
            enthropie_chaque_variable = 0
            for variable_cible in variables_cibles:
                # numérateur
                num = len(d[attribut][d[attribut]==variable][d.play ==variable_cible])
                # dénominateur
                den = len(d[attribut][d[attribut]==variable])
                fraction = num/(den+eps)  #pi
                #Calcule l'enthropie d'une variables possibles
                enthropie_chaque_variable += -fraction*np.log(fraction+eps) 
            fraction2 = den/len(d)
            enthropie += -fraction2*enthropie_chaque_variable  
        
        return(abs(enthropie))

 
    # Fonction qui retourne le taux de gain d'information de l'attribut
    def gain_inf(self,enthropie_dataset,dataset):
        return (enthropie_dataset - self.enthropieAttribut(dataset))
    
    
    
        
