
class Etat:
    
    def __init__(self, nom:str, valeur:float|int=0) -> None:
        self.nom = nom
        self.valeur = valeur
        
    def __str__(self) -> str:
        return f"{self.nom}: {self.valeur}"


class DiceSet:
    
    def __init__(self, *args):
        self.dices = list(args)
        
    def append(self, other):
        self.dices.append(other)
        
    def __eq__(self, __value:object) -> bool:
        if __value is not None and isinstance(__value, self.__class__()):
            return sorted(self.dices) == sorted(__value.dices)
        
        return False
    
    def max_same_value(self):
        previous_value = None
        current_same = 0
        max_same = 0
        for x in sorted(self.dices):
            if x == previous_value:
                current_same += 1
            else:
                current_same = 1
            
            if current_same > max_same:
                max_same = current_same
            
            previous_value = x
        
        return max_same
    
class Etat421(Etat):
    
    def __init__(self, de1:int, de2:int, de3:int, valeur:float):
        name = str(de1) + "-" + str(de2) + "-" +  str(de3)
        super(self).__init__(name, valeur)
        self.des = DiceSet(de1, de2, de3)
        
    def __eq__(self, __value: object) -> bool:
        if __value is not None and isinstance(__value, self.__class__()):
             return self.des == __value.des
        return False
