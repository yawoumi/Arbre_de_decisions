# -*- coding: utf-8 -*-
"""
Programme principal
@author: yawoumihani Hassani
"""
from EnsembleData import Ensemble
import numpy as np
import pandas as pd

def creationArbreId3(ensemble,df,l_attributs,label,parent):
    
        arbre_decision = {}   
        dataset = ensemble
        dat = np.unique(df[label],return_counts = True)
        unique_data = np.unique(df[label])
        
        #Condition d'arrêt 1: si la liste est vide
        if len(unique_data) == 0:
            return unique_data[0]
        
        #Condition d'arrêt 2: tous les attributs ont le même nom
        elif len(df) == 0:
            return unique_data[np.argmax(dat[1])]
        
        #Condition d'arrêt 3: s'il n'y a plus d'attributs à tester
        elif len(l_attributs) == 0:
            return parent
        
        else:
            parent = unique_data[np.argmax(dat[1])]
            gains = dataset.gainChaqueAttribut()
            gain_max = dataset.gainPlusEleve(gains)
            
            for valeur in np.unique(df[gain_max]):
                ensemble_p = df.where(df[gain_max] == valeur).dropna()
                ensemble_p.to_csv("Data/ens_partitionne.csv", index = False, header = True)
                s = "Data/ens_partitionne.csv"
                ensemble_partitionne = Ensemble(s)
                df = ensemble_partitionne.get_data()
                
                min_arbre = creationArbreId3(ensemble_partitionne,df,l_attributs,label, parent)
                arbre_decision[gain_max][valeur] = min_arbre
        return arbre_decision

def prediction_play(donnees_test,arbre_decision):
    for noeuds in arbre_decision.keys():
        valeur = donnees_test[noeuds]
        arbre_decision = arbre_decision[noeuds][valeur]
        
        valPrediction = 0
        if type(arbre_decision) is dict:
            valPrediction = prediction_play(donnees_test,arbre_decision)
        else:
            valPrediction = arbre_decision
            break;
    return valPrediction
            
def main():
    # PHASE APPRENTISSAGE
    #On initialise
    ensemble = Ensemble("Data/golf.csv")
    df = ensemble.get_data()
    label = 'play'
    l_attributs = ensemble.get_attributs()
    parent = None
    
    # Création de l'arbre par apprentissage
    arbre_decision = creationArbreId3(ensemble,df,l_attributs,label,parent)
    
    #PHASE PREDICTION
    #tests:
    test = {'humidity': 'normal', 'wind':1.0}
    test2 = {'humidity': 'normal', 'outlook':'rain'}
    donnees_test = pd.Series(test)
    donnees_test2 = pd.Series(test2)
    valeurPredictive = prediction_play(donnees_test, arbre_decision)
    valeurPredictive2 = prediction_play(donnees_test2, arbre_decision)
    print(valeurPredictive)
    print(valeurPredictive2)
    
    
    

    
            
# Calls the main function
if __name__ == "__main__":
    main() 
