from Action import Action

class Environnement:
    
    def __init__(self, liste_actions:list[Action]) -> None:
        self.liste_actions = liste_actions