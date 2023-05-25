from Action import Action, Mouvement
from Agent import Agent
from Etat421 import Etat, EtatsList
from Environnement import Environnement
import math as m


ei= Etat("Init", 0)
etatL = EtatsList()
lst_etats = etatL.lst_etats


lst_movt = []
for e in lst_etats:
    lst_movt.append(Mouvement(e, e.probabilite_avoir_etat()))
print([str(m) for m in lst_movt])
lst_actions = [Action("f:Init-t:RA", ei, lst_movt, 1)]
for e in lst_etats:
    lst_actions += e.genere_actions(lst_etats)
print([str(m) for m in lst_actions])

env = Environnement(lst_actions)

joueur = Agent(
                nom="Joe"
                , environnement=env
                , etat_initial=ei
                , tx_apprentissage=0.9
                , tx_exploration=0.9
                ,facteur_attenuation=0.1)
joueur.simuler(1000)


