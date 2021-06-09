# -*- coding: utf-8 -*-
"""
Classe permettant d'extraire les attributs
et les valeurs d'un jeu de données

@author: yawoumihani Hassani
"""

import pandas as pd
import numpy as np
from Attribut import Attribut


"""
 Classe permettant d extraire le jeu de données sous forme de tableau 
 et initialise les valeurs possibles pour un attribut 
"""

class Ensemble:
    
    def __init__(self,file):
        self.data = pd.read_csv(file)
        self.attributs = []
        dic = {}
        for attribut_nom in self.data.columns:
            a = Attribut(attribut_nom)
            self.attributs.append(a) 
        
        # Récupérer les valeurs pour chaque attribut et les ajoute à l'attribut
        for att in self.get_attributs():
            valeur = set(self.data.get(att.get_nomAttribut()))
            dic[att.get_nomAttribut()] = valeur
            att.set_liste_valeurs(dic)
    
    # Getter
    def get_data(self):
        return self.data
    
    # Setter
    def set_data(self, data):
        self.data = data 
    
    # Récupérer les attributs d'un jeu de données
    def get_attributs(self):
        return self.attributs
    
    #Retourne la valeur de l'enthropie de l'ensemble des données
    def enthropieData(self):
        enthropie_data = 0  
        valeurs = self.get_data().play.unique()  
        for valeur in valeurs:
            fraction = self.get_data().play.value_counts()[valeur]/len(self.get_data().play)  
            enthropie_data += -fraction*np.log2(fraction)
        return enthropie_data
    
    def enthropieChaqueAttribut(self):
        d = self.get_attributs()
        enthropie_attributs = {} 
        for attribut in d[:-1]: #Car l'attribut à prédire est play
            enthropie_attributs[attribut.get_nomAttribut()] = attribut.enthropieAttribut(self.get_data())
        return enthropie_attributs
    
    def gainChaqueAttribut(self):
        d = self.get_attributs()
        e = self.enthropieChaqueAttribut()
        gain_informations = {}
        for attribut in d[:-1]:
            gain_informations[attribut.get_nomAttribut()] = attribut.gain_inf(self.enthropieData(),self.get_data())  
        return gain_informations
    
    def gainPlusEleve(self,tous_les_gains):
        plus_eleve = max(tous_les_gains, key=lambda key: tous_les_gains[key])
        return plus_eleve
    
    


