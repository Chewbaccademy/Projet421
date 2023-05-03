
class Etat:
    
    def __init__(self, nom:str, valeur:float|int=0) -> None:
        self.nom = nom
        self.valeur = valeur
        
    def __str__(self) -> str:
        return f"{self.nom}: {self.valeur}"