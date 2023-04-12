from Action import Action, Mouvement
from Agent import Agent
from Etat import Etat
from Environnement import Environnement


ei= Etat("Init", 0)
e1 = Etat("1-1", 10)
e2 = Etat("1-2", 20)
e3 = Etat("1-3", 3)
e4 = Etat("1-4", 4)
e5 = Etat("1-5", 5)
e6 = Etat("1-6", 6)
e7 = Etat("2-2", 11)
e8 = Etat("2-3", 3)
e9 = Etat("2-4", 4)
e10 = Etat("2-5", 5)
e11 = Etat("2-6", 6)
e12 = Etat("3-3", 12)
e13 = Etat("3-4", 4)
e14 = Etat("3-5", 5)
e15 = Etat("3-6", 6)
e16 = Etat("4-4", 13)
e17 = Etat("4-5", 5)
e18 = Etat("4-6", 6)
e19 = Etat("5-5", 14)
e20 = Etat("5-6", 6)
e21 = Etat("6-6", 15)

lst_etat = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21]

lst_mouvements = []
for etat in lst_etat:
    lst_mouvements.append(Mouvement(etat, 1/18))
    lst_mouvements.append(Mouvement(etat, 1/6))

actionInitiale = Action("L", ei, [mouv1, mouv2, mouv3, mouv4, mouv5, mouv6], 1)
action1g = Action("1G", e1, [g1], 0)
action1l = Action("1L", e1, [mouv1, mouv2, mouv3, mouv4, mouv5, mouv6], -0.1)
action2g = Action("2G", e2, [g2], 0)
action2l = Action("2L", e2, [mouv1, mouv2, mouv3, mouv4, mouv5, mouv6], -0.1)
action3g = Action("3G", e3, [g3], 0)
action3l = Action("3L", e3, [mouv1, mouv2, mouv3, mouv4, mouv5, mouv6], -0.1)
action4g = Action("4G", e4, [g4], 0)
action4l = Action("4L", e4, [mouv1, mouv2, mouv3, mouv4, mouv5, mouv6], -0.1)
action5g = Action("5G", e5, [g5], 0)
action5l = Action("5L", e5, [mouv1, mouv2, mouv3, mouv4, mouv5, mouv6], -0.1)
action6g = Action("6G", e6, [g6], 0)
action6l = Action("6L", e6, [mouv1, mouv2, mouv3, mouv4, mouv5, mouv6], -0.1)

env = Environnement([actionInitiale, action1g, action1l,action2g,action2l,action3g,action3l,action4g,action4l,action5g,action5l,action6g,action6l])

joueur = Agent("Joe", env, ei, 0.9, 0.8, 0.5)
joueur.simuler(1000)