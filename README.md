# Arbre_de_decisions

## Contexte du projet

Ce projet s’inscrit dans le cadre du module PROJET631 – Projet Algorithmique de la formation IDU.

L’objectif est d’appliquer les notions de programmation orientée objet au sein d'un algorithme d'arbre de décisions.
Nous avons donc pour objectif comprendre et implémenter l’algorithme Id3 l’enrichir à travers différentes extensions proposées dans l’algorithme C4.5.
## Cahier des charges

Le principe de l’algorithme Id3 qui réalise la construction de l’arbre à partir de S est le suivant :
1. Sélectionner le « meilleur » attribut Ai pour faire croître l’arbre :
 Le « meilleur » attribut est celui qui possède le gain d’information le plus élevé pour S.
 Un nouveau noeud n(Ai) est ajouté à l’arbre et des branches sont créées pour chaque valeur possible de l’attribut Ai, i.e. vi1, vi2, …, viK.
2. Partitionner l’ensemble d’apprentissage « local » S en K sous-ensembles S1, S2, …, SK, chaque sous-ensemble regroupant les données satisfaisant au test Ai = vik, k= 1, ..., K.
3. Le processus de construction continue (étapes 1 et 2) jusqu’à satisfaire une des conditions d’arrêt suivantes :
 L’ensemble d’exemples associés au noeud courant est vide.
 Tous les exemples d’apprentissage associés au noeud courant ont la même valeur de classe, auquel cas une feuille avec cette valeur de classe est retournée.
 Tous les attributs ont été utilisés sur la branche en cours de développement, auquel cas une feuille est retournée avec la classe majoritaire parmi les exemples associés au noeud courant.
## Utilisation

Pour faire ce projet j'ai utilisé :
- Python

Pour executer le code, il suffit d'éxecuter le fichier Main.py qui contient le programme principal