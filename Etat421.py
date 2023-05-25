from Etat import Etat, DiceSet
from Action import Action, Mouvement
import math as m

class EtatsList:
    
    def __init__(self):
        e1 = Etat421((4,2,1), 800)
        e2 = Etat421((1,1,1), 700)
        e3 = Etat421((1,1,6), 406)
        e4 = Etat421((1,1,5), 405)
        e5 = Etat421((1,1,4), 404)
        e6 = Etat421((1,1,3), 403)
        e7 = Etat421((1,1,2), 402)
        e8 = Etat421((6,6,6), 306)
        e9 = Etat421((5,5,5), 303)
        e10 = Etat421((4,4,4), 304)
        e11 = Etat421((3,3,3), 303)
        e12 = Etat421((2,2,2), 302)
        e13 = Etat421((1,2,3), 203)
        e14 = Etat421((2,3,4), 204)
        e15 = Etat421((3,4,5), 205)
        e16 = Etat421((4,5,6), 206)
        e17 = Etat421((2,2,1), 0)
        e18 = Etat421((6,1,2), 106)
        e19 = Etat421((6,1,3), 106)
        e20 = Etat421((6,1,4), 106)
        e21 = Etat421((6,1,5), 106)
        e22 = Etat421((6,1,6), 106)
        e23 = Etat421((6,2,2), 106)
        e24 = Etat421((6,2,3), 106)
        e25 = Etat421((6,2,4), 106)
        e26 = Etat421((6,2,5), 106)
        e27 = Etat421((6,2,6), 106)
        e28 = Etat421((6,3,3), 106)
        e29 = Etat421((6,4,3), 106)
        e30 = Etat421((6,5,3), 106)
        e31 = Etat421((6,6,3), 106)
        e32 = Etat421((6,4,4), 106)
        e33 = Etat421((6,4,6), 106)
        e34 = Etat421((6,5,5), 106)
        e35 = Etat421((6,5,6), 106)
        e36 = Etat421((5,5,4), 105)
        e37 = Etat421((5,5,3), 105)
        e38 = Etat421((5,5,2), 105)
        e39 = Etat421((5,5,1), 105)
        e40 = Etat421((5,4,2), 105)
        e41 = Etat421((5,4,1), 105)
        e42 = Etat421((5,3,3), 105)
        e43 = Etat421((5,3,2), 105)
        e44 = Etat421((5,3,1), 105)
        e45 = Etat421((5,2,2), 105)
        e46 = Etat421((5,2,1), 105)
        e47 = Etat421((4,4,3), 104)
        e48 = Etat421((4,4,2), 104)
        e49 = Etat421((4,4,1), 104)
        e50 = Etat421((4,3,3), 104)
        e51 = Etat421((4,3,1), 104)
        e52 = Etat421((4,2,2), 104)
        e53 = Etat421((3,3,2), 103)
        e54 = Etat421((3,3,1), 103)
        e55 = Etat421((3,2,2), 103)



        self.lst_etats = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21, e22, e23, e24, e25, e26, e27, e28, e29, e30, e31, e31, e32, e33, e34, e35, e36, e37, e38, e39, e40, e41, e42, e43, e44, e45, e46, e47, e48, e49, e50, e51, e52, e53, e54, e55]


class Etat421(Etat):
    
    def __init__(self, des:tuple, valeur:float):
        name = ""
        for de in des:
            name += str(de) + "-"
        name = name[:-1]
        super().__init__(name, valeur)
        self.des = DiceSet(*des)
        
    def __eq__(self, __value: object) -> bool:
        if __value is not None and type(__value) == type(self):
             return self.des == __value.des
        return False
    
    def __sub__(self, other):
        self.des = self.des - other.des
        
    def __contains__(self, other):
        return other.des in self.des
    
    def probabilite_avoir_etat(self, set_base:DiceSet=None):
        if set_base is None:
            return round((6 / m.factorial(self.des.max_same_value())) / 216, 9)
        
        if set_base not in self.des:
            return 0
        
        if len(set_base) == 2:
            return 1/6
        
        if len(set_base) == 1:
            sub_des = self.des - set_base
            sub_etat = Etat421(tuple(sub_des), self.valeur)
            return round((2 / m.factorial(sub_etat.des.max_same_value())) / 36, 9)
        
        round()
        
        pass
    
    def genere_actions(self, lst_etats:list):
        lst_actions = []
        
        # actions de tout relancer
        lst_movt = []
        for e in lst_etats:
            lst_movt.append(Mouvement(e, e.probabilite_avoir_etat()))
            
        lst_actions.append(Action("f:%s-t:RA" % self.nom, self, lst_movt.copy(), -1))
        
        
        # relancer 2 de
        for de_garde in self.des:
            lst_movt = []
            for e in [etat for etat in lst_etats if DiceSet(de_garde) in etat.des]:
                lst_movt.append(Mouvement(e, e.probabilite_avoir_etat(DiceSet(de_garde))))
            lst_actions.append(Action("f:%s-t:R[%s]" % (self.nom, str(self.des - DiceSet(de_garde))), self, lst_movt.copy(), -1))
            
        # relancer 1 de
        for i in range(len(self.des)):
            de_garde1 = self.des[i]
            for j in range(len(self.des)):
                if i == j:
                    continue
                de_garde2 = self.des[j]
                de_garde = (de_garde1, de_garde2)
                lst_movt = []
                for e in [etat for etat in lst_etats if DiceSet(*de_garde) in etat.des]:
                    lst_movt.append(Mouvement(e, e.probabilite_avoir_etat(DiceSet(*de_garde))))
                lst_actions.append(Action("f:%s-t:R[%s]" % (self.nom, str(self.des - DiceSet(*de_garde))), self, lst_movt.copy(), -1))
        
        # tout garder
        lst_movt = []
        lst_movt.append(Mouvement(self, 1))
        lst_actions.append(Action("f:%s-t:G" % self.nom, self, lst_movt.copy(), 0))
        
        
        return lst_actions
                
                
            
            
        
        