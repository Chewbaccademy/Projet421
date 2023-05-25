
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
        
    def __len__(self):
        return len(self.dices)
    
    def __contains__(self, other):
        if not isinstance(other, DiceSet):
            return False
        
        serial_self = ''.join([str(x) for x in sorted(self.dices)])
        serial_other = ''.join([str(x) for x in sorted(other.dices)])
        
        return serial_other in serial_self
    
    def __sub__(self, other):
        new_set = self.copy()
        for dice in other.dices:
            new_set.dices.remove(dice)
            
        return new_set
        
    def __eq__(self, __value:object) -> bool:
        if __value is not None and type(__value) == type(self):
            return sorted(self.dices) == sorted(__value.dices)
        return False
    
    def __tuple__(self):
        return tuple(self.dices)
    
    def __str__(self):
        return str(self.dices)
    
    
    def __iter__(self):
        return (dice for dice in self.dices)
    
    def __next__(self):
        return next(self.dices)
    
    def __getitem__(self, item):
         return self.dices[item]
    
    def copy(self):
        return DiceSet(*self.dices)
    
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
    

