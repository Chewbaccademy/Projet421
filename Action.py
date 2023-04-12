from Etat import Etat
import random as rd

class Mouvement:
    
    def __init__(self, etat_final:Etat, probabilite:float=1.0):
        self.etat_final = etat_final
        if 0.0 < probabilite <= 1.0:
            self.probabilite = probabilite
        else:
            raise ValueError("Création de mouvement impossible : la probabilité doit être dans l'intervalle ]0,1]")

class Action:
    
    def __init__(self, nom:str, etat_initial:Etat, mouvements:list[Mouvement], recompense:float|int):
        # filtres
        if sum([mouvement.probabilite for mouvement in mouvements]) != 1:
            raise ValueError(f"Création de l'action {nom} impossible : la somme des probabilités est != 1")
        
        self.nom = nom
        self.etat_initial = etat_initial
        self.mouvements = mouvements
        self.recompense = recompense
        
    def tirer_etat(self):
        etats = [mouvement.etat_final for mouvement in self.mouvements]
        probabilites = [mouvement.probabilite for mouvement in self.mouvements]
        
        return rd.choices(etats, weights=probabilites)
    
    def consommer(self) -> tuple(Etat, float):
        return (self.tirer_etat(), self.recompense)